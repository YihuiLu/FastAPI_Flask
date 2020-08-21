# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 09:54
# @Author  : yifei_Lu
# @Site    :
# @File    : book.py
# @Software: PyCharm
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from flask import jsonify

from app.models.base import db
from app.models.hello import Hello
from app.validators.app.v1.hello import PostHelloForm

api = Redprint('hello')


@api.route("", methods=['GET'])
def get_hello():
    """获取hello接口

    @@@
    ## function:

    - ##### Description:
        > 获取hello接口
    - ##### Login authentication :   ` True `
    - ##### Content-Type : ` application/json `


    ## request:

    - ### headers

    | args | nullable | type | remark |
    |:------:|:-----:|:-----:|:------:|
    | token  | false | str   | token  |


    - ### args

    Overall


     | args | type | nullable | remark |
    | :--------:|:--------:|:--------:|:--------: |                                              |

    - #### Request the sample:
        ```
        {}
        ```

    ## return:
    - ### args

    | args | type | remark |
    |:------:|:-----:|:-----:|
    |  msg  |  str  |  消息  |


    - #### responseType: ` json `
        ```
        {"msg": "Hello World"}
        ```
    @@@
    """
    return jsonify({"msg": "Hello World"})


@api.route("", methods=['POST'])
def post_hello():
    """上传hello接口

    @@@
    ## function:

    - ##### Description:
        > 上传hello接口
    - ##### Login authentication :   ` True `
    - ##### Content-Type : ` application/json `


    ## request:

    - ### headers

    | args | nullable | type | remark |
    |:------:|:-----:|:-----:|:------:|
    | token  | false | str   | token  |


    - ### args

    Overall


     | args | type | nullable | remark |
    | :--------:|:--------:|:--------:|:--------: |
    | language | str | False |  |                                              |

    - #### Request the sample:
        ```
        {"language":"zh"}
        ```

    ## return:
    - ### args

    | args | type | remark |
    |:------:|:-----:|:-----:|


    - #### responseType: ` json `
        ```
        {"error_code": 0, "msg": "success", "request": "POST /v1/hello"}
        ```
    @@@
    """
    form = PostHelloForm().validate_for_api()
    with db.auto_commit():
        hello = Hello()
        hello.set_attrs(form.data)
        db.session.add(hello)
    return Success(msg='success')
