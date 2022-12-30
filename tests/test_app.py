import unittest, json
from app import create_app
from config.config import app_config
from flask import current_app

from app import db

class TestApp(unittest.TestCase):

    def setUp(self):
        config_name = "testing"
        self.app = create_app(app_config[config_name])
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        
            

        self.test_user = {
            "username": "benedict",
            "email": "ben@gmail.com",
            "password": "nqis@beS_22"
        }
        self.user_login ={
            "username": "benedict",
            "password": "nqis@beS_22"
        }
        self.user = self.client.post('/users', data=json.dumps(self.test_user),
                                     content_type='application/json')
        green = self.client.post('/login', data=json.dumps({
            "username": "benedict",
            "password": "nqis@beS_22"
        }), content_type='application/json')
        print(green)

    def register(self):
        resp = self.client.post('/users', data=json.dumps(self.test_user),
                                     content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        respo = self.client.post('/login', data=json.dumps({
            "username": "benedict",
            "password": "nqis@beS_22"
        }), content_type='application/json')
        # self.assertEqual(respo.status_code,200)

    def test_app(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data.decode(), "Hello World!")

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


if(__name__ == "__main__"):
    unittest.main(verbosity=2)