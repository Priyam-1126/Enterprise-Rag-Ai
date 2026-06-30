from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Generates vector embeddings for text using
    BAAI/bge-small-en-v1.5
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def encode(self, text: str) -> list[float]:
        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def encode_batch(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
        )

        return embeddings.tolist()


embedding_service = EmbeddingService()