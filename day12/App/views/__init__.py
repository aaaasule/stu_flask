# -*- encoding: utf-8 -*-

from .first_blue import blue
from App import models


def init_views(app):
    app.register_blueprint(blueprint=blue)
