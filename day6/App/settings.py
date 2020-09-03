<<<<<<< HEAD
# -*- encoding: utf-8 -*-
"""
@File    : settings.py
@Time    : 2020/8/26 9:40
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
=======
#!/usr/bin/env python 
# encoding: utf-8
import os
>>>>>>> master


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/day6"


class DevelopConfig(Config):
=======


class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:lionel123@localhost:3306/flask_day6"
    # SQLALCHEMY_DATABASE_URI = os.getenv("")


class TestConfig(Config):
>>>>>>> master
    pass


class ProductConfig(Config):
<<<<<<< HEAD
    pass
=======
    DEBUG = False
>>>>>>> master


envs = {
    "develop": DevelopConfig,
<<<<<<< HEAD
=======
    "test": TestConfig,
>>>>>>> master
    "product": ProductConfig
}
