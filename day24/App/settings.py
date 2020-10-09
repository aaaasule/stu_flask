# -*- encoding: utf-8 -*-
def create_url(info):
    engine = info.get("engine")
    driver = info.get("driver")
    user = info.get("user")
    password = info.get("password")
    host = info.get("host")
    port = info.get("port")
    db = info.get("db")
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, db)


class Config(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "adafargraegerhtsrwhyjswjhytjsyjs"


class DevelopConfig(Config):
    info = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": 'root',
        'password': '123456',
        'host': "localhost",
        "port": 3306,
        "db": "day24"

    }
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 25
    MAIL_USERNAME = 'aaaasule123@163.com'
    MAIL_PASSWORD = 'aaaasule123'  # 授权码
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    SQLALCHEMY_DATABASE_URI = create_url(info)


class TestingConfig(Config):
    pass


class ProductConfig(Config):
    pass


envs = {
    "develop": DevelopConfig,
    "test": TestingConfig,
    "product": ProductConfig
}
