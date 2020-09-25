# -*- encoding: utf-8 -*-
import time
from apscheduler.schedulers.blocking import BlockingScheduler


def my_job():
    print("sss {} ".format(time.ctime()))


sched = BlockingScheduler()
# #  date 固定时间调用   只会执行一次
# sched.add_job(func=my_job, trigger='date', next_run_time="2020-09-25 17:32:59")
# sched.start()
#  interval  每隔5秒执行一次
"""
weeks (int)  –  间隔几周 
days (int)  –  间隔几天 
hours (int)  –  间隔几小时 
minutes (int)  –  间隔几分钟 
seconds (int)  –  间隔多少秒 
start_date (datetime|str)  –  开始日期 
end_date (datetime|str)  –  结束日期 
timezone (datetime.tzinfo|str)  –  时区 
"""

# sched.add_job(func=my_job, trigger='interval', seconds=5)
# sched.start()

# corn  定时调度 (例如在每天的某一个时间点执行任务)

"""
(int|str) 表示参数既可以是int类型，也可以是str类型
(datetime | str) 表示参数既可以是datetime类型，也可以是str类型
year (int|str) – 4-digit year -（表示四位数的年份，如2008年）
month (int|str) – month (1-12) -（表示取值范围为1-12月）
day (int|str) – day of the (1-31) -（表示取值范围为1-31日）
week (int|str) – ISO week (1-53) -（格里历2006年12月31日可以写成2006年-W52-7（扩展形式）或2006W527（紧凑形式））
day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun) - （表示一周中的第几天，既可以用0-6表示也可以用其英语缩写表示）
hour (int|str) – hour (0-23) - （表示取值范围为0-23时）
minute (int|str) – minute (0-59) - （表示取值范围为0-59分）
second (int|str) – second (0-59) - （表示取值范围为0-59秒）
start_date (datetime|str) – earliest possible date/time to trigger on (inclusive) - （表示开始时间）
end_date (datetime|str) – latest possible date/time to trigger on (inclusive) - （表示结束时间）
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone) -（表示时区取值）
其他参数格式用法示例
#表示2017年3月22日17时19分07秒执行该程序
sched.add_job(my_job, 'cron', year=2017,month = 03,day = 22,hour = 17,minute = 19,second = 07)
 
#表示任务在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00 执行该程序
sched.add_job(my_job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
 
#表示从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
sched.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30,end_date='2014-05-30')
 
#表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
sched.add_job(my_job, 'cron',second = '*/5')

"""

sched.add_job(func=my_job, trigger='cron', hour='17', minute='40', second='1')
sched.start()
