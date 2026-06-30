from pathlib import Path

from docx import Document
from pypdf import PdfReader


class DocumentParser:
    """Extract text from supported document types."""

    @staticmethod
    def parse(file_path: str) -> str:
        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return DocumentParser._read_pdf(file_path)

        if extension == ".docx":
            return DocumentParser._read_docx(file_path)

        raise ValueError(f"Unsupported file type: {extension}")

    @staticmethod
    def _read_pdf(file_path: str) -> str:
        try:
            reader = PdfReader(file_path)

            text = []

            for page in reader.pages:
                try:
                    content = page.extract_text()

                    if content:
                        text.append(content)

                except Exception:
                    # Skip pages that cannot be parsed
                    continue

            result = "\n".join(text)

            if not result.strip():
                raise ValueError(
                    "No readable text found in the PDF."
                )

            return result

        except Exception as e:
            raise Exception(
                f"Failed to read PDF: {e}"
            )

    @staticmethod
    def _read_docx(file_path: str) -> str:
        try:
            document = Document(file_path)

            text = []

            for paragraph in document.paragraphs:
                if paragraph.text.strip():
                    text.append(paragraph.text)

            result = "\n".join(text)

            if not result.strip():
                raise ValueError(
                    "No readable text found in the DOCX."
                )

            return result

        except Exception as e:
            raise Exception(
                f"Failed to read DOCX: {e}"
            )