# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/9/3 10:25
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from .api import api


def init_views(app):
    app.register_blueprint(blueprint=api)
