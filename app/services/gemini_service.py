import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = os.getenv(
            "MODEL_NAME",
            "gemini-2.5-flash",
        )

    def answer(
        self,
        question: str,
        context: str,
    ):

        prompt = f"""
You are an Enterprise AI Assistant.

Answer ONLY from the provided context.

If the answer is not available in the context, reply exactly:

"I couldn't find this information in the uploaded enterprise documents."

Instructions:

Instructions:

- Answer ONLY using the provided context.
- Never use outside knowledge.
- Write the answer using Markdown.
- Start with a short summary.
- Use ## headings.
- Use bullet points where appropriate.
- Use numbered steps for procedures.
- Highlight important keywords using **bold**.
- Keep the answer clear and professional.
- If the answer is not found in the context, reply exactly:
"I couldn't find this information in the uploaded enterprise documents."
Context:
{context}

Question:
{question}
Answer:
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text


gemini = GeminiService()