# -*- encoding: utf-8 -*-
"""
@File    : first_blue.py
@Time    : 2020/9/8 15:54
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint, render_template, jsonify
from App import models
from App.models import User

api = Blueprint("api", __name__, url_prefix="/api")


@api.route('/index/')
def index():
    print("hhhh")
    result = {"name": "leo", "age": 14, "height": 181}

    return render_template("index.html", context=result)


@api.route('/add_user')
def add_user():
    u = User()
    u.u_name = "lionel"
    u.u_age = 14
    u.u_sex = True
    u.save()

    return jsonify(msg="Success"), 200


@api.route('/get_data')
def get_data():
    u = User()
    data = u.query.get_all()
    print(data)
    return jsonify(msg="Success")
