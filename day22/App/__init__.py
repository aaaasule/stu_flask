# -*- encoding: utf-8 -*-
from flask import Flask

from App.ext import init_ext, scheduler
from App.settings import envs
from App.views import init_views
from datetime import datetime


def print_time():
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("time:{}".format(time_now))


def create_app(env):
    app = Flask(__name__, static_folder="../static")
    app.config.from_object(envs.get(env))

    init_ext(app)

    init_views(app)
    scheduler.remove_job(id='job01')
    scheduler.add_job(id="job01", func=print_time, trigger='cron', day_of_week="*", hour=14,
                      minute=18, second=59)
    scheduler.start()
    return app
