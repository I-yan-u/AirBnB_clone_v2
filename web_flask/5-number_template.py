#!/usr/bin/python3
""" Flask app """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Get path / on host:5000 """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Get path /hbnb on host:5000 """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Get path /c/<text> on host:5000 """
    string = ""
    for c in text:
        if c == '_':
            string += " "
        else:
            string += c
    return 'C {}'.format(string)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Get path /python/<text> on host:5000 """
    string = ""
    for c in text:
        if c == '_':
            string += " "
        else:
            string += c
    return 'Python {}'.format(string)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Get path /number/<n> on host:5000 """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    """ Get path /number_template/<n> on host:5000 """
    string = 'Number: {}'.format(n)
    return render_template('5-number.html', content=string)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
