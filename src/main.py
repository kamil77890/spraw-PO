from datetime import datetime
from flask import Flask, request, Response, jsonify
from src.controllers import UserController
from src.users import UserService
from src.users import User

app = Flask(__name__)
user_repository = UserService()
user_controller = UserController(user_repository)

@app.get("/users")
def get_all_users():
    users = user_controller.get_all()
    return jsonify([user.as_dict for user in users])

@app.get("/users/<int:user_id>")
def get_user_by_id(user_id):
    user = user_controller.get_by_id(user_id)
    if user:
        return jsonify(user.as_dict), 200

@app.post("/users")
def create_user():
    user_data = request.json
    user = user_controller.create(user_data)
    return "", 201

@app.patch("/users/<int:user_id>")
def update_user(user_id):
    user_data = request.json
    user = user_controller.update(user_id, user_data)
    if user:
        return "", 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    success = user_controller.delete(user_id)
    if success:
        return "", 204