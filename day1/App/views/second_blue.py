# -*- encoding: utf-8 -*-
"""
@File    : second_blue.py
@Time    : 2020/8/12 17:16
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint

second = Blueprint('second_blue', __name__)


@second.route("/hello/")
def hello():
    return "second blue!"
