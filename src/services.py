from .models import User

class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, data):
        user_id = len(self.users) + 1
        user = User(user_id, data['firstName'], data['lastName'], data['birthYear'], data['group'])
        self.users[user_id] = user
        return user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        if user:
            if 'firstName' in data:
                user.first_name = data['firstName']
            if 'lastName' in data:
                user.last_name = data['lastName']
            if 'birthYear' in data:
                user.birth_year = data['birthYear']
            if 'group' in data:
                user.group = data['group']
            return user
        return None

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def get_all_users(self):
        return [user.to_json() for user in self.users.values()]
