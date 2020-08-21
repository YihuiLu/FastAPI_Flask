# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 2:58 下午
# @Author  : Teacher Lu
# @FileName: hello.py
# @Software: PyCharm
# @Blog    : https://www.yifeilu.cn

from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError, Optional
from app.validators.base import BaseForm as Form


class PostHelloForm(Form):
    language = StringField(validators=[DataRequired()])
    color = StringField(validators=[Optional()], default='蓝色')

    def validate_language(self, value):
        keys = ['zh', 'en']
        if value.data not in keys:
            raise ValidationError('超出语言范围, 可选值:{}'.format(str(keys)))
