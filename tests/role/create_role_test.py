import unittest
import requests
from tests.config import HOST, PORT


class TestEndpoint(unittest.TestCase):
    def test_valid_login(self):
        response = requests.get(F'http://{HOST}:{PORT}/')
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = requests.get(F'http://{HOST}:{PORT}/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
