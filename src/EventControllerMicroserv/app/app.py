from __init__ import app
from flask import Flask, request, jsonify
import requests


# Replace these URLs with the actual URLs of your registration, storage, and loginfo microservices
REGISTRATION_MICROSERVICE_URL = "http://localhost:5001/register"
STORAGE_MICROSERVICE_URL = "http://localhost:5002//upload"
LOGINFO_MICROSERVICE_URL = "http://localhost:5003/loginfo"


@app.route('/register_event', methods=['POST'])
def register_event():
    try:
        data = request.json
        # Forward registration event to the Storage Microservice
        storage_response = requests.post(
            "http://localhost:5001/signup", json=data)

        return jsonify({

            'message': 'Event forwarded to microservices successfully.'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)
