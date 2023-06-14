from flask import jsonify
from flask.blueprints import Blueprint

from src.hello.services import handle_hello


hello_route = Blueprint("hello", __name__)


@hello_route.route("/hello", methods=("GET",))
def hello():
    return jsonify({"text": "hello, bro"})


@hello_route.route("/hello/<name>")
def hello_with_name(name: str):
    user_hello = handle_hello(name)

    return jsonify(user_hello.to_user())
