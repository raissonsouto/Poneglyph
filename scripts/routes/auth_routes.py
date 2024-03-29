from flask import Blueprint, jsonify, request
from scripts.models.user_model import User
from scripts.util.messages import Messages

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route("/register", methods=["POST"])
def register():
    if not request.is_json:
        return jsonify({'message': Messages.REQUEST_IS_NOT_A_JSON}), 400

    json_data = request.json

    username = json_data['username']
    password = json_data['password']
    email = json_data['email']
    phone = ""

    try:
        phone = json_data['phone']
    except KeyError:
        pass

    if not username or not password or not email:
        return jsonify({'message': Messages.MISSING_PARAMS}), 400

    if not User(username, email, password, phone):
        return jsonify({'message': Messages.REGISTER_FAILED}), 400

    return jsonify({'message': Messages.REGISTER_SUCCESED}), 200


@auth_routes.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({'message': Messages.REQUEST_IS_NOT_A_JSON}), 400

    json_data = request.json

    username = json_data['username']
    password = json_data['password']

    if not username or not password:
        return jsonify({'message': Messages.MISSING_PARAMS}), 400

    user_session_token = User.authenticate(username, password)

    if not user_session_token:
        return jsonify({'message': Messages.INVALID_CREDENTIALS}), 401

    return jsonify(), 200


# @auth_routes.route("/forgot-password", methods=["POST"])

# @auth_routes.route("/forgot-password/random code", methods=["POST"])

# @auth_routes.route("/change-password", methods=["POST"])
