# -*- encoding: utf-8 -*-
from flask import request
from flask_restful import Resource, abort, fields, marshal, marshal_with

from App.models import Goods

good_fields = {
    "id": fields.Integer,
    "g_name": fields.String(attribute="d_name"),
    "g_price": fields.Float
}

single_fields = {
    "data": fields.Nested(good_fields),
    "status": fields.Integer,
    "msg": fields.String
}

multi_goods_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(good_fields))
}


class GoodsListResource(Resource):
    @marshal_with(multi_goods_fields)
    def get(self):
        good_list = Goods.query.all()
        data = {
            "status": 200,
            "msg": "ok",
            "data": good_list
        }

        return data

    @marshal_with(single_fields)
    def post(self):
        g_name = request.form.get("g_name")
        g_price = request.form.get("g_price")
        goods = Goods()
        goods.d_name = g_name
        goods.g_price = g_price

        # data = {"msg": "create success", "status": 201, "data": marshal(goods, good_fields)}
        data = {"msg": "create success", "status": 201, "data": goods}
        if not goods.save():
            abort(400)
        return data


class GoodsResource(Resource):
    @marshal_with(single_fields)
    def get(self, id):
        goods = Goods.query.get(id)

        data = {
            "status": 200,
            "msg": "success",
            "data": goods
        }
        return data

    def delete(self, id):
        goods = Goods.query.get(id)

        if not goods:
            abort(400)
        if not goods.delete():
            abort(400)
        data = {
            "msg": "success",
            "status": 204
        }
        return data

    @marshal_with(single_fields)
    def put(self, id):
        goods = Goods.query.get(id)

        if not goods:
            abort(404, message="goods doesn't exists")
        g_price = request.form.get("g_price")
        g_name = request.form.get("g_name")
        goods.d_name = g_name
        goods.g_price = g_price

        if not goods.save():
            abort(400)
        data = {
            "status": 201,
            "msg": "put ok",
            "data": goods
        }

        return data

    @marshal_with(single_fields)
    def patch(self, id):
        goods = Goods.query.get(id)

        if not goods:
            abort(404)
        g_price = request.form.get("g_price")
        g_name = request.form.get("g_name")
        goods.d_name = g_name or goods.d_name
        goods.g_price = g_price or goods.g_price

        if not goods.save():
            abort(400)
        data = {
            "status": 201,
            "msg": "patch ok",
            "data": goods
        }

        return data
