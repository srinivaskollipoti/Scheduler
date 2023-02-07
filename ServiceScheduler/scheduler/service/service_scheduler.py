import json
from cache.redis_client import RedisClient

EMPTY_QUEUE = '{"vip_queue": [], "regular_queue": []}'


class ServiceScheduler:
    """Class for scheduling appointments based on priority.

    Attributes:
        vip_count (int): Number of consecutive VIP customers serviced so far.
        redis_client (RedisClient): Redis client instance.
    """

    def __init__(self) -> None:
        """Constructor to initialize required components."""
        self.vip_count = 0
        self.redis_client = RedisClient()

    def add_customer(self, customer: dict):
        """Add a customer to the queue.

        Args:
            customer (dict): Customer information with keys 'is_vip' and other details.
        """
        data = json.loads(self.redis_client.get_data("queue") or EMPTY_QUEUE)

        if customer["is_vip"]:
            data["vip_queue"].append(customer)
        else:
            data["regular_queue"].append(customer)

        self.redis_client.set_data("queue", json.dumps(data))

    def get_next_customer(self) -> dict:
        """Return the next customer to be serviced.

        Returns:
            dict: Customer information or None if there's no customer in queue.
        """
        data = json.loads(self.redis_client.get_data("queue") or EMPTY_QUEUE)

        if data["vip_queue"] and self.vip_count < 2:
            self.vip_count += 1
            next_cust = data["vip_queue"].pop(0)
        elif data["regular_queue"]:
            self.vip_count = 0
            next_cust = data["regular_queue"].pop(0)
        elif data["vip_queue"]:
            next_cust = data["vip_queue"].pop(0)
        else:
            next_cust = None

        self.redis_client.set_data("queue", json.dumps(data or EMPTY_QUEUE))

        return next_cust
