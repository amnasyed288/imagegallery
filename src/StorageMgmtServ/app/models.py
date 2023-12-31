# models.py
from pymongo import MongoClient
from gridfs import GridFS


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://msaadanbese21seecs:driweswa@cluster0.gljno9v.mongodb.net/imagegallerydata"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['imagegallerydata']
user_storage_collection = db['images']

fs = GridFS(db)
