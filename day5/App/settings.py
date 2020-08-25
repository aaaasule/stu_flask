# -*- encoding: utf-8 -*-
"""
@File    : settings.py
@Time    : 2020/8/25 16:07
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:lionel123@localhost:3306/test"


class ProductConfig(Config):
    pass


envs = {
    "develop": DevelopConfig,
    "product": ProductConfig
}
