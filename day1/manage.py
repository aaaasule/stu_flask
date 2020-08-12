# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 0021 9:10
# @Author  : Zhang
# @File    : manage.py

from flask_script import Manager

from App import create_app

app = create_app()
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
