# -*- encoding: utf-8 -*-

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    DebugToolbarExtension(app=app)
