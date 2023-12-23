# models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    data_volume = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, date, data_volume):
        self.user_id = user_id
        self.date = date
        self.data_volume = data_volume
