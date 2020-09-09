# -*- encoding: utf-8 -*-
"""
@File    : second_blue.py
@Time    : 2020/9/9 17:47
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint

from App.tasks import add

task = Blueprint("task", __name__, url_prefix="/task")


@task.route('/test')
def test():
    add(10, 9)
    add.apply_async(args=[5, 7], queue='eegqueue')
    return 'success'
