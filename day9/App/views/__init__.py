# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/9/7 16:12
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from .first_api import api
from App import models
from .task import task


def init_views(app):
    app.register_blueprint(blueprint=api)
    app.register_blueprint(blueprint=task)
