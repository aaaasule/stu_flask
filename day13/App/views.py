# -*- encoding: utf-8 -*-
from flask import Blueprint, jsonify, render_template
from App import models
from App.models import Animal, Cat, Dog


def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint('blue', __name__)


@blue.route('/index/')
def index():
    return jsonify({"code": 0, "data": {"name": "leo", "age": 14}})


@blue.route('/add_animal/')
def add_animal():
    a = Animal()
    a.a_name = "小土狗"
    a.save()
    return "add animal success"


@blue.route('/add_cat/')
def add_cat():
    cat = Cat()
    cat.a_name = "小奶猫"
    cat.c_legs = 16
    cat.save()
    return "add cat success"


@blue.route('/add_dog/')
def add_dog():
    d = Dog()
    d.a_name = "大黑狗"
    d.d_eat = "buff"
    d.save()
    return "add dog success"


@blue.route('/get_cats/')
def get_cats():
    # cat = Cat()
    # cats = Cat.query.filter(Cat.id.__eq__(2)).all()  # __eq__ 等于  __lt__  小於 __le__ 小於等於

    """
    類名.屬性名.魔術方法
    類名.屬性名 數學運算符

    :return:
    """
    # cats = Cat.query.filter(Cat.id == 2)

    cats = Cat.query.filter(Cat.a_name.contains("黑"))   # 屬性  a_name  中包含   黑  的  一條數據
    print("cats:{}".format(cats))
    print(type(cats))

    return render_template("Cats.html", cats=cats)
