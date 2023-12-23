# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  
db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()  # Create database tables before running the app
    app.run(host='0.0.0.0', port=5002, debug=True)
