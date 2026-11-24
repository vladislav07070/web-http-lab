from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

notes = []
next_id = 1


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=80)
    content: str = Field(..., min_length=1, max_length=500)


@app.get("/")
def home_page():
    return {"message": "do smth"}


@app.get("/hello")
def read_hello():
    return {"message": "Hello from Notes API"}


@app.get("/health")
def return_health():
    return {"status": "ok"}


@app.get("/notes")
def return_notes():
    return notes


@app.post("/notes", status_code=201)
def add_new_note(note: NoteCreate):
    global next_id
    new_note = {"id": next_id, "title": note.title, "content": note.content}
    notes.append(new_note)
    next_id += 1
    return new_note
