from sqlalchemy.orm import Session
from sqlalchemy import text

from app.services.embedding import embedding_service


class DenseRetriever:

    @staticmethod
    def search(
        db: Session,
        question: str,
        top_k: int = 5,
    ):

        embedding = embedding_service.encode(question)

        vector = "[" + ",".join(map(str, embedding)) + "]"

        query = text("""
            SELECT
                id,
                chunk_number,
                chunk_text,
                embedding <=> CAST(:embedding AS vector) AS distance
            FROM document_chunks
            WHERE embedding IS NOT NULL
            ORDER BY embedding <=> CAST(:embedding AS vector)
            LIMIT :top_k
        """)

        result = db.execute(
            query,
            {
                "embedding": vector,
                "top_k": top_k,
            },
        )

        return result.mappings().all()