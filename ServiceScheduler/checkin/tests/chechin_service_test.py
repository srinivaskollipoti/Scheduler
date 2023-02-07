import unittest

from checkin.model.customer import Customer
from checkin.service.checkin_service import CheckinService


class TestCheckinService(unittest.TestCase):
    def test_checkin(self):
        checkin_service = CheckinService()
        customer = Customer("John", "Doe", "555-555-5555", True)

        # Test successful checkin
        checkin_service.cr.save_and_retrieve = lambda x: 1
        result = checkin_service.checkin(customer)
        self.assertEqual(result, 1)

        # Test failed checkin
        checkin_service.cr.save_and_retrieve = lambda x: None
        result = checkin_service.checkin(customer)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
