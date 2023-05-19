#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

apiHost = getenv("HBNB_API_HOST")
apiPort = getenv("HBNB_API_PORT")

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(Exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def error_404(self):
    """ handle error_404 """
    error_dict = {"error": "Not found"}
    return make_response(jsonify(error_dict), 404)


if __name__ == '__main__':
    if apiPort and apiHost:
        app.run(host=apiHost, port=apiPort, threaded=True, debug=True)
    else:
        app.run(host='0.0.0.0', port='5000', threaded=True, debug=True)
