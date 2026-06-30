from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):
        self.model = CrossEncoder(
            "BAAI/bge-reranker-base"
        )

    def rerank(
        self,
        question,
        documents,
    ):

        # Convert RowMapping -> dict
        docs = [dict(doc) for doc in documents]

        pairs = [
            (
                question,
                doc["chunk_text"],
            )
            for doc in docs
        ]

        scores = self.model.predict(pairs)

        for doc, score in zip(docs, scores):
            doc["rerank_score"] = float(score)

        docs.sort(
            key=lambda x: x["rerank_score"],
            reverse=True,
        )

        return docs


reranker = Reranker()