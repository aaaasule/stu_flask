# -*- encoding: utf-8 -*-
from flask import Blueprint
from App import models

def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint("blue", __name__, template_folder="../templates")


@blue.route("/index/")
def index():
    return "Success"
