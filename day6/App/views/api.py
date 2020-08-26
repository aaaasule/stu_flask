# -*- encoding: utf-8 -*-
"""
@File    : api.py
@Time    : 2020/8/26 9:36
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint, jsonify, request
from App import models

api = Blueprint("blue", __name__, url_prefix="/api/")


@api.route('/index/')
def index():
    return jsonify(msg="Success")


@api.route("/send/")
def send():
    print(request.args)  # args 获取get请求参数  ImmutableMultiDict([('user', 'lionel'), ('age', '14')])
    print(type(request.args))  # <class 'werkzeug.datastructures.ImmutableMultiDict'>

    print(request.form)  # form 接受post请求
    print(type(request.form))
    return jsonify(msg="Success!")
