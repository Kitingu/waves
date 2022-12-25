import bcrypt
from datetime import date
import uuid

db = []


class User:

    def __init__(self, username, email, password):

        self.username = username
        self.email = email
        self.password = password
        self.date_created= date.today().strftime("%d/%m/%Y")

    def create_user(self):
        user = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            "user_id": str(uuid.uuid4()),
            "date_created":self.date_created
        }
        db.append(user)
        return {
            'username': user['username'],
            'email': user['email'],
            'user_id': user['user_id'],
            'date_created': user['date_created']

        }

    @classmethod
    def get_user(cls,field, value):
        for user in db:
            if user[field] == value:
                return user

    @staticmethod
    def get_users():
        return db

    @staticmethod
    def delete_user(user):
        db.pop(user)

    def update_user(self, user, field):
        pass

# ben = User('benedict',"ben@gmail.com","asdfgh")
# ben.create_user()
# print(ben.get_users())
# ben.login('benedict','asdfh')
