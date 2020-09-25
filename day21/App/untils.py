# -*- encoding: utf-8 -*-
import time
from apscheduler.schedulers.blocking import BlockingScheduler


def my_job():
    print("sss {} ".format(time.ctime()))


sched = BlockingScheduler()
sched.add_job(func=my_job, trigger='cron', hour='17', minute='40', second='1')
sched.start()
