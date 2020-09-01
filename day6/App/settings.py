#!/usr/bin/env python 
# encoding: utf-8
import os


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:lionel123@localhost:3306/flask_day6"
    # SQLALCHEMY_DATABASE_URI = os.getenv("")


class TestConfig(Config):
    pass


class ProductConfig(Config):
    DEBUG = False


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig
}
