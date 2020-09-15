# -*- encoding: utf-8 -*-
from App.ext import db


class ModelBase:
    def save(self):
        db.session.add(self)
        db.session.commit()


class Animals(db.Model, ModelBase):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    a_name = db.Column(db.String(16), unique=True)
    a_breed = db.Column(db.String(16))
    a_color = db.Column(db.String(16))


class Cats(Animals):
    c_eat = db.Column(db.String(16))


class Dogs(Animals):
    d_legs = db.Column(db.String(16))
