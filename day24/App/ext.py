# -*- encoding: utf-8 -*-
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def init_ext(app):
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
