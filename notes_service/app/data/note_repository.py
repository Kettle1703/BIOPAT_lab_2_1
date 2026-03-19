from sqlalchemy.orm import Session
from app.models.note_model import Note


class NoteRepository:
    def create(self, db: Session, title: str, content: str):
        note = Note(title=title, content=content)
        db.add(note)
        db.commit()
        db.refresh(note)
        return note

    def get_by_id(self, db: Session, note_id: int):
        return db.query(Note).filter(Note.id == note_id).first()

    def update(self, db: Session, note, title: str, content: str):
        note.title = title
        note.content = content
        db.commit()
        db.refresh(note)
        return note

    def delete(self, db: Session, note):
        db.delete(note)
        db.commit()
