
# src/user_acc_mgmt_serv/__init__.py
from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


# from flask_sqlalchemy import SQLAlchemy

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite for simplicity
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['imagegallery']
user_collection = db['userdata']

# db = client['imagegallery']
# user_storage_collection = db['userimage']
