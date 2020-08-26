# -*- encoding: utf-8 -*-
"""
@File    : api.py
@Time    : 2020/8/26 9:36
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint, jsonify
from App import models

api = Blueprint("blue", __name__, url_prefix="/api")


@api.route('/index')
def index():
    return jsonify(msg="Success")
