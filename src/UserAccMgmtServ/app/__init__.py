
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

# client = MongoClient('mongodb+srv://msaadanbese21seecs:<password>@cluster0.gljno9v.mongodb.net/')



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://msaadanbese21seecs:driweswa@cluster0.gljno9v.mongodb.net/imagegallery"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['imagegallery']
user_collection = db['gallery']
