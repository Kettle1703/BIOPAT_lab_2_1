from app.core.redis_client import redis_client


class RedisNoteRepository:
    def get_content_key(self, note_id: int):
        return f"note:{note_id}:content"

    def get_meta_key(self, note_id: int):
        return f"note:{note_id}:meta"

    def set_note_content(self, note_id: int, content: str):
        return redis_client.set(self.get_content_key(note_id), content)

    def get_note_content(self, note_id: int):
        return redis_client.get(self.get_content_key(note_id))

    def delete_note_content(self, note_id: int):
        return redis_client.delete(self.get_content_key(note_id))

    def set_note_meta(self, note_id: int, meta: dict):
        return redis_client.hset(self.get_meta_key(note_id), mapping=meta)

    def get_note_meta(self, note_id: int):
        return redis_client.hgetall(self.get_meta_key(note_id))

    def update_meta_field(self, note_id: int, field: str, value: str):
        return redis_client.hset(self.get_meta_key(note_id), field, value)

    def delete_note_meta(self, note_id: int):
        return redis_client.delete(self.get_meta_key(note_id))
