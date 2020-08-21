# -*- coding: utf-8 -*-
# @Time    : 2019-04-30 10:28
# @Author  : yifei_Lu
# @Site    :
# @File    : auth.py
# @Software: PyCharm
from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    """
    使用HTTPBasicAuth验证时，前端应该遵守以下规范：
    1. 密钥数据应放在请求头中
    2. 请求头的key应是 Authorization
    3. 值应是 basic base64(qiyue:123456)
              ^            ^   ^  ^
        声明加密类型       账号 冒号 密码
                  ^            ^
            不可缺少空格   将账号，冒号，密码组成的字符串base64加密
    """
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        # request
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid',
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired',
                         error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    # request 视图函数
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden()
    return User(uid, ac_type, scope)
