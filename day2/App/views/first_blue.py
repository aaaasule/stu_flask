# -*- encoding: utf-8 -*-
"""
@File    : first_blue.py
@Time    : 2020/8/12 17:13
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""

from flask import Blueprint, render_template

from App.models import db, User, PreviewData

blue = Blueprint("blue", __name__)


@blue.route("/")
def index():
    return render_template('hello.html', msg="下班就要下暴雨了！")


@blue.route("/createdb/")
def createdb():
    db.create_all()
    return "创建成功！"


@blue.route("/adduser/")
def adduser():
    user = User()
    user.username = "lionel"
    # db.session.add(user)
    # db.session.commit()
    user.save()
    return "添加成功！"


@blue.route("/drop/")
def drop():
    db.drop_all()
    return "删除成功！"

@blue.route("/addpreview/")
def addpreview():
    preview = PreviewData()
    preview.tenant_id = 4
    # db.session.add(user)
    # db.session.commit()
    preview.save()
    return "添加成功！"
