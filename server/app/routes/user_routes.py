from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Sector
from sqlalchemy.exc import IntegrityError
from app.services.admin import create_admin
from app.forms.user_forms import UserSignupForm
from app.forms.user_forms import UserLoginForm
from flask_login import login_user, logout_user, login_required
from utils.mailing_utils import send_confirmation_email, confirm_token
from app import db

user_blue_print = Blueprint("users", __name__)

# signup
@user_blue_print.route("/signup", methods=["GET", "POST"])
def signup():
    form = UserSignupForm()
    
    if request.method == "POST" :
    # and form.validate_on_submit():
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
            # personal_recognition=form.personal_recognition.data,
            is_local=form.is_local.data,
            is_not_local=form.is_not_local.data if not form.is_local.data else None,
            password_hash=hashed_password
        )
        
        try:
            db.session.add(user)
            # if user.role == "admin":
            #     db.session.flush()
            db.session.commit()
            
            # send_confirmation_email(user.email)
            # flash("Check your inbox to confirm your email", "info")

        except IntegrityError:
            db.session.rollback()
            flash("This email or phone already exists.", "danger")
            return redirect(request.referrer or url_for("users.signup"))
        login_user(user)
        flash("You have been registered successfully!", "success")
        if user.role == "admin":
            try:
                create_admin(user.id, sector_name=address["sector"].lower())
                return redirect(url_for("dashboard.admin"))
            except ValueError as err:
                user.role = "citizen"
                flash(err, "danger")
        return redirect(url_for("dashboard.citizen"))
    return render_template("user_auth/signup.html", form=form)

# login
@user_blue_print.route("/login", methods=["GET", "POST"])
def login():
    form = UserLoginForm()
    if request.method == "POST":
    # and form.validate_on_submit():
        identifier = form.identifier.data # can be either phone or email
        password = form.password.data
        user = None

        if "@" in identifier:
            user = User.query.filter_by(email=identifier).first()
        else:
            user = User.query.filter_by(phone=identifier).first()
        
        if user and check_password_hash(user.password_hash, password):
            flash("Logged in successfully.", "success")
            login_user(user)
            
            # return redirect(url_for("dashboard.user"))
            if user.role == "citizen":
                return redirect(url_for("dashboard.citizen"))
            
            elif user.role == "admin":
                # return redirect(url_for("main.home"))
                return redirect(url_for("dashboard.admin"))
            
            # elif user.role == "fines_inforcer":
            #     return redirect(url_for("dashboard.fines_inforcer"))
            
            # elif user.role == "attendance_person":
            #     return redirect(url_for("dashboard.attendance_person"))
            
            else:
                return redirect(url_for("main.home"))

        else:
            flash("Invalid credentials.", "danger")

    return render_template("user_auth/login.html", form=form)

# logout
# @user_blue_print.route("/logout", methods=["POST"])
@user_blue_print.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully.", "info")
    return redirect(url_for("users.login"))

# confirmation <- to be done later
@user_blue_print.route("/confirm/<token>")
def confirm_email(token):
    email = confirm_token(token, 3600)
    if not email:
        flash("The confirmation link is invalid or expired.", "danger")
        return redirect(url_for("users.login"))

    user = User.query.filter_by(email=email).first_or_404()
    if user.is_verified:
        flash("Account already confirmed. Please log in.", "info")
    else:
        user.is_verified = True
        db.session.commit()
        flash("Your account has been verified!", "success")

    return redirect(url_for("users.login"))
