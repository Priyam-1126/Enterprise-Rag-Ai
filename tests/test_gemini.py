from app.services.gemini_service import gemini


def test_gemini():

    response = gemini.answer(
        question="What is AI?",
        context="Artificial Intelligence (AI) is the simulation of human intelligence by machines."
    )

    print("\n===== Gemini Response =====\n")
    print(response)


if __name__ == "__main__":
    test_gemini()