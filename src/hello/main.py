from flask import Flask, jsonify

from src.hello.entrypoints import hello_route

app = Flask(__name__)

app.register_blueprint(hello_route)


@app.route("/ping")
def ping():
    return jsonify({"ok": True}), 200
