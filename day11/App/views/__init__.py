# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/9/9 13:58
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from .first_blue import api
from App import models


def init_views(app):
    app.register_blueprint(blueprint=api)
