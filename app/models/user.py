import bcrypt
import datetime
import uuid

db = []


class User:

    def __init__(self, username, email, password):

        self.username = username
        self.email = email
        self.password = password
        self.db = db

    def create_user(self):
        self.db.append({
            'username': self.username,
            'email': self.email,
            'password': self.password,
            "user_id": str(uuid.uuid4())
        })

    @staticmethod
    def get_user(field,value):
        for user in db:
            if user[field] == value:
                return user

    @staticmethod
    def get_users():
        return db

    def delete_user(self, user):
        self.db.pop(user)

    def update_user(self, user, field):
        pass

# ben = User('benedict',"ben@gmail.com","asdfgh")
# ben.create_user()
# print(ben.get_users())
# ben.login('benedict','asdfh')
