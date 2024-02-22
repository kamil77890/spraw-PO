import pytest
from src.repositories import UserRepository

@pytest.fixture
def user_repository():
    return UserRepository()

def test_create_user(user_repository):
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": "1990-01-01", "group": "user"}
    initial_user_count = len(user_repository.get_all_users())
    user_repository.create_user(user_data)
    assert len(user_repository.get_all_users()) == initial_user_count + 1

