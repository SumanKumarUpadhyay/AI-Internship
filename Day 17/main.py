import os
import shutil

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from pipeline import process_pdf, ask_question

app = FastAPI(title="Basic RAG API")

# Upload Folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Request Model
class QuestionRequest(BaseModel):
    question: str


# Upload PDF
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    process_pdf(file_path)

    return {
        "message": "PDF uploaded successfully."
    }


# Ask Question
@app.post("/chat")
async def chat(request: QuestionRequest):

    answer = ask_question(request.question)

    return {
        "answer": answer
    }