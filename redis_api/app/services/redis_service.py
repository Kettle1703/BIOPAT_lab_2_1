from app.data.redis_repository import RedisRepository


class RedisService:
    def __init__(self):
        self.repo = RedisRepository()

    def create_or_update_string(self, key: str, value: str):
        self.repo.set_string(key, value)
        return {"message": "string saved", "key": key, "value": value}

    def get_string(self, key: str):
        value = self.repo.get_string(key)
        if value is None:
            return {"message": "key not found", "key": key}
        return {"key": key, "value": value}

    def delete_key(self, key: str):
        deleted = self.repo.delete_key(key)
        return {"key": key, "deleted": bool(deleted)}

    def expire_key(self, key: str, seconds: int):
        result = self.repo.set_expire(key, seconds)
        return {"key": key, "expire_set": bool(result), "seconds": seconds}

    def increment_key(self, key: str, amount: int = 1):
        value = self.repo.increment(key, amount)
        return {"key": key, "value": value}
