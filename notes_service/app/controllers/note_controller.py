from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.schemas.note_schemas import NoteCreateRequest, NoteUpdateRequest
from app.services.note_service import NoteService

router = APIRouter()
service = NoteService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/notes")
def create_note(request: NoteCreateRequest, db: Session = Depends(get_db)):
    return service.create_note(db, request.title, request.content)


@router.get("/notes/{note_id}")
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = service.get_note(db, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return note


@router.put("/notes/{note_id}")
def update_note(note_id: int, request: NoteUpdateRequest, db: Session = Depends(get_db)):
    note = service.update_note(db, note_id, request.title, request.content)
    if note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return note


@router.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    result = service.delete_note(db, note_id)
    if result is None:
        raise HTTPException(status_code=404, detail="note not found")
    return result


@router.get("/notes/{note_id}/meta")
def get_note_meta(note_id: int, db: Session = Depends(get_db)):
    meta = service.get_note_meta(db, note_id)
    if meta is None:
        raise HTTPException(status_code=404, detail="note not found")
    return meta
