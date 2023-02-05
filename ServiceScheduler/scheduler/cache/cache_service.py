from collections import deque

from service.schedule_service import SchedulingService


class Cache:
    """
    A class to manage a cache of customer data.

    Attributes:
        cached_queue (deque): A double-ended queue to store customer data.
        next_customer (object): The next customer to be served.
        scheduler (SchedulingService): An instance of the `SchedulingService` class.

    """

    def __init__(self) -> None:
        """
        Initializes the cache and creates an instance of the `SchedulingService` class.
        """
        self.cached_queue = deque()
        self.next_customer = None
        self.scheduler = SchedulingService()

    def update_customer_queue(self):
        """
        Updates the customer queue using the `priority_queue` method of the `SchedulingService` class.

        Returns:
            list: A list of customer data.
        """
        return self.scheduler.priority_queue()

    def get_next_customer(self):
        """
        Returns the next customer in the cache.

        If the cache is empty, it updates the customer queue using the `update_customer_queue` method.
        If the updated queue is still empty, `None` is returned.

        Returns:
            object or None: The next customer, or `None` if the cache is empty.
        """
        if not self.cached_queue:
            self.cached_queue = self.update_customer_queue()

        if self.cached_queue:
            self.next_customer = self.cached_queue.popleft()
            return self.next_customer
        else:
            return None
