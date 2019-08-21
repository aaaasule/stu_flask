# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 0021 9:10
# @Author  : Zhang
# @File    : manage.py

from flask import Flask, url_for, request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "我的第一个Flask项目的主页"

@app.route("/1/")
def first():
    return "项目第一页"

# @app.route("/hello/<name>")
# def say_hello(name):
#     return "{} say hello world!".format(name)


@app.route("/user/<userName>")
def profile(userName):
    return "{}".format(userName)

@app.route("/login/",methods=['POST','GET'])
def login():
    if request.methods == 'POST':
        pass
    else:
        pass

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html',name=name)

with app.test_request_context():
    print(url_for("index"))
    print(url_for("profile",userName="asule"))
    print(url_for("hello",name="ricardo"))
    print(url_for("first"))
if __name__ == "__main__":
    app.run(debug=True)