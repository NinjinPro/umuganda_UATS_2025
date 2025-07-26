from flask import Blueprint, render_template

home_blue_print = Blueprint("main", __name__)
app_blue_print = Blueprint("app", __name__)

@home_blue_print.route("/")
@home_blue_print.route("/home")
def home():
    return render_template("home.html")

@app_blue_print.route("/about")
def about():
    return render_template("app/about.html")

@app_blue_print.route("/help")
def help():
    return render_template("app/help.html")

@app_blue_print.route("/contact")
def contact():
    return render_template("app/contact.html")

@app_blue_print.route("/terms")
def terms():
    return render_template("app/terms.html")