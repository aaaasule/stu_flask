# -*- encoding: utf-8 -*-
"""
@File    : models.py
@Time    : 2020/9/9 14:03
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from App.ext import db


class ModelBase:

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(ModelBase, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_name = db.Column(db.String(16), index=True, unique=True)
    u_age = db.Column(db.Integer)
    u_height = db.Column(db.String(16))


class Book(ModelBase, db.Model):
    id = db.Column(db.Integer, primary_key=True)
