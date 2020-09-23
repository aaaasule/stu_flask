# -*- encoding: utf-8 -*-
from datetime import datetime

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


class Post(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):  # 自定义输出实例化对象的信息
        return '<Posts %r>' % self.title


class Category(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


# 一对多

class Person(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    address = db.relationship('Address', backref='person', lazy='dynamic')  # 声明关系   backref


class Address(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))


# many to many

#  辅表
tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
                )


class Page(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('pages', lazy='dynamic'))


class Tag(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True)


class News(db.Model, ModelBase):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    n_title = db.Column(db.String(32))
    n_content = db.Column(db.String(256))
