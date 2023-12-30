# src/user_acc_mgmt_serv/routes.py
from flask import request, jsonify
from __init__ import app, user_collection
import requests


@app.route("/")
def works():
    return "works"

# API to register a new user


@app.route('/register', methods=['POST'])
def register_user():
    if request.method == 'POST':
        data = request.json
        new_user = {
            'first_name': data.get('firstName', ''),
            'last_name': data.get('lastName', ''),
            'email': data.get('email', ''),
            'password': data.get('password', '')
        }
        user_collection.insert_one(new_user)
        requests.post("http://localhost:5000/register_event", json=data)

        return jsonify({'message': 'User registered successfully'})

    return jsonify({'message': 'Use POST method to register a new user'})


# API to login (authentication)
@app.route('/login', methods=['POST'])
def login_user():
    if request.method == 'POST':
        data = request.json

        email = data.get('email', '')
        password = data.get('password', '')

        user = user_collection.find_one(
            {'email': email, 'password': password})
        # user = User.query.filter_by(
        #     username=data['username'], password=data['password']).first()

        if user:
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'error': 'Invalid credentials'})

    return jsonify({'message': 'Use POST method to login'})
