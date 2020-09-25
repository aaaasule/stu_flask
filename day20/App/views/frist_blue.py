# -*- encoding: utf-8 -*-
import random

from flask import Blueprint, render_template

from App.models import User, Address

blue = Blueprint('blue', __name__, template_folder="../../templates")


@blue.route("/index/")
def index():
    return render_template('index.html')


@blue.route("/add_user/")
def add_user():
    u = User()
    u.u_name = "lionel %s " % random.randrange(100)
    u.u_name = 14
    u.a_id = Address.query.order_by(Address.id.desc()).first().id
    u.save()
    return "add user success"


@blue.route("/add_address/")
def add_address():
    a = Address()
    a.address = "长岛%s号" % random.randrange(10000)
    a.save()

    return "add address success"
