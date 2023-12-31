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

        already_email = data.get('email')

        if user_collection.find_one({'email': already_email}):
            return jsonify({'message': 'User already signed up!'}), 400
        
        new_user = {
            'first_name': data.get('firstName', ''),
            'last_name': data.get('lastName', ''),
            'email': data.get('email', ''),
            'password': data.get('password', '')
        }

        result = user_collection.insert_one(new_user)
        
        # Get the inserted document, including the generated '_id'
        user_document = user_collection.find_one({'_id': result.inserted_id})
        
        # Extract the 'user_id' (MongoDB _id converted to str)
        user_id = str(user_document.get('_id'))

        

        return jsonify({'status': 'success', 'message': 'User registered successfully', 'user_id': user_id}), 200
    

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
            
            return jsonify({'status': 'success','message': 'Login successful'})
        else:
            return jsonify({'error': 'Invalid credentials'})

    return jsonify({'message': 'Use POST method to login'})
