import unittest

from checkin.model.customer import Customer


class TestCustomer(unittest.TestCase):
    def test_init(self):
        customer = Customer("John", "Doe", "555-555-5555", True)
        self.assertEqual(customer.fname, "John")
        self.assertEqual(customer.lname, "Doe")
        self.assertEqual(customer.phone_number, "555-555-5555")
        self.assertEqual(customer.is_vip, True)

    def test_is_valid_input(self):
        customer = Customer("John", "Doe", "555-555-5555", True)
        self.assertTrue(customer.is_valid_input())
        customer = Customer("John", "Doe", "", True)
        self.assertFalse(customer.is_valid_input())
        customer = Customer("John", "", "555-555-5555", True)
        self.assertFalse(customer.is_valid_input())
        customer = Customer("", "Doe", "555-555-5555", True)
        self.assertFalse(customer.is_valid_input())
        customer = Customer("John", "Doe", "555-555-5555", None)
        self.assertFalse(customer.is_valid_input())


if __name__ == "__main__":
    unittest.main()
