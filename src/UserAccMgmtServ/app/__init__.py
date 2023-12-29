 
# src/user_acc_mgmt_serv/__init__.py
from flask import Flask


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from flask_cors import CORS
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



