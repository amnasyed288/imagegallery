# routes.py
from flask import Flask, jsonify, request
from models import db, UserUsage
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use the same URI as in app.py
db.init_app(app)

DAILY_THRESHOLD = 25

@app.route('/record-usage', methods=['POST'])
def record_usage():
    data = request.get_json()
    user_id = data.get('user_id')
    data_volume = data.get('data_volume')

    if user_id and data_volume:
        date_today = datetime.date.today()
        new_usage = UserUsage(user_id=user_id, date=date_today, data_volume=data_volume)
        db.session.add(new_usage)
        db.session.commit()

        if data_volume > DAILY_THRESHOLD:
            return jsonify({"message": "Usage recorded. Warning: Daily threshold exceeded!"})
        else:
            return jsonify({"message": "Usage recorded successfully"})
    else:
        return jsonify({"error": "Invalid data provided"}), 400

@app.route('/get-usage/<user_id>', methods=['GET'])
def get_user_usage(user_id):
    user_usage = UserUsage.query.filter_by(user_id=user_id).all()
    if not user_usage:
        return jsonify({"user_id": user_id, "message": "User not found"}), 404
    return jsonify({"user_id": user_id, "usage_records": [usage.__dict__ for usage in user_usage]})
