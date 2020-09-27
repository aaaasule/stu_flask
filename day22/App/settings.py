# -*- encoding: utf-8 -*-
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


def make_url(info):
    engine = info.get('engine')
    driver = info.get('driver')
    user = info.get('user')
    password = info.get('password')
    host = info.get('host')
    port = info.get('port')
    db = info.get('db')
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, db)


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    info = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "123456",
        "host": "localhost",
        "port": 3306,
        "db": "day22"
    }

    SQLALCHEMY_DATABASE_URI = make_url(info)

    SCHEDULER_JOBSTORES = {
        "default": SQLAlchemyJobStore(url=make_url(info))
    }


class TestingConfig(Config):
    pass


class ProductConfig(Config):
    pass


envs = {
    "develop": DevelopConfig,
    "test": TestingConfig,
    "product": ProductConfig
}
