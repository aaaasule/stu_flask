# -*- encoding: utf-8 -*-
from App.ext import db


class ModelBase(object):

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.update(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(32))


class Address(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(128))
    u_id = db.Column(db.Integer, db.ForeignKey("user.id"))
