from datetime import datetime
from app.data.note_repository import NoteRepository
from app.data.redis_note_repository import RedisNoteRepository


class NoteService:
    def __init__(self):
        self.note_repo = NoteRepository()
        self.redis_repo = RedisNoteRepository()

    def create_note(self, db, title: str, content: str):
        note = self.note_repo.create(db, title, content)

        self.redis_repo.set_note_content(note.id, note.content)
        self.redis_repo.set_note_meta(note.id, {
            "created_at": note.created_at.isoformat(),
            "updated_at": note.updated_at.isoformat(),
            "last_read_at": ""
        })

        return {
            "id": note.id,
            "title": note.title,
            "content": note.content
        }

    def get_note(self, db, note_id: int):
        note = self.note_repo.get_by_id(db, note_id)
        if note is None:
            return None

        cached_content = self.redis_repo.get_note_content(note_id)
        if cached_content is None:
            cached_content = note.content
            self.redis_repo.set_note_content(note_id, cached_content)

        last_read_at = datetime.utcnow().isoformat()
        self.redis_repo.update_meta_field(note_id, "last_read_at", last_read_at)

        meta = self.redis_repo.get_note_meta(note_id)
        if not meta:
            self.redis_repo.set_note_meta(note_id, {
                "created_at": note.created_at.isoformat(),
                "updated_at": note.updated_at.isoformat(),
                "last_read_at": last_read_at
            })

        return {
            "id": note.id,
            "title": note.title,
            "content": cached_content
        }

    def update_note(self, db, note_id: int, title: str, content: str):
        note = self.note_repo.get_by_id(db, note_id)
        if note is None:
            return None

        note.updated_at = datetime.utcnow()
        updated_note = self.note_repo.update(db, note, title, content)

        self.redis_repo.set_note_content(updated_note.id, updated_note.content)
        self.redis_repo.update_meta_field(
            updated_note.id,
            "updated_at",
            updated_note.updated_at.isoformat()
        )

        meta = self.redis_repo.get_note_meta(updated_note.id)
        if not meta:
            self.redis_repo.set_note_meta(updated_note.id, {
                "created_at": updated_note.created_at.isoformat(),
                "updated_at": updated_note.updated_at.isoformat(),
                "last_read_at": ""
            })

        return {
            "id": updated_note.id,
            "title": updated_note.title,
            "content": updated_note.content
        }

    def delete_note(self, db, note_id: int):
        note = self.note_repo.get_by_id(db, note_id)
        if note is None:
            return None

        self.note_repo.delete(db, note)
        self.redis_repo.delete_note_content(note_id)
        self.redis_repo.delete_note_meta(note_id)

        return {
            "message": "note deleted",
            "id": note_id
        }

    def get_note_meta(self, db, note_id: int):
        note = self.note_repo.get_by_id(db, note_id)
        if note is None:
            return None

        meta = self.redis_repo.get_note_meta(note_id)

        if not meta:
            meta = {
                "created_at": note.created_at.isoformat(),
                "updated_at": note.updated_at.isoformat(),
                "last_read_at": ""
            }
            self.redis_repo.set_note_meta(note_id, meta)

        return {
            "created_at": meta.get("created_at", ""),
            "updated_at": meta.get("updated_at", ""),
            "last_read_at": meta.get("last_read_at") or None
        }
