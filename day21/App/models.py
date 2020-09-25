# -*- encoding: utf-8 -*-
from App.ext import db


class ModelBase(object):

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.update(self)
        db.session.commit()


class User(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16))
    addresses = db.relationship('Address', backref='user', lazy='dynamic')  # 可以使用   address.user


class Address(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
