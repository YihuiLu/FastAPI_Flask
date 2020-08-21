# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 09:54
# @Author  : yifei_Lu
# @Site    :
# @File    : user.py
# @Software: PyCharm

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User
from flask import jsonify, g

api = Redprint('user')


@api.route("/get")
@auth.login_required
def get_user():
    """获取用户信息接口

        @@@
        ## function:

        - ##### describe:
        > 用于获取用户信息
        - ##### Login authentication :   ` True `
        - ##### Content-Type : ` application/json `

        ## request:


        - ### headers

        | args | nullable | type | remark |
        |:------:|:-----:|:-----:|:------:|
        | Authorization| false | Basic Auth | token(Basic Auth 协议，将token作为username发送)  |


        - ### args

        | args | nullable | type | remark |
        |:------:|:-----:|:-----:|:------:|
        |        |       |       |        |


        - #### Request the sample:
        ```
        GET /v1/user/get HTTP/1.1
        Host: 127.0.0.1:5000
        Authorization: Basic ZXlKaGJHY2lPaUpJVXpVeE1pSXNJbWxoJOdmNHVWlmUS5mWTZaMGd4b1BtaDFhfQlprQ1NQUTlIVURVV0FmUTo=
        Host: 127.0.0.1:5000
        ```


        ## return:
        - ### args

        | args | type | remark |
        |:------:|:-----:|:-----:|
        |        |       |       |



        - #### responseType: ` json `
        ```
       {
            "code": 200,
            "data": null,
            "msg": "success"
        }
        ```
        @@@
        """

    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    """

    :return:
    """
    uid = g.user.uid  # 防止超权
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)
