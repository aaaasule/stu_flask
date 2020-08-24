from flask import jsonify
from flask import Blueprint
from App import models
from App.ext import db
from App.models import User


blue = Blueprint("blue", __name__)


@blue.route("/index/")
def index():
    msg = "123454"

    print(msg)
    return jsonify(msg="Success")


@blue.route("/create_all/")
def create_all():
    db.create_all()

    return jsonify(msg="Success")

@blue.route("/addUser/")
def add_user():
    user = User()
    user.u_name = "lionel"
    user.save()
    return jsonify(msg="add user Success!")
