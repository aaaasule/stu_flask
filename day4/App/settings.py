class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:lionel123@localhost:3306/flask_every_day"


class ProductConfig(Config):
    pass


envs = {
    "develop": DevelopConfig,
    "product": ProductConfig
}
