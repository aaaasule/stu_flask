# -*- encoding: utf-8 -*-
"""
@File    : models.py
@Time    : 2020/8/21 11:02
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from App.ext import models


class ModelBase(object):
    def save(self):
        models.session.add(self)
        models.session.commit()


class User(ModelBase, models.Model):
    id = models.Column(models.Integer, primary_key=True)
    user_name = models.Column(models.String(16))


class Student(ModelBase, models.Model):
    id = models.Column(models.Integer, primary_key=True)
    s_name = models.Column(models.String(16))
    s_num = models.Column(models.Integer)
