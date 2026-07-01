from sentence_transformers import CrossEncoder


class Reranker:
    def __init__(self):
        self.model = None

    def _get_model(self):
        if self.model is None:
            self.model = CrossEncoder(
                "cross-encoder/ms-marco-MiniLM-L-6-v2"
            )
        return self.model

    def rerank(self, question, documents):
        docs = [dict(doc) for doc in documents]

        pairs = [
            (question, doc["chunk_text"])
            for doc in docs
        ]

        scores = self._get_model().predict(pairs)

        for doc, score in zip(docs, scores):
            doc["rerank_score"] = float(score)

        docs.sort(
            key=lambda x: x["rerank_score"],
            reverse=True,
        )

        return docs


reranker = Reranker()