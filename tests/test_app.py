import unittest, json
from app import app
from app.models.user import db as user_db
from app.models.wave import waves_db


class TestApp(unittest.TestCase):

    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()
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
        self.ctx.pop()
        waves_db.clear()
        user_db.clear()

if(__name__ == "__main__"):
    unittest.main(verbosity=2)