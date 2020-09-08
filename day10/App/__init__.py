# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/9/8 15:39
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Flask

from App.ext import init_ext
from App.setting import envs
from App.views import init_views


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))

    # 初始化ext
    init_ext(app)
    #  初始化views
    init_views(app)

    return app
