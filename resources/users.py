import json
import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

from flask_bcrypt import generate_password_hash

user = Blueprint("users", "user", url_prefix = "/users")

# SHOW USER ROUTE
@user.route('/<id>', methods = ["GET"])
def get_user(id):
    """Get one user by ID"""
    print("Parameters", id)
    try:
        user = [model_to_dict(user) for user in models.User.select()]
        if user:
            return jsonify(
            data = user,
            status = {
                "code": 200,
                "message": "Success"
                }
            ), 200
        else:
            return jsonify(
                status = {
                    "code": 404,
                    "message": "User not found",
                }
            ), 404
        
    except models.DoesNotExist:
        return jsonify(
            data = {},
            status = {
                "code": 401,
                "message" : "Error getting data"
            }
        )
        
# CREATE USER ROUTE
@user.route("/register", methods = ["POST"])
def create_user():
    """Create user and send to database"""
    print("Create User Started")
    payload = request.get_json()
    payload['email'] = payload['email'].lower()
    try:
        models.User.get(models.User.email == payload['email'])
        return jsonify(
            data = {},
            status = {
                "code": 401,
                "message": "A user with that email already exist."
            }
        ), 401
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        user = models.User.create(**payload)
        # Add login_user on this line
        # return created user
        user_dict = model_to_dict(user)
        del user_dict['password']
        print(f"User {user_dict['id']} created.")
        return jsonify(
            data = user_dict,
            status = {
                "code": 201,
                "message": "Account Register Successfully"
                }
            ), 201