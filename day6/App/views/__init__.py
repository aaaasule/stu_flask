#!/usr/bin/env python 
# encoding: utf-8
from .views import blue


def init_views(app):
    app.register_blueprint(blueprint=blue)
