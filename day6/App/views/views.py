#!/usr/bin/env python 
# encoding: utf-8
from flask import Blueprint, jsonify

from App.ext import db
from App.models import User

blue = Blueprint("blue", __name__, url_prefix="/api")


@blue.route('/index/')
def index():
    return jsonify(msg="Success")


@blue.route("/create_all/")
def create_all():
    db.create_all()
    return jsonify(msg="创建成功！")


@blue.route('/add_user')
def add_user():
    u = User()
    u.u_name = "lionel"
    u.u_age = 14
    u.save()

    return jsonify(msg="添加成功！")
