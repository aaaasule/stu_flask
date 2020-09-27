# -*- encoding: utf-8 -*-
import random

from flask import Blueprint
from App import models
from App.models import *


def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint("blue", __name__, template_folder="../templates")


@blue.route("/index/")
def index():
    return "success"


@blue.route("/add_student/")
def add_student():
    stu = Students()
    stu.s_age = 14
    stu.s_name = "lionel%s" % random.randrange(1000)
    stu.save()

    return "add students success"


@blue.route("/add_school/")
def add_school():
    school = School()
    school.position = "光白路%s" % random.randrange(1000)
    school.student_id = Students.query.order_by(Students.id.desc()).first().id
    school.save()
    return "add school success"
