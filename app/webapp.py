from flask import Blueprint, render_template

server_bp = Blueprint("main", __name__)


@server_bp.route("/")
def root():
    return render_template("index.html")


@server_bp.route("/about")
def about():
    return render_template("about.html")


@server_bp.route("/contact")
def contact():
    return render_template("contact.html")


@server_bp.route("/practicing-area")
def practicingarea():
    return render_template("practicing-area.html")


@server_bp.route("/services")
def services():
    return render_template("services.html")


@server_bp.route("/doctors")
def doctors():
    return render_template("doctors.html")
