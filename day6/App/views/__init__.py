# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/8/26 9:36
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from .api import api


def init_view(app):
    app.register_blueprint(blueprint=api)
