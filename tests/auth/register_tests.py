import unittest
import requests
from tests.config import HOST, PORT


class TestEndpoint(unittest.TestCase):
    def test_valid_registration_with_phone(self):

        payload = {
            "username": "joaozin",
            "email": "joaozin@mymail.com",
            "password": "dontreaditisecret",
            "phone": "+55 4002-8922"
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(f'http://{HOST}:{PORT}/', json=payload, headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_valid_registration_without_phone(self):

        payload = {
            "username": "joaozin",
            "email": "joaozin@mymail.com",
            "password": "dontreaditisecret"
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(f'http://{HOST}:{PORT}/', json=payload, headers=headers)

        self.assertEqual(response.status_code, 200)

    def test_registration_empty_username(self):
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

    def test_registration_user_already_exist(self):
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

        # def test_registration_request_body_is_not_a_json(self):
        # def test_registration_user_already_exist(self):


if __name__ == '__main__':
    unittest.main()
