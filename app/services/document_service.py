from sqlalchemy.orm import Session

from app.database.models import Document, DocumentChunk
from app.services.vector_store import VectorStore


class DocumentService:

    @staticmethod
    def save_document(
        db: Session,
        filename: str,
        category: str,
        content: str,
        chunks: list[str],
    ):

        # Save document
        document = Document(
            filename=filename,
            category=category,
            content=content,
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        # Save chunks
        for index, chunk in enumerate(chunks):

            chunk_data = DocumentChunk(
                document_id=document.id,
                chunk_number=index + 1,
                chunk_text=chunk,
            )

            db.add(chunk_data)

        db.commit()

        # Generate embeddings for all chunks
        VectorStore.generate_embeddings(
            db=db,
            document_id=document.id,
        )

        return document