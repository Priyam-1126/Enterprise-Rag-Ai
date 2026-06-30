# Enterprise RAG AI Assistant - Complete Setup Guide

This guide explains how to run the Enterprise RAG AI Assistant on any Windows machine from scratch.

---

# Project Requirements

Before running the project, install the following software:

- Python 3.12.10
- Node.js (LTS Version)
- Git
- Docker Desktop (Optional - only for local PostgreSQL)
- VS Code (Recommended)

Verify installation:

```bash
python --version
node -v
npm -v
git --version
```

---

# Clone the Repository

```bash
git clone https://github.com/Priyam-1126/Enterprise-Rag-Ai.git

cd Enterprise-Rag-Ai
```

---

# Backend Setup

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

---

## Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Verify

```bash
pip check
```

Expected output

```
No broken requirements found.
```

---

# Environment Variables

Copy

```
.env.example
```

to

```
.env
```

Example

```env
DATABASE_URL=YOUR_DATABASE_URL
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
MODEL_NAME=gemini-2.5-flash
```

Never commit your real .env file.

---

# Database

## Option 1 (Recommended)

Use Neon PostgreSQL.

Paste your Neon DATABASE_URL into .env.

---

## Option 2

Run PostgreSQL locally.

Docker

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

---

# Run Backend

Normal

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 9000
```

API Documentation

```
http://127.0.0.1:9000/docs
```

Health Check

```
http://127.0.0.1:9000/health
```

---

# Frontend Setup

Open another terminal.

```bash
cd frontend
```

Install packages

```bash
npm install
```

Run

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# Complete Startup Order

1. Activate Virtual Environment

```bash
.venv\Scripts\activate
```

2. Start Backend

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 9000
```

3. Open another terminal

```bash
cd frontend
```

4. Install

```bash
npm install
```

5. Start Frontend

```bash
npm run dev
```

6. Open

```
http://localhost:5173
```

---

# Testing

Upload

- PDF
- DOCX

Ask

```
Summarize this document.
```

Expected

A document summary.

Ask

```
What is the leave policy?
```

Expected

Answer from uploaded document.

Ask

```
Who is the President of Mars?
```

Expected

```
I couldn't find this information in the uploaded enterprise documents.
```

---

# Common Errors

## ModuleNotFoundError

Example

```
ModuleNotFoundError: No module named 'langchain_text_splitters'
```

Solution

```bash
pip install -r requirements.txt
```

---

## Upload Failed

Possible Reasons

- Backend not running
- Wrong API URL
- Invalid .env

Verify backend

```
http://127.0.0.1:9000/docs
```

---

## Chat Failed

Possible Reasons

- Gemini API Key missing
- Empty Database
- Upload failed

Verify

```
GEMINI_API_KEY
DATABASE_URL
```

---

## WinError 10013

Port 8000 is blocked.

Run backend on

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 9000
```

Also update frontend API URL

```
http://127.0.0.1:9000
```

---

## Docker Error

Restart Docker Desktop.

Run

```bash
docker compose up -d
```

---

# Install New Dependency

```bash
pip install package_name
```

Update

```
requirements.txt
```

Commit

```bash
git add .
git commit -m "Add dependency"
git push
```

---

# Git Commands

Clone

```bash
git clone <repository-url>
```

Status

```bash
git status
```

Pull

```bash
git pull
```

Push

```bash
git add .
git commit -m "message"
git push
```

---

# Deployment

Backend

Render

Frontend

Vercel

Database

Neon PostgreSQL

---

# Tech Stack

Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- pgvector

Frontend

- React
- Axios
- Tailwind CSS

AI

- Google Gemini
- Sentence Transformers
- Cross Encoder
- Hybrid Search
- BM25
- Reciprocal Rank Fusion

---

# Project Structure

```
Enterprise-Rag-Ai
│
├── app
├── frontend
├── tests
├── data
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── runtime.txt
├── README.md
├── .env.example
├── .gitignore
└── SETUP_GUIDE.md
```

---

# Maintainer

Priyam Kumar Sahu

GitHub

https://github.com/Priyam-1126/Enterprise-Rag-Ai