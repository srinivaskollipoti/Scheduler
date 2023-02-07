import unittest

from checkin.model.customer import Customer
from checkin.service.customer_validation_service import CustomerValidationService


class TestCustomerValidationService(unittest.TestCase):
    def test_validate(self):
        validation_service = CustomerValidationService()
        customer = Customer("John", "Doe", "555-555-5555", True)

        # Test successful validation
        validation_service.cd.retrieve = lambda x: x
        result = validation_service.validate(customer)
        self.assertTrue(result)

        # Test failed validation
        validation_service.cd.retrieve = lambda x: None
        result = validation_service.validate(customer)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
