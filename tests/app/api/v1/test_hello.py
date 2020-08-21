# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 2:28 下午
# @Author  : Teacher Lu
# @FileName: test_hello.py
# @Software: PyCharm
# @Blog    : https://www.yifeilu.cn


def test_hello(client):
    rv = client.get('/v1/hello')
    data = rv.data
    print(data)
    assert b'Hello' in data


def test_post_hello(client):
    rv = client.post('/v1/hello', json={
        "language": "zh"
    })
    data = rv.get_json()
    print(data)
    assert 'success' == data.get('msg')
