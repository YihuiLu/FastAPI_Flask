# -*- coding: utf-8 -*-
# @Time    : 2019-04-28 09:44
# @Author  : yifei_Lu
# @Site    :
# @File    : run.py.py
# @Software: PyCharm
from flask import request
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if app.config['DEBUG']:
        app.logger.info(request.data)
        app.logger.error(e)
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            # app.logger.error(e)
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(port=7777)
