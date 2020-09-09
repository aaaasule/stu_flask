# -*- encoding: utf-8 -*-
"""
@File    : settings.py
@Time    : 2020/9/9 13:48
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""


class Config:
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "n9ceqv38)#&mwuat@(mjb_p%em$e8$qyr#fw9ot!=ba6lijx-6"

    SESSION_TYPE = 'redis'

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@172.17.0.2:3306/day11"


class DevelopConfig(Config):
    pass


class TestConfig(Config):
    pass


class ProductConfig(Config):
    DEBUG = False


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig,
}
