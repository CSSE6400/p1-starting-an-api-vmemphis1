from flask import Blueprint, jsonify

api = Blueprint("api", __name__, url_prefix="/api/v1")


@api.route("/health")
def health():
    return jsonify({"status": "ok"})

@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({
        "id": 1,
        "title": "Buy groceries",
        "completed": True,
        "deadline_at" : "2024-06-30T12:00:00Z",
        "created_at": "2024-06-25T10:00:00Z",
        "updated_at": "2024-06-26T15:00:00Z"
    })

@api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    return jsonify({
        "id": id,
        "title": "Buy groceries",
        "completed": True,
        "deadline_at" : "2024-06-30T12:00:00Z",
        "created_at": "2024-06-25T10:00:00Z",
        "updated_at": "2024-06-26T15:00:00Z"
    })

@api.route('/todos', methods=['POST'])
def create_todo():
    return jsonify({
        "id": 1,
        "title": "Walk the dog",
        "completed": True,
        "deadline_at" : "2024-07-01T18:00:00Z",
        "created_at": "2024-06-27T09:00:00Z",
        "updated_at": "2024-06-27T09:00:00Z"
    }), 201

@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    return jsonify({
        "id": id,
        "title": "Walk the dog",
        "description": "Take the dog for a walk in the park",
        "completed": True,
        "deadline_at" : "2024-07-01T18:00:00Z",
        "created_at": "2024-06-27T09:00:00Z",
        "updated_at": "2024-06-28T10:00:00Z"
    })

@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    return jsonify({
        "id": id,
        "title": "Walk the dog",
        "description": "Take the dog for a walk in the park",
        "completed": True,
        "deadline_at" : "2024-07-01T18:00:00Z",
        "created_at": "2024-06-27T09:00:00Z",
        "updated_at": "2024-06-28T10:00:00Z"
    })