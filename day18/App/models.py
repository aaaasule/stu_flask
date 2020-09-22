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


class Customer(ModelBase, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(16))
    c_age = db.Column(db.Integer)
    address = db.relationship('Address', backref='customer', lazy=True)


class Address(ModelBase, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_local = db.Column(db.String(16))

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
