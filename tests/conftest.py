# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 10:07 上午
# @Author  : Teacher Lu
# @FileName: conftest.py.py
# @Software: PyCharm
# @Blog    : https://www.yifeilu.cn


import os

import pytest

from app import create_app
from app.models.base import get_db
from app.models.base import init_db

# read in SQL for populating test data
with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""

    # create the app with common test config
    app = create_app(True)
    # create the database and load test data
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app
    # remove the database
    os.remove(app.config["SQLALCHEMY_DATABASE_URI"].replace("sqlite:///", ''))


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, username="test", password="test"):
        return self._client.post(
            "/auth/login", data={"username": username, "password": password}
        )

    def logout(self):
        return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
    return AuthActions(client)
