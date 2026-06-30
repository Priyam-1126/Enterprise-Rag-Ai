from pathlib import Path

from docx import Document
from pypdf import PdfReader


class DocumentParser:
    """Read supported document formats."""

    @staticmethod
    def read_pdf(file_path: str) -> str:
        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)

    @staticmethod
    def read_docx(file_path: str) -> str:

        document = Document(file_path)

        paragraphs = [
            paragraph.text
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]

        return "\n".join(paragraphs)

    @staticmethod
    def parse(file_path: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return DocumentParser.read_pdf(file_path)

        if extension == ".docx":
            return DocumentParser.read_docx(file_path)

        raise ValueError(f"Unsupported file type: {extension}")