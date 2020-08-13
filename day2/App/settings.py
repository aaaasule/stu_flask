# -*- encoding: utf-8 -*-
"""
@File    : settings.py
@Time    : 2020/8/12 16:43
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_info(db_info):
    engine = db_info.get("ENGINE") or "sqlite"
    driver = db_info.get("DRIVER")
    user = db_info.get("USER")
    password = db_info.get("PASSWORD")
    host = db_info.get("HOST")
    port = db_info.get("PORT")
    name = db_info.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config():
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = False


class DevelopConfig(Config):
    DEBUG = True
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "test"
    }
    SQLALCHEMY_DATABASE_URI = get_db_info(db_info)


class TestConfig(Config):
    DEBUG = True
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "test"
    }
    SQLALCHEMY_DATABASE_URI = get_db_info(db_info)


class ProductConfig(Config):
    DEBUG = True
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "test"
    }
    SQLALCHEMY_DATABASE_URI = get_db_info(db_info)


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig

}
