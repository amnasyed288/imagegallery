# models.py
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserActivityModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    activity_type = db.Column(db.String(20), nullable=False)
    data_volume = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
