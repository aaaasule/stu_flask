# -*- encoding: utf-8 -*-

from App.ext import db


class ModelBase:

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def save_all(self):
    #     db.session.add_all(self)
    #     db.session.commit()


class Students(ModelBase, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
