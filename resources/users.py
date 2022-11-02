import json
import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

user = Blueprint("users", "user")

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
user.route("/", methods = ["POST"])
def create_user():
    """Create user and send to database"""
    payload = request.get_json()
    print(type(payload), "payload")
    user = models.User.create(**payload)
    print(user.__dict__)
    print(dir(user))
    user_dict = model_to_dict(user)
    return jsonify(
        data = user_dict,
        status = {
            "code": 201,
            "message": "Successfully Registered"
        }
    )