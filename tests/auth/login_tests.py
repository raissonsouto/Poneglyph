import unittest
import requests
from tests.config import HOST, PORT


class TestEndpoint(unittest.TestCase):
    def test_valid_login(self):
        response = requests.get(F'http://{HOST}:{PORT}/')
        self.assertEqual(response.status_code, 200)

    def test_login_empty_username(self):
        """
        Test error: username empty
        """
        payload = {
            "username": "joaozin",
            "email": "joaozin@mymail.com",
            "password": "dontreaditisecret",
            "phone": "+55 4002-8922"
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(f'http://{HOST}:{PORT}/', json=payload, headers=headers)

        self.assertEqual(response.status_code, 200)

        # def test_login_empty_password(self):
        # def test_login_user_or_pass_dont_match(self):
        # def test_login_not_a_json(self):


if __name__ == '__main__':
    unittest.main()
