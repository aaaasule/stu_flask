# -*- encoding: utf-8 -*-
"""
@File    : first_blue.py
@Time    : 2020/8/12 17:13
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""

from flask import Blueprint, render_template

blue = Blueprint("blue", __name__)


@blue.route("/")
def index():
    return render_template('hello.html', msg="下班就要下暴雨了！")
