from flask import Blueprint, jsonify, request
from scripts.models.user_model import User

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route("/register", methods=["POST"])
def register():
    if not request.is_json():
        return 400

    json_data = request.json

    username = json_data['username']
    password = json_data['password']
    email = json_data['email']
    phone = json_data['phone']

    User.create_user()
    
    return jsonify(), 200


@auth_routes.route("/login", methods=["POST"])
def login():
    
    if not request.is_json():
        return 400

    json_data = request.json

    username = json_data['username']
    password = json_data['password']

    return jsonify(), 200



# @auth_routes.route("/forgot-password", methods=["POST"])
# @auth_routes.route("/forgot-password/random code", methods=["POST"])
# @auth_routes.route("/change-password", methods=["POST"])
# @auth_routes.route("/get-account", methods=["POST"])
# @auth_routes.route("/update-account", methods=["POST"])
# @auth_routes.route("/delete-account", methods=["POST"])
