# -*- encoding: utf-8 -*-
from App.ext import db


class ModelBase(object):

    def save(self):
        db.session.add(self)
        db.session.commit()


class Student(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))


class User(db.Model, ModelBase):
    # __tablename__ = "userdoel"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16), unique=True)
    u_des = db.Column(db.String(128), nullable=True)


class Animal(db.Model, ModelBase):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    a_name = db.Column(db.String(16), unique=True)


class Cat(Animal):
    c_legs = db.Column(db.Integer, default=4)


class Dog(Animal):
    d_eat = db.Column(db.String(16), default="骨头")
