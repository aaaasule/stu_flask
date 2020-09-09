# -*- encoding: utf-8 -*-
"""
@File    : tasks.py
@Time    : 2020/9/9 17:36
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
import time

from App.ext import celery
#
# #  创建celery 对象，设置任务队列使用redis
# app = Celery("tasks", broker='redis://localhost:6379')


# 创建任务
@celery.task()
def add(a, b):
    time.sleep(5)
    n = a + b
    print(n)
    return n

#
# if __name__ == "__main__":
#     # 调用任务
#     add.delay(10, 5)
#     print("程序结束！")
