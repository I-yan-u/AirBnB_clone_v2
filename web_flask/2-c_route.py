#!/usr/bin/python3
""" Flask web app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_routes(text):
    """ C is ... """
    out = "C "
    for char in text:
        if char == "_":
            out += " "
        else:
            out += char
    return out


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
