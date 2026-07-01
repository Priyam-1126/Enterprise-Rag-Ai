from fastapi import FastAPI

from app.api.routes import router
from app.api.upload import router as upload_router
from app.core.config import settings
from app.database.db import Base, engine
from app.api.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "Enterprise RAG API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

