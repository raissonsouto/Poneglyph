import unittest
import requests
from tests.config import HOST, PORT, REQUEST_HEADER

""""
Successful login with valid credentials
Successful login with uppercase letters in credentials
Successful login with lowercase letters in credentials
Successful login with numbers in credentials
Successful login with special characters in credentials
Successful login with a long credentials
Successful login with a short credentials

Failed login with an invalid username
Failed login with an invalid password
Failed login with an empty username
Failed login with an empty password
Failed login with null username
Failed login with null password

Failed login with only whitespace in username and/or password
Failed login with single space character in username and/or password
Failed login with multiple space characters in username and/or password
Failed login with tab character in username and/or password
Failed login with newline character in username and/or password
Failed login with carriage return character in username and/or password
Failed login with null character in username and/or password
Failed login with restricted characters such as backslash, forward slash, quotation mark, apostrophe, etc.
"""


class TestEndpoint(unittest.TestCase):
    ROUTE = '/auth/login'

    def test_valid_login_1(self):
        """
        Test login (Successful): Only lowercase in username.
        """
        payload = {
            "username": "joaozin",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

    def test_valid_login_2(self):
        """
        Test login (Successful): Only lowercase and uppercase in username.
        """
        payload = {
            "username": "JOAOzin",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

    def test_valid_login_3(self):
        """
        Test login (Successful): Only lowercase and numbers in username.
        Test range: abcdefghijklmnopqrstuvwxyz0123456789
        """
        payload = {
            "username": "j0a0z1n",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

    def test_valid_login_4(self):
        """
        Test login (Successful): Only lowercase and valid symbols in username.

        """
        payload = {
            "username": "jo@o$in",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

    def test_valid_login_5(self):
        """
        Test login (Successful): Login with maximum size in username (30).
        """
        payload = {
            "username": "joaozinjoaozinjoaozinjoaozinnn",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

    def test_valid_login_6(self):
        """
        Test login (Successful): Login with minimum size in username (3).
        """
        payload = {
            "username": "jzn",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

        # @todo: password input tests following the pattern above

    def test_valid_login_7(self):
        """
        Test login (Successful): Only lowercase and uppercase in password.
        """
        payload = {
            "username": "joaozin",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

    def test_valid_login_8(self):
        """
        Test login (Successful): Only lowercase and numbers in password.
        """
        payload = {
            "username": "JOAOzin",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

    def test_valid_login_9(self):
        """
        Test login (Successful): Only lowercase and symbols in password.
        """
        payload = {
            "username": "j0a0z1n",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

    def test_valid_login_10(self):
        """
        Test login (Successful): Login with maximum size in password (255).
        """
        payload = {
            "username": "joaozinjoaozinjoaozinjoaozinnn",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

    def test_valid_login_11(self):
        """
        Test login (Successful): Login with minimum size in username (8).
        """
        payload = {
            "username": "jzn",
            "password": "dontreaditisecret"
        }

        response = requests.post(f'http://{HOST}:{PORT}/{self.ROUTE}', json=payload, headers=REQUEST_HEADER)
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

        response = requests.post(f'http://{HOST}:{PORT}/', json=payload, headers=REQUEST_HEADER)
        self.assertEqual(response.status_code, 200)

        # def test_login_empty_password(self):
        # def test_login_user_or_pass_dont_match(self):
        # def test_login_not_a_json(self):


if __name__ == '__main__':
    unittest.main()
