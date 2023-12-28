# models.py
from pymongo import MongoClient
from gridfs import GridFS

client = MongoClient('mongodb://localhost:27017/')
db = client['imagegallery']
user_storage_collection = db['userimage']
fs = GridFS(db)
