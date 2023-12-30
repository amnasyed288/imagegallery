from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
