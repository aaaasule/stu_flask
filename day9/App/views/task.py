# -*- encoding: utf-8 -*-
"""
@File    : task.py
@Time    : 2020/9/7 16:44
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
import datetime

from flask import Blueprint, current_app, jsonify

from App.logger import logger

task = Blueprint("task", __name__, url_prefix="/task")


def job01():
    otherStyleTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info("func job01 在 {} 执行一次！".format(otherStyleTime))


@task.route("/add/")
def add_jobs():
    current_app.apscheduler.add_job(id="task1", func=job01, trigger='cron', day_of_week="*", hour=17,
                                    minute=9, second=59)

    return jsonify(msg="func jon01 start success")
