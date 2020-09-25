# -*- encoding: utf-8 -*-
import random

from flask import Blueprint, request
from App import models
from App.models import *


def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint('blue', __name__, template_folder="../templates")


@blue.route("/index/")
def index():
    return "Success"


@blue.route("/add_user/")
def add_user():
    user = User()
    user.u_name = "leo%s" % random.randrange(1000)

    user.save()

    return "add user success"


@blue.route("/add_address/")
def add_address():
    address = Address()
    address.email = "x %s xxx@bjdv.com" % random.randrange(1000)
    address.user_id = User.query.order_by(User.id.desc()).first().id

    address.save()
    return "add address success"


@blue.route("/get_user/")
def get_user():
    address_id = request.args.get("a_id")
    address = Address.query.filter(Address.id == address_id).first()
    print("address_id", address_id)
    print("address", address.user.u_name)
    return "get user success"
