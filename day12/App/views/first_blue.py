# -*- encoding: utf-8 -*-
from flask import Blueprint, Response, jsonify, render_template

from App.ext import db
from App.models import Students

blue = Blueprint("blue", __name__, template_folder='.')


@blue.route('/index/')
def index():
    print("success")
    response = Response({"name": "lionel"})
    return response


@blue.route('/add_student/<name>/')
def add_student(name):
    student = Students()
    student.name = name
    student.save()

    return jsonify(msg="add student {} Success".format(name))


@blue.route('/add_students/')
def add_students():
    students = []
    for i in range(5):
        student = Students()
        student.name = "leo{}".format(i)
        students.append(student)
    db.session.add_all(students)
    db.session.commit()

    return jsonify(msg=" add students success")


@blue.route('/get_student/')
def get_student():
    # student = Students.query.first()
    # print(student)
    # student = Students.query.get_or_404(1)  # 主键id
    student = Students.query.get(1)  # 主键id

    return jsonify(msg='get student {} success'.format(student.name))


@blue.route('/get_students/')
def get_students():
    students = Students.query.all()  # 获取所有

    return render_template("students.html", students=students)


@blue.route('/delete/')
def delete():
    s = Students.query.get(3)
    print(s.name)
    db.session.delete(s)
    db.session.commit()

    return jsonify(msg="delete student {} Success".format(s.name))


@blue.route('/update_student/')
def update_student():
    s = Students.query.first()
    s.name = "asule"
    db.session.add(s)
    db.session.commit()
    return jsonify(msg="update student success")
