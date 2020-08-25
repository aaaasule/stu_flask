# -*- encoding: utf-8 -*-
"""
@File    : models.py
@Time    : 2020/8/25 16:07
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from App.ext import db


class ModelBase(object):

    def save(self):
        db.session.add(self)
        db.session.commit()


class Users(ModelBase, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_name = db.Column(db.String(16))
