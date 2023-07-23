#!/usr/bin/python3
""" Flask web app """
from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_routes(text="is cool"):
    """ Python is cool """
    out = "Python "
    for char in text:
        if char == "_":
            out += " "
        else:
            out += char
    return out


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ number in root """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Loads template HTML in n is int """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
