from pydantic import BaseModel


class NoteCreateRequest(BaseModel):
    title: str
    content: str


class NoteUpdateRequest(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str


class NoteMetaResponse(BaseModel):
    created_at: str
    updated_at: str
    last_read_at: str | None = None
