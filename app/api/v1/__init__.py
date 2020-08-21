# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 09:54
# @Author  : yifei_Lu
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

"""
v1 表示版本号
此模块用于实现redprint
"""

from flask import Blueprint
from app.api.v1 import hello, user, client, token


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    hello.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    return bp_v1
