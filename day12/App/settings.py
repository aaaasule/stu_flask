# -*- encoding: utf-8 -*-

class Config():
    DEBUG = True
    SECRET_KEY = "n9ceqv38)#&mwuat@(mjb_p%em$e8$qyr#fw9ot!=ba6lijx-6"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/day12"


class DevelopConfig(Config):
    pass


class TestConfig(Config):
    pass


class ProductConfig(Config):
    DEBUG = False


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig
}
