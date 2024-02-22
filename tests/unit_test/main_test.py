import pytest
from src.main import app, get_all_users, get_user_by_id, create_user, update_user, delete_user
from flask import Flask, jsonify, request
from src.users import User
from src.controllers import UserController
from src.repositories import UserRepository

STATUS_OK = 200
CREATED = 201
NO_CONTENT = 204
BAD_REQUEST = 400
NOT_FOUND = 404


@pytest.fixture
def user_data():
    return [
        {"id": 0, "firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"},
        {"id": 1, "firstName": "Jane", "lastName": "Doe", "birthYear": 1995, "group": "user"},
        {"id": 2, "firstName": "Alex", "lastName": "Smith", "birthYear": 1985, "group": "admin"}
    ]


@pytest.fixture
def user():
    return User(2, "Alex", "Smith", 1985, "admin")


@pytest.fixture
def input_user_data():
    return {"id": 0, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}


def test_get_users_endpoint_returns_200(user_data):
    with app.test_request_context():
        users = get_all_users()
    assert users.status_code == STATUS_OK


def test_get_user_by_id_endpoint_returns_200(user):
    with app.test_request_context():
        user = get_user_by_id(user.id)
    assert user.status_code == STATUS_OK


def test_get_user_by_id_endpoint_uses_right_id(user):
    with app.test_request_context():
        get_user_by_id(user.id)
    assert request.view_args["user_id"] == user.id


def test_get_user_by_id_endpoint_returns_404():
    with app.test_request_context():
        user = get_user_by_id(999)
    assert user.status_code == NOT_FOUND


def test_post_users_endpoint_returns_201(input_user_data):
    with app.test_request_context(json=input_user_data):
        user = create_user()
    assert user.status_code == CREATED


def test_post_users_endpoint_returns_400():
    with app.test_request_context(json={"id": 0, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "ur"}):
        user = create_user()
    assert user.status_code == BAD_REQUEST


def test_patch_users_endpoint_returns_200(user):
    with app.test_request_context(json={"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}):
        user = update_user(user.id)
    assert user.status_code == STATUS_OK


def test_patch_users_endpoint_returns_400_when_wrong_id(user):
    with app.test_request_context(json={"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}):
        user = update_user(0)
    assert user.status_code == BAD_REQUEST


def test_patch_users_endpoint_returns_400_when_wrong_group(user):
    with app.test_request_context(json={"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "ur"}):
        user = update_user(0)
    assert user.status_code == BAD_REQUEST


def test_delete_user_endpoint_returns_204(user):
    user_repository = UserRepository()
    user_controller = UserController(user_repository)

    user_controller.create(user.__dict__)

    with app.test_request_context():
        response = delete_user(user.id)

    assert response.status_code == NO_CONTENT


def test_delete_user_endpoint_returns_404(user):
    with app.test_request_context():
        response = delete_user(user.id)
    assert response.status_code == NOT_FOUND
