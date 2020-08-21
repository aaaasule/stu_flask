# -*- encoding: utf-8 -*-
"""
@File    : settings.py
@Time    : 2020/8/21 11:02
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/test"


envs = {
    "develop": DevelopConfig
}
