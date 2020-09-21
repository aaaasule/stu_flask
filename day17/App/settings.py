# -*- encoding: utf-8 -*-


class Config(object):
    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/day17"


class TestConfig(Config):
    pass


class ProductConfig(Config):
    pass


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig
}
