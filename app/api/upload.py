from pathlib import Path
import shutil

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.services.chunker import DocumentChunker
from app.services.document_service import DocumentService
from app.services.parser import DocumentParser

router = APIRouter(
    prefix="/upload",
    tags=["Documents"],
)

UPLOAD_DIRECTORY = Path("data/documents")
UPLOAD_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True,
)


@router.post("/")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    extension = Path(file.filename).suffix.lower()

    if extension not in [".pdf", ".docx"]:

        raise HTTPException(
            status_code=400,
            detail="Unsupported document type.",
        )

    destination = UPLOAD_DIRECTORY / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer,
        )

    text = DocumentParser.parse(
        str(destination)
    )

    chunker = DocumentChunker()

    chunks = chunker.split(text)

    document = DocumentService.save_document(
        db=db,
        filename=file.filename,
        category="General",
        content=text,
        chunks=chunks,
    )

    return {

        "message": "Upload Successful",

        "document_id": document.id,

        "chunks": len(chunks),

        "filename": file.filename,
    }