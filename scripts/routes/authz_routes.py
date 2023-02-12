from flask import Blueprint, jsonify, request
from scripts.models.roles_model import Role


authz_routes = Blueprint('authz_routes', __name__)


@authz_routes.route('/roles', methods=['POST'])
def create_role():
    data = request.get_json()
    name = data.get('name')
    capacity = data.get('capacity')

    role = Role.create(name, capacity)
    response = {
        'id': role.id,
        'name': role.name,
        'capacity': role.capacity,
        'created_at': role.created_at
    }
    return jsonify(response), 201


@authz_routes.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    role = Role.get(role_id)
    if role is None:
        return '', 404
    response = {
        'id': role.id,
        'name': role.name,
        'capacity': role.capacity,
        'created_at': role.created_at
    }
    return jsonify(response), 200


@authz_routes.route('/roles', methods=['GET'])
def get_all_roles():
    roles = Role.get_all()
    response = [{
        'id': role.id,
        'name': role.name,
        'capacity': role.capacity,
        'created_at': role.created_at
    } for role in roles]
    return jsonify(response), 200


@authz_routes.route('/roles/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    role = Role.get(role_id)
    if role is None:
        return '', 404

    data = request.get_json()
    name = data.get('name')
    capacity = data.get('capacity')
    role.update(name, capacity)

    response = {
        'id': role.id,
        'name': role.name,
        'capacity': role.capacity,
        'created_at': role.created_at
    }
    return jsonify(response), 200


@authz_routes.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    role = Role.get(role_id)
    if role is None:
        return '', 404

    role.delete()
    return '', 204

