 
# src/user_acc_mgmt_serv/routes.py
from flask import request, jsonify
from __init__ import app, db
from models import User

@app.route("/")
def works():
    return "works"

# API to register a new user
@app.route('/api/user/register', methods=['POST'])
def register_user():
    data = request.json

    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})

# API to login (authentication)
@app.route('/api/user/login', methods=['POST'])
def login_user():
    data = request.json

    user = User.query.filter_by(username=data['username'], password=data['password']).first()

    if user:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'error': 'Invalid credentials'})
