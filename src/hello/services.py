from src.hello.config import get_secret_name
from src.hello.models import SecretAnswer, BasicHello


def handle_hello(name: str):
    if name == get_secret_name():
        return SecretAnswer(name=name, secret="qwerty12345")

    return BasicHello(name)
