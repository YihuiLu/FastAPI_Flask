# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 10:51
# @Author  : yifei_Lu
# @Site    :
# @File    : enums.py
# @Software: PyCharm
from enum import Enum

"""
此模块用于定义枚举为框架使用

"""


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 小程序
    USER_MINA = 200
