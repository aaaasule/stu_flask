# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/8/26 9:33
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
    #  config
    app.config.from_object(envs.get(env))

    # ext
    init_ext(app)
    # views
    init_view(app)

    return app
