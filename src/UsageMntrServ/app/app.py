# app.py
from flask import Flask
from routes import define_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_activity.db'

# Initialize the database
from models import db
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Define route handlers
define_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
