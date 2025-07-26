# purpose:
    # generate user token if creaditials are valid
    # and then help sending the appropriate user object for the front_end

from flask import Blueprint, request, jsonify, flash, url_for, render_template, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.forms.user_forms import UserSignupForm
from app.models import User
from app import db

auth_blue_print = Blueprint("auth", __name__)

@auth_blue_print.route("/signup", methods=["GET", "POST"])
def signup():
    form = UserSignupForm()
    if form.validate_on_submit():
        address = {
            "province": form.province.data,
            "district": form.district.data,
            "sector": form.sector.data,
            "cell": form.cell.data,
            "village": form.village.data,
            "isibo": form.isibo.data
        }
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            first_name=form.first_name.data,
            middle_name=form.middle_name.data,
            last_name=form.last_name.data,
            gender=form.gender.data,
            email=form.email.data,
            phone=form.phone.data,
            address=address,
            role=form.role.data,
            personal_recognition=form.personal_recognition.data,
            is_local=form.is_local.data,
            is_not_local=form.is_not_local.data if not form.is_local.data else None,
            password_hash=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("User registered successfully!", "success")
        return redirect(url_for("auth_blue_print.signup"))  # Or login page
    return render_template("auth/signup.html", form=form)


@auth_blue_print.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(phone=data.get("user_phone_number")).first() or User.query.filter_by(email=data.get("user_email_address")).first()

    if not user or not check_password_hash(user.password, data.get("user_password")):
        return jsonify({
            "msg": "Invalid credentials"
        }), 401

    token = create_access_token(identity=user.id)
    return jsonify({
        "access_token": token,
        "user": user.return_dict()
    })


@auth_blue_print.route("/profile")
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user:
        return jsonify(user.return_dict())
    return jsonify({
        "msg": "User not found"
    }), 404
