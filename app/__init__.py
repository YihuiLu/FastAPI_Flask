# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 09:45
# @Author  : yifei_Lu
# @Site    :
# @File    : __init__.py.py
# @Software: PyCharm
from .app import Flask
from flask_docs import ApiDoc


def register_blueprints(app):
    """
    此函数用于将redprint注册到blueprint
    :param app:
    :return:
    """
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)


def create_app(test_config=False):
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    if test_config:
        app.config.from_object('app.config.test')
    register_blueprints(app)
    register_plugin(app)
    ApiDoc(app)
    return app
