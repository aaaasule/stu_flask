# -*- encoding: utf-8 -*-
from flask_restful import Resource


class UsersResource(Resource):

    def get(self):
        return {"msg": "user is ok"}


class UserResource(Resource):

    def get(self, id):
        return {"msg": "user {} is ok".format(id)}
