# -*- encoding: utf-8 -*-
"""
@File    : ext.py
@Time    : 2020/8/25 16:07
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(db)


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app)
