# -*- encoding: utf-8 -*-
"""
@File    : views.py
@Time    : 2020/8/12 16:44
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""

# def init_route(app):
#     @app.route("/")
#     def index():
#         return "我的第一个Flask项目的主页"

from .first_blue import blue
from .second_blue import second
from .third import third


def init_views(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=second)
    app.register_blueprint(blueprint=third)
