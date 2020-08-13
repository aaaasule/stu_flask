# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/8/12 16:26
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Flask

from App.ext import init_ext
# from App.models import init_model
from App.settings import envs
from App.views import init_views


def create_app(env):
    app = Flask(__name__)
    # 数据库+驱动://用户名:密码@主机:端口/具体库名
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/test"
    app.config.from_object(envs.get(env))
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    init_views(app)  # 初始化views
    # init_model(app)
    init_ext(app)
    return app
