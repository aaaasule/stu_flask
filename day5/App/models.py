# -*- encoding: utf-8 -*-
"""
@File    : models.py
@Time    : 2020/8/25 16:07
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from App.ext import models


class ModelBase(object):

    def save(self):
        models.session.add(self)
        models.session.commit()


class Users(ModelBase, models.Model):
    id = models.Column(models.Integer, primary_key=True)
    u_name = models.Column(models.String(16))
