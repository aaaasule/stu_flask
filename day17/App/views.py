# -*- encoding: utf-8 -*-
import random

from flask import Blueprint, render_template, request
from App import models
from App.models import Cats, Dogs, Customer, Address


def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint('blue', __name__, template_folder="../templates")


@blue.route("/index/")
def index():
    return "success"


@blue.route("/add_cat/")
def add_cat():
    cat = Cats()
    cat.a_name = "大花"
    cat.a_weight = "40"
    cat.a_height = "168"
    cat.a_color = "花色"
    cat.a_detail = "大花大花大花"
    cat.c_eat = "fish"
    cat.save()

    return "add cat da hua  success"


@blue.route("/add_dog/")
def add_dog():
    dog = Dogs()
    dog.a_name = "大狗"
    dog.a_height = "185"
    dog.a_weight = "80"
    dog.a_color = "白色"
    dog.a_detail = "大狗名叫苟日新"
    dog.save()

    return "add da gou success"


@blue.route("/get_cats/")
def get_cats():
    # cats = Cats.query.filter(Cats.id == 2).all()   # filter参数为 SQL Expression
    # cats = Cats.query.get_or_404(1)
    # cats = Cats.query.filter(Cats.a_name.contains("大")).all()   # 类似模糊查询
    # cats = Cats.query.all() # 查询所有
    # cats = Cats.query.get(1)  # 根据主键查询
    # cats = Cats.query.filter_by(id=1, a_name="大花").all()  # filter_by   关键参数查询 多个字段之间关系为and
    from sqlalchemy import or_
    # cats = Cats.query.filter(or_(Cats.id == 1, Cats.a_name == "二花")).all()  # filter   关键参数查询 多个字段之间关系为 or
    # cats = Cats.query.offset(1).limit(2)  # 跳过第一个，限制显示条数   offset 和 limit 不区分前后关系
    # cats = Cats.query.limit(2).offset(1)  # 跳过前几天，限制显示条数   order_by 调用必须在offset和limit之前

    cats = Cats.query.order_by('id').offset(2).limit(3)
    print(cats)
    print(type(cats))
    return render_template("Cats.html", cats=cats)


@blue.route("/update_cat/")
def update_cat():
    cat = Cats.query.get(1)  # 先查询到该条数据 在修改  commit()
    cat.a_height = "170"
    cat.save()

    return "update cat success"


@blue.route("/delete_cat/")
def delete_cat():
    cat = Cats.query.get(3)
    cat.delete()

    return "delete cat success"


@blue.route("/add_dogs/")
def add_dogs():
    for i in range(10):
        dog = Dogs()
        dog.a_name = "狗子-{}".format(random.randint(1, 1000))
        dog.save()

    return "add dogs success"


@blue.route("/get_dog/")
def get_dog():
    page = request.args.get('page', 1, int)
    per_page = request.args.get('per_page', 4, int)

    dogs = Dogs.query.offset((page - 1) * per_page).limit(per_page)
    print(dogs)
    print(type(dogs))
    return render_template("Dogs.html", dogs=dogs)


@blue.route("/get_dogs_with_page/")
def get_dogs_with_page():
    pagination = Dogs.query.paginate()
    per_page = request.args.get('per_page', 4, int)
    return render_template("Dogs.html", pagination=pagination, per_page=per_page)


@blue.route("/add_customer/")
def add_customer():
    customer = Customer()
    customer.c_name = "lionel{}".format(random.randrange(10000))
    customer.save()

    return "add customer success %s" % customer.c_name


@blue.route("/add_address/")
def add_address():
    address = Address()
    address.a_address = "召唤师峡谷{}".format(random.randrange(10000))
    address.c_customer_id = Customer.query.order_by(Customer.id.desc()).first().id

    address.save()

    return "add address success %s " % address.c_customer_id


@blue.route("/get_customer/")
def get_customer():
    a_id = request.args.get('a_id', type=int)
    address = Address.query.get(a_id)
    customer = Customer.query.get(address.id)
    print(address, customer)
    return "customer %s %s" % (customer.id, customer.c_name)
