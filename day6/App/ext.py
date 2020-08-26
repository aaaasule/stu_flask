# -*- encoding: utf-8 -*-
"""
@File    : ext.py
@Time    : 2020/8/26 9:43
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

models = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    models.init_app(app)
    migrate.init_app(app, models)
