from app.services.embedding import embedding_service


def test_embedding():

    vector = embedding_service.encode(
        "Enterprise RAG"
    )

    assert len(vector) == 384

    print("✅ Embedding Test Passed")


if __name__ == "__main__":
    test_embedding()