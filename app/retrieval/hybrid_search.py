from app.retrieval.dense_search import DenseRetriever
from app.retrieval.sparse_search import SparseRetriever


class HybridRetriever:

    @staticmethod
    def search(
        db,
        question,
        top_k=5,
    ):

        dense = DenseRetriever.search(
            db,
            question,
            top_k,
        )

        sparse = SparseRetriever.search(
            db,
            question,
            top_k,
        )

        return {
            "dense": dense,
            "sparse": sparse,
        }