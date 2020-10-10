# -*- encoding: utf-8 -*-
from App.ext import db


class ModelBase(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.update(self)
        db.session.commit()


class Goods(ModelBase, db.Model):
    d_name = db.Column(db.String(64))
    g_price = db.Column(db.Float, default=0)
