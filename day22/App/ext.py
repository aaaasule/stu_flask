# -*- encoding: utf-8 -*-
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

db = SQLAlchemy()
migrate = Migrate()
scheduler = APScheduler()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    scheduler.init_app(app)
