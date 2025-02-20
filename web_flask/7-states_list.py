#!/usr/bin/python3
"""

    Runs a Flask web application on 0.0.0.0:5000

"""
from flask import Flask, render_template
import sys
sys.path.append("../")
try:
    from models import storage
except ImportError:
    raise Exception(ImportError)

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """ Returns an HTML page of all States sorted by name """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Removes the current SQLAlchemy session. """
    storage.close()


if __name__ == "__main__":
    """ Run on 0.0.0.0 """
    app.run(host='0.0.0.0', port='5000')
