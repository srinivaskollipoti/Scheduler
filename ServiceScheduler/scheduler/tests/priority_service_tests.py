import unittest
from collections import deque
from scheduler.dao.appointment_dao import AppointmentDao
from scheduler.service.priority_service import PrirorityScheduler


class TestPriorityScheduler(unittest.TestCase):
    def setUp(self):
        self.priority_scheduler = PrirorityScheduler()
        self.appointment = AppointmentDao()

    def test_process_queue(self):
        customer_list = [
            {"VIP": False, "name": "John Doe"},
            {"VIP": True, "name": "Jane Doe"},
            {"VIP": False, "name": "Jim Doe"},
            {"VIP": True, "name": "Joan Doe"},
            {"VIP": False, "name": "Jake Doe"},
        ]

        expected_result = deque(
            [
                {"VIP": True, "name": "Jane Doe"},
                {"VIP": True, "name": "Joan Doe"},
                {"VIP": False, "name": "John Doe"},
                {"VIP": False, "name": "Jim Doe"},
                {"VIP": False, "name": "Jake Doe"},
            ]
        )

        result = self.priority_scheduler.process_queue(customer_list)
        self.assertEqual(result, expected_result)

    def test_fetch_waiting_jobs(self):
        scheduler = PrirorityScheduler()
        waiting_jobs = scheduler.fetch_waiting_jobs()
        self.assertIsInstance(waiting_jobs, list)

    def test_process_queue(self):
        scheduler = PrirorityScheduler()
        customers = [
            {"id": 1, "name": "A", "VIP": True},
            {"id": 2, "name": "B", "VIP": False},
            {"id": 3, "name": "C", "VIP": True},
            {"id": 4, "name": "D", "VIP": False},
        ]
        priority_queue = scheduler.process_queue(customers)
        self.assertEqual(len(priority_queue), 4)
        self.assertEqual(priority_queue[0]["id"], 1)
        self.assertEqual(priority_queue[1]["id"], 3)
        self.assertEqual(priority_queue[2]["id"], 2)
        self.assertEqual(priority_queue[3]["id"], 4)

    def test_process_queue_with_empty_list(self):
        scheduler = PrirorityScheduler()
        customers = []
        priority_queue = scheduler.process_queue(customers)
        self.assertEqual(len(priority_queue), 0)


if __name__ == "__main__":
    unittest.main()
