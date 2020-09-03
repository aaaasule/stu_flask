# -*- encoding: utf-8 -*-
"""
@File    : settings.py
@Time    : 2020/9/3 10:17
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""


class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/flask_day8?charset=utf8"


class TestConfig(Config):
    pass


class ProductConfig(Config):
    DEBUG = False


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig
}
