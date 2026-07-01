from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self):
        self.model = None

    def _get_model(self):
        if self.model is None:
            self.model = SentenceTransformer(
                "BAAI/bge-small-en-v1.5"
            )
        return self.model

    def encode(self, text: str):
        model = self._get_model()
        return model.encode(
            text,
            normalize_embeddings=True,
        ).tolist()

    def encode_batch(self, texts):
        model = self._get_model()
        return model.encode(
            texts,
            normalize_embeddings=True,
        ).tolist()


embedding_service = EmbeddingService()