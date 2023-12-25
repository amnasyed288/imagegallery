from flask import jsonify, request
from models import UserActivityModel, db
import datetime

def log_activity(user_id, activity_type, data_volume):
    try:
        activity = UserActivityModel(user_id=user_id, activity_type=activity_type, data_volume=data_volume)
        db.session.add(activity)
        db.session.commit()
    except Exception as e:
        raise e

def get_daily_usage(user_id):
    try:
        today = datetime.datetime.utcnow().date()
        daily_usage = db.session.query(db.func.sum(UserActivityModel.data_volume)).filter(
            UserActivityModel.user_id == user_id,
            db.func.DATE(UserActivityModel.timestamp) == today
        ).scalar() or 0.0

        return daily_usage
    except Exception as e:
        raise e

def send_alert(user_id):
    try:
        # Placeholder for sending alerts (log a warning message)
        alert_message = f"ALERT: User {user_id} has exceeded the daily usage threshold!"
        app.logger.warning(alert_message)

    except Exception as e:
        raise e

def define_routes(app):
    @app.route("/")
    def works():
        return "works"
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
