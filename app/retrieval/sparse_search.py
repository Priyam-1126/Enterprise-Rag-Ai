from sqlalchemy import text
from sqlalchemy.orm import Session


class SparseRetriever:

    @staticmethod
    def search(
        db: Session,
        question: str,
        top_k: int = 5,
    ):

        sql = text("""
            SELECT
                id,
                chunk_number,
                chunk_text,
                ts_rank(
                    to_tsvector('english', chunk_text),
                    plainto_tsquery('english', :query)
                ) AS score
            FROM document_chunks
            WHERE to_tsvector('english', chunk_text)
                  @@ plainto_tsquery('english', :query)
            ORDER BY score DESC
            LIMIT :top_k;
        """)

        result = db.execute(
            sql,
            {
                "query": question,
                "top_k": top_k,
            },
        )

        return result.mappings().all()