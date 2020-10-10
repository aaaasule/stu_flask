# -*- encoding: utf-8 -*-
from flask_restful import Resource


class HelloWorldResource(Resource):

    def get(self):
        return {"msg": "hello world"}
