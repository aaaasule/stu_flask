# -*- encoding: utf-8 -*-
from flask import request


def load_middleware(app):
    @app.before_request
    def before():
        print("request_methods", request.method)

    @app.after_request
    def after(resp):
        print("resp", resp)
        print("type:", type(resp))
        return resp
