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
    TESING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 5 # 数据库连接池大小，默认是数据库引擎的默认值
    SQLALCHEMY_POOL_TIMEOUT = 10  # 指定数据库连接池的超时时间，默认是10
    # SQLALCHEMY_POOL_RECYCLE = 10  # 自动回收连接的秒数

class DevelopConfig(Config):
    DEBUG = True
    info = {
        "engine": 'mysql',
        "driver": "pymysql",
        "user": "root",
        "password": "123456",
        "host": "localhost",
        "port": 3306,
        "db": "day21",
    }
    SQLALCHEMY_DATABASE_URI = create_url(info)




class TestConfig(Config):
    pass


class ProductConfig(Config):
    pass


envs = {
    'develop': DevelopConfig,
    'test': TestConfig,
    'product': ProductConfig
}
