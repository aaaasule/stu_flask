#!/usr/bin/env python 
# encoding: utf-8
from flask import Blueprint, jsonify

api = Blueprint("api",__name__,url_prefix="/api")


@api.route('/index/')
def test_api():
    return jsonify(msg="Success")