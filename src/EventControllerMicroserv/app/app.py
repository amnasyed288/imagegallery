 
from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
import requests

app = Flask(__name__)
CORS(app)

# Replace these URLs with the actual URLs of your registration and storage microservices
REGISTRATION_MICROSERVICE_URL = "http://localhost:5001/register"
STORAGE_MICROSERVICE_SIGNUP = "http://localhost:5002/signup"
STORAGE_MICROSERVICE_UPLOAD = "http://localhost:5002/upload"

@app.route('/register', methods=['POST'])
def register_event():
    try:
        data = request.json

        # Forward registration event to the Registration Microservice
        registration_response = requests.post(REGISTRATION_MICROSERVICE_URL, json=data)

        # Check if registration was successful
        if registration_response.status_code == 200 and registration_response.json().get('status') == 'success':
            # Log the success
        

            # Extract user_id from the registration response
            user_id = registration_response.json().get('user_id')

            # Forward the same payload to the Storage Microservice if registration is successful
            storage_response = requests.post(STORAGE_MICROSERVICE_SIGNUP, json=user_id)

            # Log the storage response
            print("Storage response:", storage_response.json())

            return jsonify({
                'registration_response': registration_response.json(),
                'storage_response': storage_response.json(),
                'message': 'Event forwarded to microservices successfully.'
            })
        
        else:
            return jsonify({
                'registration_response': registration_response.json(),
                'message': 'Registration failed. Event not forwarded to storage microservice.'
            })

    except Exception as e:
        # Log the exception
        print("Exception:", e)
        return jsonify({'error': str(e)}), 500



@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        data = request.json

        # Forward registration event to the Registration Microservice
        upload_response = requests.post(STORAGE_MICROSERVICE_UPLOAD, json=data)

        # Check if registration was successful
        if upload_response.status_code == 200 and upload_response.json().get('status') == 'success':
            # Log the success
        

            # Extract user_id from the registration response
            user_id = registration_response.json().get('user_id')

            # Forward the same payload to the Storage Microservice if registration is successful
            storage_response = requests.post(STORAGE_MICROSERVICE_SIGNUP, json=user_id)

            # Log the storage response
            print("Storage response:", storage_response.json())

            return jsonify({
                'registration_response': registration_response.json(),
                'storage_response': storage_response.json(),
                'message': 'Event forwarded to microservices successfully.'
            })
        
        else:
            return jsonify({
                'registration_response': registration_response.json(),
                'message': 'Registration failed. Event not forwarded to storage microservice.'
            })

    except Exception as e:
        # Log the exception
        print("Exception:", e)
        return jsonify({'error': str(e)}), 500










if __name__ == '__main__':
    app.run(port=5000, debug=True)