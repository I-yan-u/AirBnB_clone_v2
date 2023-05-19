#!/usr/bin/python3
""" Defines the state /api/v1/states api"""
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
def get_states():
    """ Get all states in storage or db """
    all_states = storage.all(State).values()
    state_list = []
    for state in all_states:
        state_list.append(state.to_dict())
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_states_id(state_id=None):
    """ Get individual states by id"""
    data = storage.get(State, state_id)
    if not data:
        abort(404)
    else:
        return jsonify(data.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_state(states_id=None):
    """ Deletes state by id"""
    data = storage.get(State, state_id)
    if data:
        storage.delete(data)
        storage.save()
        return make_response(jsonify({}), 200)
    else:
        abort(404)


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def post_state():
    """ handles a post request """
    req_json = request.get_json()
    if not req_json:
        abort(400, description="Not a JSON")
    if "name" not in req_json:
        abort(400, description="Missing name")
    else:
        new_state = State(**req_json)
        new_state.save()
        return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id=None):
    """ Updates db/storage from put request"""
    state = storage.get(State, state_id)
    req_json = request.get_json()
    if not state:
        abort(404)
    if not req_json:
        abort(400, description="Not a JSON")

    Ignore_keys = ['id', 'created_at', 'updated_at']

    for key, value in req_json.items():
        if key not in Ignore_keys:
            setattr(state, key, value)
    state.save()
    return make_response(jsonify(state.to_dict()), 200)
