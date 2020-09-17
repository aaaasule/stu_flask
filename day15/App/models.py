# -*- encoding: utf-8 -*-
from App.ext import db


class ModelBase(object):

    def save(self):
        db.session.add(self)
        db.session.commit()


class Animals(ModelBase, db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_name = db.Column(db.String(16), unique=True)
    a_color = db.Column(db.String(16))
    a_weight = db.Column(db.Integer)


class Dogs(Animals):
    d_eat = db.Column(db.String(16))


class Cats(Animals):
    c_eat = db.Column(db.String(16))
