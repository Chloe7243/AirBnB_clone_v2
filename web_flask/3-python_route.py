#!/usr/bin/python3
""" Web Flask """
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python(text="is cool"):
    return f"Python {escape(text).replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5300)
