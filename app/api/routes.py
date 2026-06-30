from fastapi import APIRouter
from sqlalchemy import text

from app.database.db import engine

router = APIRouter(tags=["System"])


@router.get("/")
async def home():
    return {
        "application": "Enterprise Knowledge Assistant",
        "version": "1.0.0",
        "status": "Running",
    }


@router.get("/health")
async def health():
    return {
        "status": "Healthy",
    }


@router.get("/database")
async def database():

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "Connected",
        }

    except Exception as error:
        return {
            "database": "Disconnected",
            "error": str(error),
        }