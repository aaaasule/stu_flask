# -*- encoding: utf-8 -*-
"""
@File    : settings.py
@Time    : 2020/9/7 16:07
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置作业存储器
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url="mysql+pymysql://root:123456@localhost:3306/day9"),
    }
    # 配置执行器 并设置线程数
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 5}
    }

    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,  # 默认情况下关闭新的作业
        'max_instances': 3  # 设置调度程序同事运行的特定作业的最大实例数
    }


class DevelopConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/day9"


class TestConfig(Config):
    DEBUG = False


class ProductConfig(Config):
    DEBUG = False


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig
}
