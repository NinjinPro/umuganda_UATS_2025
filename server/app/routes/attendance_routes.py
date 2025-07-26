from flask import Blueprint, request, jsonify
from app import db
from app.models.attendance import Attendance
from app.models.user import User
from app.models.umuganda import Umuganda

attendance_blue_print = Blueprint("attendances", __name__)

# mark attendance of a user
@attendance_blue_print.route("/", methods=["POST"])
def mark_attendance():
    data = request.get_json()
    user_id = data.get("user_id")
    umuganda_id = data.get("umuganda_id")
    status = data.get("status", "present")
    format_used = data.get("format_used", "web_form")

    # Check if user and umuganda exist
    user = User.query.get(user_id)
    umuganda = Umuganda.query.get(umuganda_id)

    if not user or not umuganda:
        return jsonify({"error": "Invalid user_id or umuganda_id"}), 404

    # Prevent double attendance
    existing = Attendance.query.filter_by(user_id=user_id, umuganda_id=umuganda_id).first()
    if existing:
        return jsonify({"message": "Attendance already recorded", "attendance": existing.return_dict()}), 409

    attendance = Attendance(
        user_id=user_id,
        umuganda_id=umuganda_id,
        status=status,
        format_used=format_used,
    )
    db.session.add(attendance)
    db.session.commit()
    return jsonify({"message": "Attendance marked successfully", "attendance": attendance.return_dict()}), 201

# list of user's attendance <- all attendances of a user
@attendance_blue_print.route("/user/<int:user_id>", methods=["GET"])
def get_user_attendance(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    attendance = [a.return_dict() for a in user.attendances]
    return jsonify({"user_id": user_id, "attendance": attendance})

# list of attendance for a umuganda <- attendenca of that umuganda
@attendance_blue_print.route("/<int:umuganda_id>", methods=["GET"])
def get_umuganda_attendance(umuganda_id):
    umuganda = Umuganda.query.get(umuganda_id)
    if not umuganda:
        return jsonify({"error": "Umuganda not found"}), 404

    attendance = [a.return_dict() for a in umuganda.attendances]
    return jsonify({"umuganda_id": umuganda_id, "attendance": attendance})
