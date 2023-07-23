 #!/usr/bin/python3
""" Use Flask to create a simple web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Route to Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display Hbnb """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
