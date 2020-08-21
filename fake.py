# -*- coding: utf-8 -*-
# @Time    : 2019-05-04 12:24
# @Author  : yifei_Lu
# @Site    :
# @File    : fake.py
# @Software: PyCharm


from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'Super'
        user.password = '123456'
        user.email = '999@qq.com'
        user.auth = 2
        db.session.add(user)
