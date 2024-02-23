from datetime import datetime

class User:
    def __init__(self, id, first_name, last_name, birth_year, group):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.group = group

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "age": datetime.year() - self.birth_year,
            "group": self.group
        }
