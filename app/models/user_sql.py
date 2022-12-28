import uuid
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy import Column,create_engine
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from datetime import date
import os

load_dotenv() 


db =create_engine("mssql+pyodbc://"+os.getenv("DB_USER")+":"+os.getenv("DB_PASSWORD")+"@"+os.getenv("DB_SERVER_NAME")+"/"+os.getenv("DB_NAME")+"?driver="+os.getenv("DB_DRIVER_NAME"))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(50))
    user_id = Column(String(50))
    date_created = Column(String(50))
    is_admin = Column(String)

    # repr method is used to print the object in a readable format for debugging purposes
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.user_id}', '{self.date_created}', '{self.is_admin}')"
    
    #create a new user 
    def create_user(self):
        try:
            user = User(username= self.username, email=self.email, password=self.password, user_id=str(uuid.uuid4()), date_created=date.today().strftime("%d/%m/%Y"), is_admin="False")
            session.add(user)
            session.commit()
            
            return user
        except Exception as e:
            print(e)
            session.rollback()

    # get all users
    def get_users(self):
        users = session.query(User).all()
        return users

    # get a user by id
    @classmethod
    def get_user(cls,username):
        user = session.query(User).filter_by(username=username).first()
        return user
    
conn = db.connect()
Session = sessionmaker(bind=conn)
session = Session()
Base.metadata.create_all(db)

#create table if not exists
# Base.metadata.create_all(db)


# create a new user
def create_user():
    try:
        user = User(username= "bucky", email="bucky@gmail.com", password="asdf123", user_id=str(uuid.uuid4()), date_created=date.today().strftime("%d/%m/%Y"), is_admin="False")
        session.add(user)
        session.commit()
        serialized_user = {
            "username": user.username,
            "email": user.email,
            "user_id": user.user_id,
            "date_created": user.date_created,
            "is_admin": user.is_admin
        }
        return serialized_user

    except Exception as e:
        print(e)
        session.rollback()

# # get all users
# users = session.query(User).all()
# for user in users:
#     print (user)


# # get a use   r by id
# user = session.query(User).filter_by(id=1).first()
# print(user)

print(create_user())