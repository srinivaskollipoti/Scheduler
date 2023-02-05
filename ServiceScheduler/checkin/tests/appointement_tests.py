import unittest
from flask import Flask
from service.checkin_service import CheckinService
from service.customer_validation_service import CustomerValidationService

PERMITTED_TYPES = ["application/json"]

app = Flask(__name__)
customer_service = CustomerValidationService()
checkin_service = CheckinService()

class TestCreateAppointment(unittest.TestCase):

    def test_create_appointment_invalid_content_type(self):
        client = app.test_client()
        response = client.post(
            "/v1/appointments", json={}, headers={"CONTENT_TYPE": "application/dummy"}
        )

        self.assertEqual(response.status_code, 400)

    def test_create_appointment_empty_input(self):
        client = app.test_client()
        input = {
            "firstName": "",
            "lastName": "",
            "phoneNumber": "",
            "is_vip": "",
        }
        response = client.post("/v1/appointments", json=input)

        self.assertEqual(response.status_code, 400)
    def test_create_appointment_valid_input(self):
        client = app.test_client()
        input = {
            "firstName": "John",
            "lastName": "Doe",
            "phoneNumber": "+1 123 123 1234",
            "is_vip": False,
        }
        response = client.post("/v1/appointments", json=input)

        self.assertEqual(response.status_code, 201)

    def test_create_appointment_with_existing_phone_number(self):
        client = app.test_client()
        input = {
            "firstName": "Jane",
            "lastName": "Doe",
            "phoneNumber": "+1 123 123 1234",
            "is_vip": True,
        }
        response = client.post("/v1/appointments", json=input)

        self.assertEqual(response.status_code, 409)

    def test_create_appointment_without_required_fields(self):
        client = app.test_client()
        input = {
            "firstName": "Jane",
            "lastName": "",
            "phoneNumber": "+1 123 123 1234",
        }
        response = client.post("/v1/appointments", json=input)

        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
