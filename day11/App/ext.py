# -*- encoding: utf-8 -*-
"""
@File    : ext.py
@Time    : 2020/9/9 13:57
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
# from flask_celery import Celery
from flask_migrate import Migrate
# from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
# sess = Session()
# celery = Celery()


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    # sess.init_app(app=app)
    # celery.init_app(app=app)
