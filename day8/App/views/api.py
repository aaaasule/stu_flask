# -*- encoding: utf-8 -*-
"""
@File    : api.py
@Time    : 2020/9/3 10:25
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint, jsonify, render_template, make_response, Response, abort
from App import models
from App.ext import db

from App.models import User

api = Blueprint("api", __name__)


@api.route('/index')
def index():
    context = {"name": "lionel", "age": 14}
    return render_template("index.html", context=context)


@api.route("/create_all/")
def create_all():
    db.create_all()

    return jsonify(msg="Success")


@api.route('/add_user/<int:age>/<name>/')
def add_user(age, name):
    u = User()
    u.u_name = name
    u.u_age = age
    u.save()

    return jsonify(msg="Success")


@api.route('/make_response')
def make_re():
    # result = make_response("<h1>hello!<h1>")  # 参数:data  code
    # print(result)
    # print(type(result))  # <class 'flask.wrappers.Response'>
    abort(404)  # 主动终止
    # abort(Response("bye bye !"))
    result = Response("自己动！")
    return result


@api.errorhandler(404)
def handle_error(error):
    print(error)
    return "what error"
