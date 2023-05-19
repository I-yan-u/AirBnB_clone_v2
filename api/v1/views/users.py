#!/usr/bin/python3
""" Defines th user"""
from models import storage
from models.user import User
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request


@app_views.route('/users/', methods=['GET'], strict_slashes=False)
def get_users():
    """ Gets all users"""
    users = storage.all(User).values()
    user_list = []
    for user in users:
        user_list.append(user.to_dict())
    return jsonify(user_list)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user_id(user_id=None):
    """ Get user by id"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_user(user_id=None):
    """ Deletes an existing user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    else:
        storage.delete(user)
        storage.save()
        return make_response(jsonify({}), 200)


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
def create_user():
    """ Creates a new User"""
    req_json = request.get_json()
    if not req_json:
        abort(400, description="Not a JSON")
    if "email" not in req_json:
        abort(400, description="Missing email")
    if "password" not in req_json:
        abort(400, description="Missing password")

    new_user = User(**req_json)
    new_user.save()
    return make_response(jsonify(new_user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user():
    """ Changes attributes of specified user"""
    req_json = request.get_json()
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not req_json:
        abort(400, description="Not a JSON")

    Ignore_list = ['id', 'email', 'created_at', 'updated_at']

    for key, val in req_json.items():
        if key not in Ignore_list:
            setattr(user, key, val)
    user.save()
    return make_response(jsonify(user.to_dict()), 200)
