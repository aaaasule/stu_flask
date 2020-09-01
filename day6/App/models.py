#!/usr/bin/env python 
# encoding: utf-8
from App.ext import db


class ModelBase(object):

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(ModelBase, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    u_name = db.Column(db.String(16), unique=True)
    u_age = db.Column(db.Integer)
    # u_sex = db.Column(db.)
