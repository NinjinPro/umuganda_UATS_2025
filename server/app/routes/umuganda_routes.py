from flask import Blueprint, request, jsonify, redirect, abort, flash
from flask_jwt_extended import jwt_required
from flask_login import login_required, current_user
from app.models import Umuganda
from datetime import datetime
from functools import wraps
from app import db

def role_required(role_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            if current_user.role != role_name:
                abort(403)
            return view_func(*args, **kwargs)
        return wrapper
    return decorator

umuganda_blue_print = Blueprint("umugandas", __name__)

# get-all
@umuganda_blue_print.route("/")
@jwt_required()
@login_required
def get_umugandas():
    imiganda = Umuganda.query.all()
    return jsonify([u.return_dict() for u in imiganda]), 200

# get-one
@umuganda_blue_print.route("/<int:id>")
# @jwt_required()
@login_required
def get_umuganda(id):
    umuganda = Umuganda.query.get_or_404(id)
    return jsonify(umuganda.return_dict()), 200

# create
@umuganda_blue_print.route("/", methods=["POST"])
# @jwt_required()
@login_required
def create_umuganda():
    data = request.get_json()
    start_time = datetime.strptime(data.get("start_time"), "%Y-%m-%dT%H:%M")
    end_time = datetime.strptime(data.get("end_time"), "%Y-%m-%dT%H:%M")
    new_umuganda = Umuganda(
        title=data.get("title"),
        location=data.get("location") or f'{current_user.address["sector"]} mainhole',
        description=data.get("description"),
        umuganda_date=datetime.strptime(data.get("umuganda_date"), "%Y-%m-%d"),
        # umuganda_date=datetime.strptime(data.get("umuganda_date")),
        created_by=current_user.id,
        start_time=start_time,
        end_time=end_time
    )
    try:
        db.session.add(new_umuganda)
        db.session.commit()
        return jsonify({
            "status": "success"
            # "data": new_umuganda.return_dict()
        })
    except Exception as e:
        db.session.rollback()
        msg = None
        if "unique constraint failed" in str(e.orig).lower():
            msg = "This type of umuganda already exist"

        elif "not null constraint failed" in str(e.orig).lower():
            msg = "Their is a missing required field"

        # elif "unique constraint failed" in str(e.orig).lower():
        #     msg = "This type of umuganda already exist"

        # elif "unique constraint failed" in str(e.orig).lower():
        #     msg = "This type of umuganda already exist"

        return jsonify({
            "status": "failed",
            "msg": msg
        })

# update
@umuganda_blue_print.route("/<int:id>", methods=["PUT"])
# @jwt_required()
@login_required
def update_umuganda(id):
    umuganda = Umuganda.query.get_or_404(id)
    data = request.get_json()

    umuganda.title = data.get("title", umuganda.title)
    umuganda.location = data.get("location", umuganda.location)
    if data.get("scheduled_for"):
        umuganda.scheduled_for = datetime.strptime(data.get("scheduled_for"), "%Y-%m-%d %H:%M")

    db.session.commit()
    return jsonify(umuganda.return_dict()), 200

# delete
@umuganda_blue_print.route("/<int:id>", methods=["DELETE"])
# @jwt_required()
@login_required
def delete_umuganda(id):
    umuganda = Umuganda.query.get_or_404(id)
    try:
        db.session.delete(umuganda)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({
            "status" : "failed"
        })
    return jsonify({"msg": "Umuganda session was deleted successfully"}), 200