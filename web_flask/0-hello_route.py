#!/usr/bin/python3
""" Flask app """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Get path / on host:5000 """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
