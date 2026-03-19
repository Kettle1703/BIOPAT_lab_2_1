from fastapi import FastAPI
from app.core.db import Base, engine
from app.models.note_model import Note
from app.controllers.note_controller import router as note_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes Service")

app.include_router(note_router)
