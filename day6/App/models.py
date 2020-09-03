<<<<<<< HEAD
# -*- encoding: utf-8 -*-
"""
@File    : models.py
@Time    : 2020/8/26 9:45
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from App.ext import models
=======
#!/usr/bin/env python 
# encoding: utf-8
from App.ext import db
>>>>>>> master


class ModelBase(object):

    def save(self):
<<<<<<< HEAD
        models.session.add(self)
        models.session.commit()


class User(ModelBase, models.Model):
    id = models.Column(models.Integer, primary_key=True)
    u_name = models.Column(models.String(16), unique=True)
=======
        db.session.add(self)
        db.session.commit()


class User(ModelBase, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    u_name = db.Column(db.String(16), unique=True)
    u_age = db.Column(db.Integer)
    # u_sex = db.Column(db.)
>>>>>>> master
