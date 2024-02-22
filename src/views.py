from flask import Flask, request, jsonify
from .services import UserService

app = Flask(__name__)
user_service = UserService()

@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user.to_json()), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if data:
        user = user_service.create_user(data)
        return jsonify(user.to_json()), 201
    return jsonify({"error": "Invalid data"}), 400

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.json
    user = user_service.update_user(user_id, data)
    if user:
        return jsonify(user.to_json()), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = user_service.delete_user(user_id)
    if success:
        return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
