from datetime import timedelta

import redis

data_expire_time = 60


class RedisDB:
    def __init__(self):
        self.redis_db = redis.Redis(host="localhost", port=6379, db=1)

    def post(self, key, value, expiration_time: int = 168):
        return self.redis_db.setex(name=key, value=value, time=timedelta(hours=expiration_time))

    def get(self, key):
        return self.redis_db.get(name=key)
