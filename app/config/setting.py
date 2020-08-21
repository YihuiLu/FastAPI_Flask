# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 09:47
# @Author  : yifei_Lu
# @Site    :
# @File    : setting.py
# @Software: PyCharm
import os

"""非敏感信息配置文件"""

TOKEN_EXPIRATION = 30 * 24 * 3600  # token过期时间（开发期间设置为一个月）

# JSONIFY_PRETTYPRINT_REGULAR = True

API_DOC_MEMBER = ['v1']  # 需要生成api的路由地址，列表内配置的不是蓝图名，而是路由第一级地址名

if os.environ.get('DEPLOY_ENV') == 'PRODUCTION':
    DEBUG = False
else:
    DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = True
