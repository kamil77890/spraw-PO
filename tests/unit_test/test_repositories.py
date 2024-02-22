import pytest
from src.repositories import UserRepository

@pytest.fixture
def user_repository():
    return UserRepository()

def test_create_user(user_repository):
    user_data = {"firstName": "vxdvxd", "lastName": "xvdvxdv", "birthYear": "1990-01-01", "group": "user"}
    initial_user_count = len(user_repository.get_all_users())
    user_repository.create_user(user_data)
    assert len(user_repository.get_all_users()) == initial_user_count + 1

def test_get_all_users(user_repository):
    assert isinstance(user_repository.get_all_users(), list)

def test_get_user_by_id(user_repository):
    user_data = {"firstName": "dvxvx", "lastName": "vdxvx", "birthYear": "1990-01-01", "group": "user"}
    created_user = user_repository.create_user(user_data)
    fetched_user = user_repository.get_user_by_id(created_user["id"])
    assert fetched_user == created_user

def test_update_user(user_repository):
    user_data = {"firstName": "vxdv", "lastName": "vxdv", "birthYear": "1990-01-01", "group": "user"}
    created_user = user_repository.create_user(user_data)
    updated_data = {"firstName": "vxdv", "lastName": "vxdv"}
    updated_user = user_repository.update_user(created_user["id"], updated_data)
    assert updated_user["firstName"] == "vxdv" and updated_user["lastName"] == "vxdv"

def test_delete_user(user_repository):
    user_data = {"firstName": "vxdv", "lastName": "vxdvxd", "birthYear": "1990-01-01", "group": "user"}
    created_user = user_repository.create_user(user_data)
    initial_user_count = len(user_repository.get_all_users())
    user_repository.delete_user(created_user["id"])
    assert len(user_repository.get_all_users()) == initial_user_count - 1
