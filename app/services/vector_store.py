from sqlalchemy.orm import Session

from app.database.models import DocumentChunk
from app.services.embedding import embedding_service


class VectorStore:

    @staticmethod
    def generate_embeddings(
        db: Session,
        document_id: int,
    ) -> int:

        chunks = (
            db.query(DocumentChunk)
            .filter(DocumentChunk.document_id == document_id)
            .all()
        )

        if not chunks:
            return 0

        for chunk in chunks:
            chunk.embedding = embedding_service.encode(
                chunk.chunk_text
            )
            db.add(chunk)

        db.commit()

        return len(chunks)