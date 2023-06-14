import os

import pytest

from src.hello.models import BasicHello, SecretAnswer
from src.hello.services import handle_hello


@pytest.fixture()
def common_user():
    return "common_user"


@pytest.fixture()
def secret_user():
    dan = "dan"
    os.environ.setdefault("SECRET_NAME", dan)
    return dan


def test_hello_for_common_user(common_user):
    hello_response = handle_hello(common_user)

    assert isinstance(hello_response, BasicHello)
    assert hello_response.name == common_user


def test_hello_for_secret_user(secret_user):
    hello_response = handle_hello(secret_user)

    assert isinstance(hello_response, SecretAnswer)
    assert hello_response.name == secret_user
