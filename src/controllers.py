from repositories import UserRepository

class UserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def create(self, user_data):
        return self._repository.create_user(user_data)

    def get_all(self):
        return self._repository.get_all_users()

    def get_by_id(self, user_id):
        return self._repository.get_user_by_id(user_id)

    def update(self, user_id, user_data):
        return self._repository.update_user(user_id, user_data)

    def delete(self, user_id):
        return self._repository.delete_user(user_id)