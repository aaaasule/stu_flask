<<<<<<< HEAD
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
=======
#!/usr/bin/env python 
# encoding: utf-8
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
>>>>>>> master
migrate = Migrate()


def init_ext(app):
<<<<<<< HEAD
    models.init_app(app)
    migrate.init_app(app, models)
=======
    db.init_app(app)
    migrate.init_app(app=app, db=db)
>>>>>>> master
