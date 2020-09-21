# -*- encoding: utf-8 -*-
from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_views


def create_app(env):
    app = Flask(__name__, static_folder="../static")
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_views(app)

    return app
