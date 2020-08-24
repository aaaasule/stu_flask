from .first_blue import blue
from .second import api


def init_views(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=api)
