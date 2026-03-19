from app.data.redis_repository import RedisRepository


class RedisService:
    def __init__(self):
        self.repo = RedisRepository()

    # STRING
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

    # INTEGER
    def create_or_update_integer(self, key: str, value: int):
        self.repo.set_string(key, str(value))
        return {"message": "integer saved", "key": key, "value": value}

    def get_integer(self, key: str):
        value = self.repo.get_string(key)
        if value is None:
            return {"message": "key not found", "key": key}
        return {"key": key, "value": int(value)}

    def increment_integer(self, key: str, amount: int = 1):
        value = self.repo.increment(key, amount)
        return {"key": key, "value": value}

    # HASH
    def create_or_update_hash(self, key: str, values: dict):
        self.repo.set_hash(key, values)
        return {"message": "hash saved", "key": key, "values": values}

    def get_hash(self, key: str):
        value = self.repo.get_hash(key)
        if not value:
            return {"message": "key not found", "key": key}
        return {"key": key, "values": value}

    def get_hash_field(self, key: str, field: str):
        value = self.repo.get_hash_field(key, field)
        if value is None:
            return {"message": "field not found", "key": key, "field": field}
        return {"key": key, "field": field, "value": value}

    def delete_hash(self, key: str):
        deleted = self.repo.delete_key(key)
        return {"key": key, "deleted": bool(deleted)}

    def delete_hash_field(self, key: str, field: str):
        deleted = self.repo.delete_hash_field(key, field)
        return {"key": key, "field": field, "deleted": bool(deleted)}

    def increment_hash_field(self, key: str, field: str, amount: int = 1):
        value = self.repo.increment_hash_field(key, field, amount)
        return {"key": key, "field": field, "value": value}

    # LIST
    def create_list(self, key: str, values: list[str]):
        self.repo.create_list(key, values)
        return {"message": "list created", "key": key, "values": values}

    def get_list(self, key: str):
        values = self.repo.get_list(key)
        if not values:
            return {"message": "key not found or list is empty", "key": key}
        return {"key": key, "values": values}

    def update_list(self, key: str, values: list[str]):
        self.repo.replace_list(key, values)
        return {"message": "list updated", "key": key, "values": values}

    def delete_list(self, key: str):
        deleted = self.repo.delete_key(key)
        return {"key": key, "deleted": bool(deleted)}

    def increment_list_item(self, key: str, index: int, amount: int = 1):
        current_value = self.repo.get_list_item(key, index)
        if current_value is None:
            return {"message": "list item not found", "key": key, "index": index}

        try:
            new_value = int(current_value) + amount
        except ValueError:
            return {
                "message": "list item is not integer",
                "key": key,
                "index": index,
                "value": current_value
            }

        self.repo.set_list_item(key, index, str(new_value))
        return {"key": key, "index": index, "value": new_value}
