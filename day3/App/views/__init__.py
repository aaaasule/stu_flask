# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/8/21 10:54
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from .first_blue import blue


def init_view(app):
    app.register_blueprint(blueprint=blue)
