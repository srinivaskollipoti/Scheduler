import unittest
from unittest.mock import MagicMock, patch
from collections import deque
from service.schedule_service import SchedulingService
from cache import Cache


class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = Cache()

    def test_update_customer_queue(self):
        with patch.object(
            SchedulingService, "priority_queue", return_value=["John", "Jane"]
        ):
            self.assertEqual(self.cache.update_customer_queue(), ["John", "Jane"])

    def test_get_next_customer_with_non_empty_queue(self):
        self.cache.cached_queue = deque(["John", "Jane"])
        self.assertEqual(self.cache.get_next_customer(), "John")

    def test_get_next_customer_with_empty_queue(self):
        with patch.object(SchedulingService, "priority_queue", return_value=[]):
            self.assertIsNone(self.cache.get_next_customer())

    @patch("service.schedule_service.SchedulingService")
    def test_get_next_customer(self, mock_scheduling_service):
        mock_scheduling_service.priority_queue.return_value = deque([1, 2, 3])
        self.assertEqual(self.cache.get_next_customer(), 1)
        self.assertEqual(self.cache.get_next_customer(), 2)
        self.assertEqual(self.cache.get_next_customer(), 3)
        self.assertIsNone(self.cache.get_next_customer())
        self.assertEqual(mock_scheduling_service.priority_queue.call_count, 2)


if __name__ == "__main__":
    unittest.main()
