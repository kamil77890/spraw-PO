import pytest
from src.controllers import UserController
from src.repositories import UserRepository

@pytest.fixture
def user_repository():
    return UserRepository()

@pytest.fixture
def user_controller(user_repository):
    return UserController(repository=user_repository)

def test_user_controller_can_be_instantiated(user_controller):
    assert isinstance(user_controller, UserController)

def test_raises_on_create_method(user_controller, user_repository):
    user_data = {"id": 0, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}
    with pytest.raises(NotImplementedError):
        user_controller.create(user_data)

def test_pass_user_data_to_repository(user_controller, user_repository):
    user_data = {"id": 0, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}
    with pytest.raises(NotImplementedError):
        user_controller.create(user_data)

def test_raises_on_get_all_method(user_controller, user_repository):
    with pytest.raises(NotImplementedError):
        user_controller.get_all()

def test_raises_on_get_by_id_method(user_controller, user_repository):
    user_id = 1
    with pytest.raises(NotImplementedError):
        user_controller.get_by_id(user_id)

def test_pass_get_by_id_data_to_repository(user_controller, user_repository):
    user_id = 1
    with pytest.raises(NotImplementedError):
        user_controller.get_by_id(user_id)

def test_raises_on_update_method(user_controller, user_repository):
    user_id = 1
    user_data = {"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}
    with pytest.raises(NotImplementedError):
        user_controller.update(user_id, user_data)

def test_pass_update_data_to_repository(user_controller, user_repository):
    user_id = 1
    user_data = {"id": 3, "firstName": "Ame", "lastName": "Thing", "birthYear": 1995, "group": "user"}
    with pytest.raises(NotImplementedError):
        user_controller.update(user_id, user_data)

def test_raises_on_delete_method(user_controller, user_repository):
    user_id = 1
    with pytest.raises(NotImplementedError):
        user_controller.delete(user_id)

def test_pass_delete_data_to_repository(user_controller, user_repository):
    user_id = 1
    with pytest.raises(NotImplementedError):
        user_controller.delete(user_id)
