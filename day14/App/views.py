# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template
from App import models
from App.models import Cats


def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint("blue", __name__)


@blue.route('/index/')
def index():
    return "success"


@blue.route("/add_cat/")
def add_cat():
    cat = Cats()
    cat.a_name = "小央"
    cat.a_breed = "𠆤"
    cat.a_color = "hei色"
    cat.c_eat = "bone"

    cat.save()

    return "add cat success"


@blue.route("/get_cats/")
def get_cats():
    # cats = Cats.query.filter(Cats.id.__eq__(2))
    cats = Cats.query.filter(Cats.a_name.contains("黑"))
    print(cats)
    print(type(cats))  # <class 'flask_sqlalchemy.BaseQuery'>

    return render_template("Cats.html", cats=cats)


