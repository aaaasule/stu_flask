# -*- encoding: utf-8 -*-
from flask import Blueprint, request, render_template
from App import models
from App.models import *


def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint("blue", __name__, template_folder="../templates")


@blue.route("/index/", methods=["POST", "GET"])
def index():
    params = {"name": "leo"}

    print(params)

    return render_template("index.html", params=params)


@blue.route("/add_cats/")
def add_cats():
    cat = Cats()
    cat.a_name = "小黑"
    cat.a_color = "black"
    cat.a_weight = 45
    cat.c_eat = "fish"
    cat.save()
    return "add cat success"


@blue.route("/get_cats/")
def get_cats():
    cats = Cats.query.filter(Cats.id == 1).all()
    print(cats)
    print(type(cats))

    return render_template("Cats.html", cats=cats)
