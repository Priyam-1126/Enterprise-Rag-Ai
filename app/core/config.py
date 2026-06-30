from pathlib import Path

from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")


class Settings:
    APP_NAME = "Enterprise Knowledge Assistant"
    APP_VERSION = "1.0.0"

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/ragdb",
    )

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


settings = Settings()