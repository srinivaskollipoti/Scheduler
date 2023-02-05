import unittest
from unittest.mock import patch
import logging
from service.priority_service import PrirorityScheduler
from service.schedule_service import SchedulingService


class TestSchedulingService(unittest.TestCase):
    @patch.object(PrirorityScheduler, "fetch_waiting_jobs")
    def test_priority_queue_success(self, mock_fetch_waiting_jobs):
        mock_fetch_waiting_jobs.return_value = [
            {"VIP": True, "id": 1, "name": "A"},
            {"VIP": False, "id": 2, "name": "B"},
            {"VIP": True, "id": 3, "name": "C"},
            {"VIP": False, "id": 4, "name": "D"},
        ]

        scheduling_service = SchedulingService()
        result = scheduling_service.priority_queue()

        self.assertEqual(
            result,
            [
                {"VIP": True, "id": 1, "name": "A"},
                {"VIP": True, "id": 3, "name": "C"},
                {"VIP": False, "id": 2, "name": "B"},
                {"VIP": False, "id": 4, "name": "D"},
            ],
        )

    @patch.object(PrirorityScheduler, "fetch_waiting_jobs")
    def test_priority_queue_fetch_error(self, mock_fetch_waiting_jobs):
        mock_fetch_waiting_jobs.side_effect = Exception("Error fetching jobs")

        scheduling_service = SchedulingService()
        with self.assertRaises(Exception) as context:
            scheduling_service.priority_queue()
        self.assertEqual(str(context.exception), "Unable to retrieve the next customer")

        log_output = [
            record.message for record in logging.getLogger().handlers[0].records
        ]
        self.assertEqual(log_output, ["Error fetching jobs"])

    def test_priority_queue():
        scheduling_service = SchedulingService()
        priority_queue = scheduling_service.priority_queue()
        assert priority_queue, "The priority queue should not be empty"

    def test_priority_queue_with_no_waiting_customers():
        scheduling_service = SchedulingService()
        # Mocking `fetch_waiting_jobs` to return an empty list
        scheduling_service.priority_scheduler.fetch_waiting_jobs = lambda: []
        priority_queue = scheduling_service.priority_queue()
        assert not priority_queue, "The priority queue should be empty"


if __name__ == "__main__":
    unittest.main()
