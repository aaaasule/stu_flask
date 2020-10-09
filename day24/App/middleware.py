# -*- encoding: utf-8 -*-
from flask import request, g


def load_middleware(app):
    @app.before_request
    def before():
        g.msg = "hahhah"
        print("request_url", request.url)

    @app.after_request
    def after(resp):
        print("resp:", resp)
        print(type(resp))
        return resp
