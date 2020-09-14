# -*- encoding: utf-8 -*-


class Config(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@172.17.0.2:3306/day13"


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = ""


class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = ""


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig
}
