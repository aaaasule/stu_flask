# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/8/12 16:26
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Flask

from App.views import init_views


def create_app():
    app = Flask(__name__)
    init_views(app)  # 初始化views

    return app
