
# src/user_acc_mgmt_serv/models.py

from __init__ import user_collection

user_collection['id']
user_collection['first_name']
user_collection['last_name']
user_collection['username']
user_collection['password']
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50), nullable=False)  # Corrected field name
#     last_name = db.Column(db.String(50), nullable=False)   # Corrected field name
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(50), nullable=False)

# def __repr__(self):
#     return f"<User {self.username}>"
