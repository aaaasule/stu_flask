# -*- encoding: utf-8 -*-
"""
@File    : ext.py
@Time    : 2020/8/12 16:43
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask_migrate import Migrate

migrate = Migrate()


def init_ext(app):
    migrate.init_app(app)
