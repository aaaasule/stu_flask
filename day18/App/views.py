# -*- encoding: utf-8 -*-
import random

from flask import Blueprint
from App import models
from App.models import *


def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint('blue', __name__, template_folder="../templates")


@blue.route("/index/")
def index():
    return "success"


@blue.route("/add_customer/")
def add_customer():
    c = Customer()
    c.c_name = "消费者%s" % random.randrange(1000)
    c.c_age = 14
    c.save()
    return "add customer success"


@blue.route("/add_address/")
def add_address():
    a = Address()
    a.a_local = "蓝天%s" % random.randrange(1000)
    a.customer_id = Customer.query.order_by(Customer.id.desc()).first().id

    a.save()

    return "add address success"


@blue.route("/get_customer/")
def get_customer():
    address = Customer.query.order_by(Customer.id.desc()).first().id
    return "get address:%s success" % address
