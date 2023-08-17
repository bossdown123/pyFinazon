import unittest
from finazon import Finazon

API_KEY = 'YOUR_API_KEY'  # You can also set this up using environment variables or mocking for security.

class TestFinazon(unittest.TestCase):
    def test_time_series_df(self):
        # Provide sample data for the test
        sample_data = [
            {
                't': 1629888000,  # example timestamp
                'open': 150.23,
                'high': 153.44,
                'low': 149.55,
                'close': 153.12,
                'volume': 7010200
            },
            {
                't': 1629974400,  # example timestamp
                'open': 153.00,
                'high': 155.00,
                'low': 152.00,
                'close': 154.89,
                'volume': 6910200
            }
        ]
    df = self.api._time_series_df([sample_data, sample_data], ['AAPL', 'TSLA'])
    self.assertTrue(hasattr(df, 'shape'))
    def setUp(self):
        self.api = Finazon(api_key=API_KEY)

    def test_init(self):
        self.assertIsInstance(self.api, Finazon)

    def test_send_request(self):
        # This is a basic test to see if the function is callable.
        # You can expand on this with more specific tests.
        self.assertIsNotNone(self.api._send_request("/some_endpoint"))

    def test_time_series_df(self):
        # Assuming the method returns a DataFrame
        df = self.api._time_series_df([], [])
        self.assertTrue(hasattr(df, 'shape'))

    # Add more tests for other methods similarly

if __name__ == '__main__':
    unittest.main()
