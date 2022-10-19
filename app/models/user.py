import bcrypt
db = []


class User:

    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.password = password
        self.db = db

    def create_user(self):
        self.db.append({
            'name':self.name,
            'email':self.email,
            'password': self.password
        })

    def get_user(self,username):
        for user in self.db:
            if user['name'] == username:
                return user

    def get_users(self):
        return self.db

    def delete_user(self,user):
        self.db.pop(user)

    def update_user(self, user,field):


ben = User('benedict',"ben@gmail.com","asdfgh")
ben.create_user()
# print(ben.get_users())
ben.login('benedict','asdfh')