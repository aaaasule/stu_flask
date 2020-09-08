# -*- encoding: utf-8 -*-
"""
@File    : setting.py
@Time    : 2020/9/8 15:45
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/day10"


class TestConfig(Config):
    pass


class ProductConfig(Config):
    pass


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig
}
