# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/9/8 15:53
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from .first_blue import api


def init_views(app):
    app.register_blueprint(blueprint=api)
