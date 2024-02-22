from flask import Flask, request, jsonify
from controllers import UserController
from repositories import UserRepository

app = Flask(__name__)
user_repository = UserRepository()
user_controller = UserController(user_repository)

@app.route("/users", methods=["GET"])
def get_all_users():
    users = user_controller.get_all()
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = user_controller.get_by_id(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.json
    user = user_controller.create(user_data)
    return jsonify(user), 201

@app.route("/users/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    user_data = request.json
    user = user_controller.update(user_id, user_data)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    success = user_controller.delete(user_id)
    if success:
        return "", 204
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
