from flask import Blueprint, request, jsonify
from repository.targets_repository import find_target_by_id, find_all_targets
from service.target_service import convert_to_json


target_blueprint = Blueprint("target", __name__)

@target_blueprint.route("/<int:t_id>", methods=['GET'])
def get_target(t_id: int):
    return (
        find_target_by_id(t_id)
        .map(convert_to_json)
        .map(lambda c: (jsonify(c), 200))
        .value_or((jsonify({}), 404))
    )

@target_blueprint.route('/', methods=['GET'])
def get_all_targets():
    try:
        targets = find_all_targets()
        return jsonify({"targets": targets}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
