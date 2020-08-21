# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 10:01
# @Author  : yifei_Lu
# @Site    :
# @File    : redprint.py
# @Software: PyCharm


class Redprint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        """
        实现reprint的route装饰器
        :param rule:
        :param options:
        :return:
        """
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = self.name + '+' + \
                       options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
