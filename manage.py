# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 0021 9:10
# @Author  : Zhang
# @File    : manage.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "我的第一个Flask项目"


if __name__ == "__main__":
    app.run()