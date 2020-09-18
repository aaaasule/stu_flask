# -*- encoding: utf-8 -*-
from flask import Blueprint
from App.logger import setup_log


def init_views(app):
    app.register_blueprint(blueprint=blue)


blue = Blueprint("blue", __name__)


@blue.route("/index/", methods=['GET'])
def index():
    logger = setup_log('test')
    logger.info("success")
    return "success"
