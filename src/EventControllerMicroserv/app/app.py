from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
import requests

app = Flask(__name__)
CORS(app)

# Replace these URLs with the actual URLs of your registration and storage microservices
ACC_MGT_SERVICE_REGISTER = "http://user-serv:5001/register"
ACC_MGT_SERVICE_LOGIN = "http://user-serv:5001/login"
STORAGE_MICROSERVICE_SIGNUP = "http://stg-serv:5003/signup"
STORAGE_MICROSERVICE_UPLOAD = "http://stg-serv:5003/upload"
LOGGING_MICROSERVICE_UPLOAD = "http://log-serv:5007/upload"
DATAMTR_MICROSERVICE_UPLOAD = "http://usage-serv:5002/upload"


@app.route('/register', methods=['POST'])
def register_event():
    try:
        data = request.json

        # Forward registration event to the Registration Microservice
        registration_response = requests.post(
            ACC_MGT_SERVICE_REGISTER, json=data)

        # Check if registration was successful
        if registration_response.status_code == 200 and registration_response.json().get('status') == 'success':
            # Log the success

            # Extract user_id from the registration response
            user_id = registration_response.json().get('user_id')

            # Forward the same payload to the Storage Microservice if registration is successful
            storage_response = requests.post(
                STORAGE_MICROSERVICE_SIGNUP, json={'user_id': user_id})

            # Log the storage response
            print("Storage response:", storage_response.json())
            print('registration_response:', registration_response.json())

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


@app.route('/login', methods=['POST'])
def login_event():
    try:
        data = request.json

        # Forward registration event to the Registration Microservice
        login_response = requests.post(ACC_MGT_SERVICE_LOGIN, json=data)

        # Check if registration was successful
        if login_response.status_code == 200 and login_response.json().get('status') == 'success':
            # Log the success

            # Extract user_id from the registration response
            user_id = login_response.json().get('user_id')

            print('login_response:', login_response.json())

            return jsonify({
                'login_response': login_response.json(),
                'message': 'Event forwarded to microservices successfully.', 'user_id': user_id
            })

        else:
            return jsonify({
                'login_response': login_response.json(),
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

            # Log the storage response
            print("Storage response:", upload_response.json())

            logging_response = requests.post(
                LOGGING_MICROSERVICE_UPLOAD, json=data)

            return jsonify({

                'storage_response': upload_response.json(),
                'message': 'Event forwarded to microservices successfully.'
            })

        else:
            return jsonify({
                'message': 'Registration failed. Event not forwarded to storage microservice.'
            })

    except Exception as e:
        # Log the exception
        print("Exception:", e)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)
