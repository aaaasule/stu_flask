# -*- encoding: utf-8 -*-
from flask_restful import Api

from App.apis.goods import *
from App.apis.hellloworld import HelloWorldResource
from App.apis.user_api import *

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(HelloWorldResource, "/hello/")
api.add_resource(GoodsListResource, "/goods/")
api.add_resource(GoodsResource, "/goods/<int:id>/")

api.add_resource(UsersResource, "/users/")
api.add_resource(UserResource, "/user/<int:id>/")
