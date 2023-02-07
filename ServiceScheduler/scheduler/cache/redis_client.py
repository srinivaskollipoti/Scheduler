import redis


class RedisClient:
    def __init__(self):
        self.redis_instance = redis.Redis(host="redis", port=6379, db=0)

    def get_data(self, key: str):
        return self.redis_instance.get(key)

    def set_data(self, key: str, value):
        self.redis_instance.set(key, value)
