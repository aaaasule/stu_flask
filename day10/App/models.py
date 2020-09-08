# -*- encoding: utf-8 -*-
"""
@File    : models.py
@Time    : 2020/9/8 16:21
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
    __tablename = 'user'
    id = db.Column(db.Integer, primary_key=True)
    u_name = db.Column(db.String(16), unique=True)
    u_age = db.Column(db.Integer)
    u_sex = db.Column(db.Boolean)
    #  一对多
    books = db.relationship('book')


class Book(ModelBase, db.Model):
    __tablename = 'book'
    id = db.Column(db.Integer, primary_key=True)
    b_name = db.Column(db.String(16))
    #  多的一方的book表是通过外检关联到user表的
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Test(ModelBase, db.Model):
    __tablename = 'test'
    id = db.Column(db.Integer, primary_key=True)
    t = db.Column(db.String(16))
