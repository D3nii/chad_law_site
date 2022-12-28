# import future
import os
import time

from flask import Flask, redirect
from flask import Blueprint
from flask import request
from flask import flash
from app.webapp import server_bp


def create_app():
    app = Flask(__name__)

    register_blueprints(app)

    return app


def register_blueprints(server):
    server.register_blueprint(server_bp)
