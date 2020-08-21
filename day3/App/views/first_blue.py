# -*- encoding: utf-8 -*-
"""
@File    : first_blue.py
@Time    : 2020/8/21 10:54
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint
from App import models
from App.models import User

blue = Blueprint("blue", __name__, url_prefix="/blue")


@blue.route("/first_blue/")
def first_blue():
    return "first_blue"


@blue.route("/addUser/")
def add_user():
    user = User()
    user.user_name = "leo"
    user.save()
    return "添加成功！"
