from app.models import User, Umuganda, Fine
from flask import Blueprint, jsonify, render_template

test_home_blue_print = Blueprint("home_blue_print", __name__)

@test_home_blue_print.route("/home")
@test_home_blue_print.route("/")
def home_page():
    return render_template("auth.html")
