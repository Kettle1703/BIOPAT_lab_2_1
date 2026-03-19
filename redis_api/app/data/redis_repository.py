from app.core.redis_client import redis_client


class RedisRepository:
    def set_string(self, key: str, value: str):
        return redis_client.set(key, value)

    def get_string(self, key: str):
        return redis_client.get(key)

    def delete_key(self, key: str):
        return redis_client.delete(key)

    def set_expire(self, key: str, seconds: int):
        return redis_client.expire(key, seconds)

    def increment(self, key: str, amount: int = 1):
        return redis_client.incr(key, amount)
