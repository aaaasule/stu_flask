# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/8/21 10:50
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_view


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_view(app=app)

    return app
