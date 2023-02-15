from flask import Blueprint, jsonify, request
from scripts.util.messages import Messages


auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route("/get-account", methods=["POST"])
def get_account():
    if not request.is_json:
        return jsonify({'message': Messages.REQUEST_IS_NOT_A_JSON}), 400
    return 200


@auth_routes.route("/update-account", methods=["POST"])
def update_account():
    if not request.is_json:
        return jsonify({'message': Messages.REQUEST_IS_NOT_A_JSON}), 400
    return 200


@auth_routes.route("/delete-account", methods=["POST"])
def delete_account():
    if not request.is_json:
        return jsonify({'message': Messages.REQUEST_IS_NOT_A_JSON}), 400
    return 200
