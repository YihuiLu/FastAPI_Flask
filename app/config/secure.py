# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 09:47
# @Author  : yifei_Lu
# @Site    :
# @File    : secure.py
# @Software: PyCharm

"""敏感信息配置文件"""

import os

# 演示时使用SQLit, 可以换成Mysql或其他
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temporary.db')

SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'
