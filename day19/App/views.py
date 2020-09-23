# -*- encoding: utf-8 -*-
import random

from flask import Blueprint, render_template, request
from App import models
from App.ext import cache
from App.models import Category, Post, Person, Address, News


def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint('blue', __name__, template_folder='../templates')


@blue.route("/index/")
def index():
    return "index success"


@blue.route("/add_category/")
def add_category():
    py = Category("Python")
    p = Post("hello python!", "python is pretty cool ", py)
    py.save()
    p.save()

    return "add category success"


@blue.route("/add_person/")
def add_person():
    p = Person()
    p.name = "姬野%s" % random.randrange(1000)
    p.save()

    return "add person success"


@blue.route("/add_address/")
def add_address():
    a = Address()
    a.email = "xxx@bjdv.com"
    a.person_id = Person.query.order_by(Person.id.desc()).first().id
    a.save()

    return "add address success"


@blue.route("/print_repr/")
def print_repr():
    c = Category("java")
    print(c)
    print(type(c))
    return "print __repr__ : {} success".format(c)


@blue.route("/get_person/")
@cache.cached(timeout=30)
def get_person():
    page = request.args.get('page', 5, int)
    per_page = request.args.get('per_page', 5, int)
    persons = Person.query.limit(per_page).offset((page - 1) * per_page)  # limit 限制每一页多少个  offset 跳过前多少个
    print(persons)
    print(type(persons))
    print("需要查询数据库！")
    pagination = Person.query.paginate(page=page, per_page=per_page)

    return render_template("Persons.html", pagination=pagination, persons=persons, per_page=per_page)


@blue.route("/add_news/")
def add_news():
    new = News()
    new.n_title = "s10快要开始了,%s" % random.randrange(1000)
    new.n_content = "希望那谁谁%s夺冠！" % random.randrange(1000)
    new.save()

    return "add news success"


@blue.route("/get_news/")
def get_news():
    news = News.query.all()
    print(news)
    print(type(news[0]))
    return render_template('News.html', news=news)
