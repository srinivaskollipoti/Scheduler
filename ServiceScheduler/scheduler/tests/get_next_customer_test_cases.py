import json
import unittest

from flask import Flask
from scheduler.cache.cache_service import Cache
app = Flask(__name__)

class GetNextCustomerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_next_customer_success(self):
        # Arrange
        # set up a cache with a customer data in it

        # Act
        response = self.app.get('/v1/appointment/next')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.data))

    def test_get_next_customer_failure(self):
        # Arrange
        # set up a cache without any customer data in it
        cache = Cache()
        cache.set_customer_queue([])
        # Act
        response = self.app.get('/v1/appointment/next')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.data))
        # Act
        response = self.app.get('/v1/appointment/next')

        # Assert
        self.assertEqual(response.status_code, 500)
        self.assertEqual(str(response.data), "b'No customer found in queue'")

if __name__ == '__main__':
    unittest.main()
