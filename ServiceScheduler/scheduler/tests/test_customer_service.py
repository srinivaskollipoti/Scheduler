import unittest
from unittest.mock import patch

from scheduler.customer_service import app, service_scheduler


class GetNextCustomerTestCase(unittest.TestCase):
    def setUp(self):
        # Creates a test client
        self.client = app.test_client()

    @patch.object(service_scheduler, "get_next_customer")
    def test_get_next_customer_success(self, mock_get_next_customer):
        # Mocks the get_next_customer method to return a customer
        mock_get_next_customer.return_value = {
            "is_vip": False,
            "fname": "Joe",
            "lname": "D",
            "phone_number": "0000",
        }

        # Sends a GET request to the API endpoint
        response = self.client.get("/v1/appointment/next")

        # Asserts that the response has a status code of 200 and the returned customer is as expected
        self.assertEqual(response.status_code, 200)

    @patch.object(service_scheduler, "get_next_customer")
    def test_get_next_customer_success(self, mock_get_next_customer):
        # Mocks the get_next_customer method to return None
        mock_get_next_customer.return_value = None

        # Sends a GET request to the API endpoint
        response = self.client.get("/v1/appointment/next")

        # Asserts that the response has a status code of 200 and the returned customer is as expected
        self.assertEqual(response.status_code, 200)

    @patch.object(service_scheduler, "get_next_customer")
    def test_get_next_customer_error(self, mock_get_next_customer):
        # Mocks the get_next_customer method to raise a general exception
        mock_get_next_customer.side_effect = Exception("Some error")

        # Sends a GET request to the API endpoint
        response = self.client.get("/v1/appointment/next")

        # Asserts that the response has a status code of 500 and the error message is as expected
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, b"Some error")


if __name__ == "__main__":
    unittest.main()
