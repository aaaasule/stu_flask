# -*- encoding: utf-8 -*-
"""
@File    : first_blue.py
@Time    : 2020/8/25 16:08
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint, jsonify
from App import models

first_blue = Blueprint("blue", __name__)


@first_blue.route("/blue/")
def blue():
    return jsonify(msg="Success")
