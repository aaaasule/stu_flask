<<<<<<< HEAD
# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2020/8/26 9:33
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
=======
#!/usr/bin/env python 
# encoding: utf-8
>>>>>>> master
from flask import Flask

from App.ext import init_ext
from App.settings import envs
<<<<<<< HEAD
from App.views import init_view
=======
from App.views import init_views
>>>>>>> master


def create_app(env):
    app = Flask(__name__)
<<<<<<< HEAD
    #  config
    app.config.from_object(envs.get(env))

    # ext
    init_ext(app)
    # views
    init_view(app)
=======

    app.config.from_object(envs.get(env))
    init_ext(app)
    init_views(app)
>>>>>>> master

    return app
