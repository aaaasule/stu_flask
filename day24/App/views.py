# -*- encoding: utf-8 -*-
from flask import Blueprint, render_template, g, request, redirect, url_for, flash
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

from App import models
from App.ext import mail
from App.models import Student


def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint("blue", __name__)


@blue.route("/index/")
def index():
    print("g对象：", g.msg)
    return render_template("index.html")


@blue.route("/student/register/", methods=['GET', "POST"])
def student_register():
    if request.method == "GET":
        return render_template('studentRegister.html')
    elif request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        # hash_pwd = generate_password_hash(password)

        student = Student()
        student.s_name = username
        student.s_password = password
        student.save()

        return "add success"


@blue.route("/student/login/", methods=['GET', "POST"])
def student_login():
    if request.method == "GET":
        return render_template('studentLogin.html')
    elif request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        # hash_pwd = generate_password_hash(password)

        student = Student.query.filter(Student.s_name.__eq__(username)).first()
        if student and student.check_password(password):
            return "login success"
        flash("用户名或密码错误！")
        return redirect(url_for("blue.student_login"))


# 邮件发送
@blue.route("/test_send_mail/")
def send_mail():
    msg = Message("FLASK EMAIL", recipients=['1550112079@qq.com'])
    msg.body = "hello flask-mail!"
    msg.html = "<h2>hello 小天才</h2>"

    mail.send(message=msg)

    return "send message success"


@blue.route("/sendcode/")
def send_code():
    return "send code success"
