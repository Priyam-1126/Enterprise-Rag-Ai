# Enterprise RAG Assistant

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Gemini](https://img.shields.io/badge/Google-Gemini-red)

> AI-powered Enterprise Retrieval-Augmented Generation (RAG) system
> built with FastAPI, PostgreSQL + pgvector, React, Docker, and Google
> Gemini.

## Features

-   Upload PDF and DOCX documents
-   Automatic document parsing and chunking
-   Vector embeddings using BAAI Sentence Transformers
-   PostgreSQL + pgvector vector database
-   Dense + Sparse Retrieval
-   Hybrid Retrieval with Reciprocal Rank Fusion (RRF)
-   Cross-Encoder reranking
-   Gemini answer generation grounded on uploaded documents
-   React frontend for document upload and chat
-   Docker-ready backend

## Tech Stack

### Backend

-   FastAPI
-   SQLAlchemy
-   PostgreSQL
-   pgvector
-   Sentence Transformers
-   BM25
-   Google GenAI SDK

### Frontend

-   React
-   Vite
-   Axios
-   Tailwind CSS

### AI Pipeline

User Question → Query Planner → Dense Retrieval → Sparse Retrieval → RRF
→ Cross-Encoder Reranker → Gemini → Final Answer

Folder Structure

``` text
enterprise-rag/
├── app/
├── frontend/
├── data/
├── tests/
├── requirements.txt
├── docker-compose.yml
├── README.md
└── .env.example
```

## Installation

### Clone

``` bash
git clone <repository-url>
cd enterprise-rag
```

### Backend

``` bash
python -m venv .venv
```

Windows:

``` bash
.venv\Scripts\activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Create a `.env` file:

``` env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ragdb
GEMINI_API_KEY=YOUR_API_KEY
MODEL_NAME=gemini-2.5-flash
```

Run backend:

``` bash
uvicorn app.main:app --reload
```

### Frontend

``` bash
cd frontend
npm install
npm run dev
```

Open:

-   Backend: http://127.0.0.1:8000/docs
-   Frontend: http://localhost:5173

## Docker

Start services:

``` bash
docker compose up -d
```

Stop services:

``` bash
docker compose down
```

## API Endpoints

  Method   Endpoint   Description
  -------- ---------- -----------------
  POST     /upload/   Upload PDF/DOCX
  POST     /chat/     Ask a question

## Screenshots



## Future Improvements

-   Authentication
-   Conversation History
-   Streaming Responses
-   Multi-user Support
-   Admin Dashboard

## Troubleshooting

**Database connection refused**

-   Ensure Docker Desktop is running.

-   Verify PostgreSQL container is running:

    ``` bash
    docker ps
    ```

**Gemini API error**

-   Verify `GEMINI_API_KEY` in `.env`.
-   Ensure the API key is active.

## License

MIT License

## Author

**Priyam Kumar Sahu**

Final Year B.Tech (CSE/CSIT)

------------------------------------------------------------------------

If you found this project useful, consider giving it a ⭐ on GitHub.
