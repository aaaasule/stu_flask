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
        db.session.commot()


class Animal(ModelBase, db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_name = db.Column(db.String(16), unique=True)
    a_height = db.Column(db.String(16))
    a_weight = db.Column(db.String(16))
    a_color = db.Column(db.String(16))
    a_detail = db.Column(db.Text)


class Cats(Animal):
    c_eat = db.Column(db.String(16))


class Dogs(Animal):
    d_eat = db.Column(db.String(16))


class Customer(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(16), unique=True)


class Address(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_address = db.Column(db.String(128))
    c_customer_id = db.Column(db.Integer, db.ForeignKey(Customer.id))
