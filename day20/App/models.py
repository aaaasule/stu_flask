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


class User(ModelBase, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16), unique=True)
    u_age = db.Column(db.Integer)
    a_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship('Address', backref=db.backref('user', lazy='dynamic'))


class Address(ModelBase, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(128))
