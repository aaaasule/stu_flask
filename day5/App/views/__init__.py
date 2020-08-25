# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/8/25 16:07
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from .first_blue import first_blue


def init_views(app):
    app.register_blueprint(blueprint=first_blue)
