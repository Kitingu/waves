from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import json

load_dotenv()
db = SQLAlchemy()


# User Model class
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(360), nullable=False)
    user_id = db.Column(db.String(60), unique=True, nullable=False)
    date_created = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.String(60), default=False, nullable=False)

    # initialize the class
    def __init__(self, username, email, password, user_id, date_created, is_admin):
        self.username = username
        self.email = email
        self.password = password
        self.user_id = user_id
        self.date_created = date_created
        self.is_admin = is_admin

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.user_id}', '{self.date_created}', '{self.is_admin}')"

    # create a new user
    def create_user(self):
        try:
            user = User(username=self.username, email=self.email, password=self.password, user_id=self.user_id,
                        date_created=self.date_created, is_admin=self.is_admin)
            db.session.add(user)
            db.session.commit()
            serialized_user = {
                "username": user.username,
                "email": user.email,
                "user_id": user.user_id,
                "date_created": user.date_created,
                "is_admin": user.is_admin
            }
            return serialized_user
        except Exception as e:
            print("exception", e)
            db.session.rollback()

    # get all users
    @classmethod
    def get_users(cls):
        users = cls.query.all()
        return users

    # get a user by id
    @classmethod
    def get_user(cls, field, value):
        user = cls.query.filter_by(**{field: value}).first()
        print("user", type(user), user)
        return user

    # get a user by id
    @classmethod
    def get_user_by_id(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        return user

    # update a user
    @classmethod
    def update_user(cls, user_id, data):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            for key, value in data.items():
                setattr(user, key, value)
            db.session.commit()
            return user
        return False
