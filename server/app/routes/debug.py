from app.models import User, Umuganda, Fine, Admin, Sector, Payment, Chat, Notification
from flask import Blueprint, jsonify, request
import os

debug_blue_print = Blueprint("debug_blue_print", __name__)

# this end point will be used to get all data for a db_manager / react client / or just for debugging

@debug_blue_print.route("/get_all_db_data", methods=["POST"]) # we used post for security
# @debug_blue_print.route("/get_all_db_data") 
def debug_data():
    secret_key = request.json.get("secret_key")

    if secret_key == os.getenv("SECRET_KEY"):
        return jsonify({
            "status" : "failed",
            "message": "access denied!",
            "reason": "invalid creditials"
        })
    try:
        users = User.query.all()
        umugandas = Umuganda.query.all()
        fines = Fine.query.all()
        admins = Admin.query.all()
        sectors = Sector.query.all()
        payments = Payment.query.all()
        chats = Chat.query.all()
        notifications = Notification.query.all()
    except:
        return "DB is clean. No data stored"

    return jsonify({
        "users": [user.return_dict() for user in users],
        "umugandas": [umuganda.return_dict() for umuganda in umugandas],
        "fines": [fine.return_dict() for fine in fines],
        "admins": [admin.return_dict() for admin in admins],
        "sectors": [sector.return_dict() for sector in sectors],
        "payments": [payment.return_dict() for payment in payments],
        "chats": [chat.return_dict() for chat in chats],
        "notifications": [notification.return_dict() for notification in notifications]
    })
