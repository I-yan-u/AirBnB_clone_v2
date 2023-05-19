#!/usr/bin/python3
""" Defines the state /api/v1/cities api"""
from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def city_by_state_id(state_id=None):
    """ Get cities in a State with state id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    city_list = []
    cities = state.cities
    for city in cities:
        city_list.append(city.to_dict())
    return jsonify(city_list)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city_id(city_id=None):
    """ Get city with City id"""
    citi = storage.get(City, city_id)
    if not citi:
        abort(404)
    else:
        return jsonify(citi.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_city(city_id=None):
    """ Delete city with city id"""

    citi = storage.get(City, city_id)
    if citi:
        storage.delete(citi)
        storage.save()
        return make_response(jsonify({}), 200)
    else:
        abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """ Creates a city under a state"""
    req_json = request.get_json()
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not req_json:
        abort(400, description="Not a JSON")
    if "name" not in req_json:
        abort(400, description="Missing name")
    req_json['state_id'] = state_id
    new_city = City(**req_json)
    new_city.save()
    return make_response(jsonify(new_city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """ update attribute of a certain city"""
    citi = storage.get(City, city_id)
    req_json = request.get_json()
    if not citi:
        abort(404)
    if not req_json:
        abort(400, description="Not a JSON")

    Ignore_list = ['id', 'state_id', 'created_at', 'updated_at']

    for key, val in req_json.items():
        if key not in Ignore_list:
            setattr(citi, key, val)
    citi.save()
    return make_response(jsonify(citi.to_dict()), 200)
