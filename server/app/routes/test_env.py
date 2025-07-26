from flask import Blueprint, jsonify
import os

env_variables_blue_print = Blueprint("env_variables", __name__)

@env_variables_blue_print.route("/check_environment_variables")
def env_check():
    return jsonify({
        "SECRET_KEY": os.getenv("SECRET_KEY"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "JWT_SECRET_KEY": os.getenv("JWT_SECRET_KEY")
    })
