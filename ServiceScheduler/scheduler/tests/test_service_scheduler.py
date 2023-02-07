import json
import unittest

from service.service_scheduler import ServiceScheduler


class TestServiceScheduler(unittest.TestCase):
    def setUp(self):
        """Setup method to create test data and initialize the class instance."""
        self.service_scheduler = ServiceScheduler()
        self.queue_file = self.service_scheduler.queue_file
        self.customer_data = {"vip_queue": [], "regular_queue": []}
        with open(self.queue_file, "w") as file:
            json.dump(self.customer_data, file)

    def test_add_customer(self):
        """Test add_customer method to add a customer to the queue."""
        # add a vip customer
        customer_vip = {
            "is_vip": True,
            "fname": "Joe",
            "lname": "D",
            "phone_number": "0000",
        }
        self.service_scheduler.add_customer(customer_vip)
        with open(self.queue_file) as file:
            data = json.load(file)
        self.assertEqual(len(data["vip_queue"]), 1)
        self.assertEqual(len(data["regular_queue"]), 0)
        self.assertEqual(data["vip_queue"][0], customer_vip)

        # add a regular customer
        customer_reg = {
            "is_vip": False,
            "fname": "JoeA",
            "lname": "DA",
            "phone_number": "1000",
        }
        self.service_scheduler.add_customer(customer_reg)
        with open(self.queue_file) as file:
            data = json.load(file)
        self.assertEqual(len(data["vip_queue"]), 1)
        self.assertEqual(len(data["regular_queue"]), 1)
        self.assertEqual(data["regular_queue"][0], customer_reg)

    def test_get_next_customer(self):
        """Test get_next_customer method to retrieve the next customer from the queue."""
        customer1 = {
            "is_vip": True,
            "fname": "Joe",
            "lname": "D",
            "phone_number": "0000",
        }
        customer2 = {
            "is_vip": False,
            "fname": "JoeA",
            "lname": "DA",
            "phone_number": "1000",
        }
        customer3 = {
            "is_vip": True,
            "fname": "JoeB",
            "lname": "DB",
            "phone_number": "2000",
        }
        self.service_scheduler.add_customer(customer1)
        self.service_scheduler.add_customer(customer2)
        self.service_scheduler.add_customer(customer3)

        # next_customer should be customer1
        next_customer = self.service_scheduler.get_next_customer()
        self.assertEqual(next_customer, customer1)
        with open(self.queue_file) as file:
            data = json.load(file)
        self.assertEqual(len(data["vip_queue"]), 1)
        self.assertEqual(len(data["regular_queue"]), 1)

        # next_customer should be customer3
        next_customer = self.service_scheduler.get_next_customer()
        self.assertEqual(next_customer, customer3)
        with open(self.queue_file) as file:
            data = json.load(file)
        self.assertEqual(len(data["vip_queue"]), 0)
        self.assertEqual(len(data["regular_queue"]), 1)

        # next_customer should be customer2
        next_customer = self.service_scheduler.get_next_customer()
        self.assertEqual(next_customer, customer2)
        with open(self.queue_file) as file:
            data = json.load(file)
        self.assertEqual(len(data["vip_queue"]), 0)
        self.assertEqual(len(data["regular_queue"]), 0)

        # next_customer should be None
        next_customer = self.service_scheduler.get_next_customer()
        self.assertIsNone(next_customer)


if __name__ == "__main__":
    unittest.main()
