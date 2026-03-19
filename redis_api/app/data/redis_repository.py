from app.core.redis_client import redis_client


class RedisRepository:
    # STRING / INTEGER
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

    # HASH
    def set_hash(self, key: str, values: dict):
        return redis_client.hset(key, mapping=values)

    def get_hash(self, key: str):
        return redis_client.hgetall(key)

    def get_hash_field(self, key: str, field: str):
        return redis_client.hget(key, field)

    def delete_hash_field(self, key: str, field: str):
        return redis_client.hdel(key, field)

    def increment_hash_field(self, key: str, field: str, amount: int = 1):
        return redis_client.hincrby(key, field, amount)

    # LIST
    def create_list(self, key: str, values: list[str]):
        if values:
            return redis_client.rpush(key, *values)
        return 0

    def get_list(self, key: str):
        return redis_client.lrange(key, 0, -1)

    def replace_list(self, key: str, values: list[str]):
        pipe = redis_client.pipeline()
        pipe.delete(key)
        if values:
            pipe.rpush(key, *values)
        pipe.execute()
        return True

    def get_list_item(self, key: str, index: int):
        return redis_client.lindex(key, index)

    def set_list_item(self, key: str, index: int, value: str):
        return redis_client.lset(key, index, value)
