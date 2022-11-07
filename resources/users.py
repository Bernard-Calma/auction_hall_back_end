import json
import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required

user = Blueprint("users", "user", url_prefix = "/users")

# SHOW USER ROUTE
@user.route('/login', methods = ["POST"])
def get_user():
    """Login Route"""
    print(request.get_json())
    payload = request.get_json()
    payload['email'] = payload['email'].lower()
    try:
        print("Login")
        user = models.User.get(models.User.email == payload['email'])
        # print("USER", user)
        user_dict = model_to_dict(user)
        if (check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)
            # print("current user", current_user.__dict__)
            return jsonify(
            data = user_dict,
            status = {
                "code": 200,
                "message": "Login Sucessfully"
                }
            ), 200
        else:
            return jsonify(
                data = {},
                status = {
                    "code": 404,
                    "message": "Username or Password does not match",
                }
            ), 404
        
    except models.DoesNotExist:
        return jsonify(
            data = {},
            status = {
                "code": 401,
                "message" : "Username or Password does not match"
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
        login_user(user)
        # return created user
        # print(user)
        user_dict = model_to_dict(current_user, "current user")
        del user_dict['password']
        print(f"User {user_dict['id']} created.")
        return jsonify(
            data = user_dict,
            status = {
                "code": 201,
                "message": "Account Registered Successfully"
                }
            ), 201

# Get All Users Route
@user.route('/', methods = ["GET"])
def get_all_users():
    """GET ALL USERS"""
    for user in models.User.select():
        print(user.__dict__)
    return {
        "message": "yes"
    }
