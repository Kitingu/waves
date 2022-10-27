from .test_app import TestApp
import json


class TestUser(TestApp):

    def test_sign_up(self):
        resp = self.client.post('/signup', data=json.dumps({
            "username": "benedict",
            "email": "ben@gmail.com",
            "password": "nqis@beS_22"
        }),content_type='application/json')
        self.assertEqual(resp.status_code, 201)

        resp = self.client.post('/signup', data=json.dumps({
            "email": "ben@gmail.com",
            "password": "nis@beS_22"
        }), content_type='application/json')
        self.assertEqual(resp.status_code, 400)

    def test_login(self):
        resp = self.client.post('/login', data=json.dumps({
            "username": "benedict",
            "password": "niqs@beS_22"
        }), content_type='application/json')
        self.assertEqual(resp.status_code, 400)

        resp = self.client.post('/login', data=json.dumps({
            "password": "niqs@beS_22"
        }), content_type='application/json')
        self.assertEqual(resp.status_code, 400)
