# -*- encoding: utf-8 -*-


def make_url(info):
    db_url = "{}+{}://{}:{}@{}:{}/{}".format(info.get('engine'), info.get('driver'), info.get('user'),
                                             info.get('password'), info.get('host'), info.get('port'),
                                             info.get('database'))

    return db_url


class Config(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    TESTING = False

    mysql_info = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "123456",
        "host": "localhost",
        "port": 3306,
        "database": "day15",
    }

    SQLALCHEMY_DATABASE_URI = make_url(mysql_info)


class TestConfig(Config):
    TESTING = True

    # SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format()


class ProductConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format()


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig
}
