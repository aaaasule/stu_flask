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
    u_name = db.Column(db.String(16))
    u_email = db.Column(db.String(32))
    addresses = db.relationship('Address', backref='user', lazy='dynamic')


class Address(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Students(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16))
    s_age = db.Column(db.Integer)
    schools = db.relationship('School', backref='students', lazy='dynamic')


class School(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    position = db.Column(db.String(64))

    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
