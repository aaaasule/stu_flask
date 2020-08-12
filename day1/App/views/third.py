# -*- encoding: utf-8 -*-
"""
@File    : third.py
@Time    : 2020/8/12 17:28
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint

third = Blueprint('third', __name__)


@third.route("/hi/")
def hi():
    return "hi world!"
