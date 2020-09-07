# -*- encoding: utf-8 -*-
"""
@File    : first_api.py
@Time    : 2020/9/7 16:13
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint, jsonify

from App.models import PreviewData

api = Blueprint("api", __name__)


@api.route("/index/")
def index():
    print("Success!")
    return jsonify(msg="Success")


@api.route("/add/")
def add_data():
    p = PreviewData()
    p.tenant_id = 16
    p.robot_id = 14
    p.save()

    return jsonify(msg="Success")
