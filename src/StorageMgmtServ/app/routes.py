from app import app, user_storage_collection, fs
from flask import request, jsonify, send_file
from bson import ObjectId
from flask import Flask

app = Flask(__name__)


@app.route('/signup', methods=['POST'])
def signup():
    user_id = request.form.get('user_id')

    if user_storage_collection.find_one({'user_id': user_id}):
        return jsonify({'Alert': 'User already signed up!'}), 400

    user_storage_collection.insert_one({
        'user_id': user_id,
        'used_storage': 0,
        'total_storage': 10 * 1024
    })

    return jsonify({'message': 'User signed up successfully!'})


@app.route('/upload', methods=['POST'])
def upload():
    user_id = request.form.get('user_id')
    file = request.files.get('file')
    file_name = request.form.get('file_name')

    user_data = user_storage_collection.find_one({'user_id': user_id})

    if not user_data:
        return jsonify({'error': 'User not found!'}), 404

    total_storage = user_data['total_storage']
    used_storage = user_data['used_storage']

    if file:
        file_content = file.read()
        file.seek(0)  # Move the cursor to the beginning of the file

        file_size = len(file_content) / 1024

        if used_storage + file_size <= total_storage:
            # Save the file to MongoDB using GridFS
            file_id = fs.put(file, filename=file_name)
            updated_storage = used_storage + file_size

            # Update user data in the database
            user_storage_collection.update_one(
                {'user_id': user_id},
                {
                    '$set': {
                        'used_storage': used_storage + file_size
                    },
                    '$push': {
                        'file_name': {'file_id': file_id, 'name': file_name, 'size': file_size}
                    }
                }
            )

            if used_storage >= 0.8 * total_storage:
                send_alert(user_id, used_storage, total_storage)

            return jsonify({'message': 'File uploaded successfully!', 'Alert': f'User {user_id} has used {updated_storage}KB out of {total_storage}KB storage.'})
        else:
            return jsonify({'error': 'Not enough storage!'}), 400
    else:
        return jsonify({'error': 'No file provided!'}), 400


@app.route('/delete', methods=['DELETE'])
def delete():
    user_id = request.form.get('user_id')
    file_name = request.form.get('file_name')

    user_data = user_storage_collection.find_one({'user_id': user_id})

    if not user_data:
        return jsonify({'error': 'User not found!'}), 404

    for file_sets in user_data['file_name']:
        if file_name == file_sets['name']:
            # Remove the file from GridFS
            fs.delete(ObjectId(file_sets['file_id']))

            # Update user data in the database
            user_storage_collection.update_one(
                {'user_id': user_id},
                {
                    '$set': {
                        'used_storage': user_data['used_storage'] - file_sets['size'],
                    },
                    '$pull': {
                        'file_name': {'name': file_name}
                    }
                }
            )
            return jsonify({'message': 'File deleted successfully!'})

    return jsonify({'error': 'File not found'}), 400


def send_alert(user_id, used_storage, total_storage):
    print(
        f"Alert: User {user_id} has used {used_storage}KB out of {total_storage}KB storage.")


@app.route('/display/<file_id>', methods=['GET'])
def display(file_id):
    try:
        # Retrieve the file from GridFS using the provided file_id
        file_data = fs.get(ObjectId(file_id))

        # Create an in-memory file-like object for sending the file content
        # in_memory_file = io.BytesIO(file_data.read())
        mimetype = 'image/jpeg'

        # Return the file using send_file
        return send_file(file_data, mimetype=mimetype)

    except Exception as e:
        return jsonify({'error': f'Error retrieving the file: {str(e)}'}), 50


if __name__ == '__main__':
    app.run(debug=True)
