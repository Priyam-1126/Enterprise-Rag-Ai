from app.services.gemini_service import gemini


class AnswerGenerator:

    @staticmethod
    def generate(
        question,
        contexts,
    ):

        context = "\n\n".join(
            doc["chunk_text"]
            for doc in contexts
        )

        return gemini.answer(
            question,
            context,
        )