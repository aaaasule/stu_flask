# -*- encoding: utf-8 -*-
"""
@File    : first_blue.py
@Time    : 2020/9/9 13:59
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
from flask import Blueprint, render_template, request, Response, session

api = Blueprint("api", __name__, url_prefix="/api")


@api.route('/index/')
def index():
    print("first blue")
    re_result = {"name": "lionel"}
    return render_template("index.html", context=re_result)


@api.route('/login/', methods=['GET', 'POST'])
def login():
    print("request-method:{}".format(request.method))
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        print("request.form", request.form)
        form = request.form
        username = form.get("username")
        response = Response("登录成功！{}".format(username))
        # response.set_cookie("username", username)
        session['username'] = username
        session['password'] = "lionel"
        return response


@api.route('/mine/', methods=['GET', 'POST'])
def mine():
    # username = request.cookies.get("username")
    username = session.get('username')
    return "welcome back！{}".format(username)
