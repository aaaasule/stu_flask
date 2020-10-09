# -*- encoding: utf-8 -*-
from werkzeug.security import check_password_hash, generate_password_hash

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


class Student(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True)
    s_name = db.Column(db.String(16), unique=True)
    _s_password = db.Column(db.String(256))
    s_phone = db.Column(db.String(32))

    @property
    def s_password(self):
        raise Exception("Error Action")

    @s_password.setter
    def s_password(self, value):
        self._s_password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self._s_password, password)
