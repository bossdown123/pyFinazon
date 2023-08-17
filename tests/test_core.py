import unittest
from finazon import Finazon

API_KEY = 'YOUR_API_KEY'  # You can also set this up using environment variables or mocking for security.

class TestFinazon(unittest.TestCase):

    def setUp(self):
        self.api = Finazon(api_key=API_KEY)

    def test_init(self):
        self.assertIsInstance(self.api, Finazon)

    def test_send_request(self):
        # This is a basic test to see if the function is callable.
        # You can expand on this with more specific tests.
        self.assertIsNotNone(self.api._send_request("/some_endpoint"))

    # Add more tests for other methods similarly

if __name__ == '__main__':
    unittest.main()
