# routes.py
from flask import jsonify, request
from models import UserActivityModel, db
from usagemntrserv import log_activity, get_daily_usage, send_alert

def define_routes(app):
    @app.route('/trackActivity', methods=['POST'])
    def track_activity():
        try:
            req_data = request.get_json()

            if 'user_id' not in req_data or 'activity_type' not in req_data or 'data_volume' not in req_data:
                return jsonify({"error": "Invalid request data"}), 400

            user_id = req_data['user_id']
            activity_type = req_data['activity_type']
            data_volume = req_data['data_volume']

            log_activity(user_id, activity_type, data_volume)

            return jsonify({"message": "User activity logged successfully"})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/checkUsage/<int:user_id>', methods=['GET'])
    def check_daily_usage(user_id):
        try:
            daily_threshold = 25.0

            daily_usage = get_daily_usage(user_id)

            return jsonify({"user_id": user_id, "daily_usage": daily_usage, "threshold": daily_threshold})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/alertUser/<int:user_id>', methods=['POST'])
    def alert_user(user_id):
        try:
            daily_threshold = 25.0

            daily_usage = get_daily_usage(user_id)

            if daily_usage > daily_threshold:
                send_alert(user_id)

            return jsonify({"message": "Alert sent successfully"})

        except Exception as e:
            return jsonify({"error": str(e)}), 500
