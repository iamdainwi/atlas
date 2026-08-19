# Atlas

> **An AI-powered Personal Document Library built using Naive Retrieval-Augmented Generation (Naive RAG).**

Atlas allows users to upload documents, build a searchable knowledge base, and interact with their information through natural language conversations powered by Large Language Models.

---

## Overview

Atlas demonstrates how a production-grade **Naive Retrieval-Augmented Generation (RAG)** system is designed and implemented.

Instead of answering questions solely from an LLM's internal knowledge, Atlas retrieves relevant information from user-uploaded documents and provides grounded, source-backed responses.

The project is designed as a learning resource, portfolio project, and foundation for advanced RAG architectures such as Hybrid RAG, Graph RAG, and Agentic RAG.

---

## Key Features

### Authentication

- JWT Authentication
- Secure Password Hashing
- Refresh Tokens
- User Profiles

---

### Document Management

- Upload Documents
- Rename Documents
- Delete Documents
- Download Original Files
- Document Preview
- Search & Filter

---

### Supported File Formats

- PDF
- DOCX
- TXT
- Markdown (.md)

---

### Document Processing

- Text Extraction
- Text Cleaning
- Intelligent Chunking
- Metadata Generation
- Background Processing

---

### Embeddings

- Sentence Transformer Embeddings
- Configurable Embedding Models
- Batch Processing

---

### Semantic Retrieval

- Vector Similarity Search
- Top-K Retrieval
- Metadata Filtering
- Source Citation

---

### AI Chat

- Natural Language Questions
- Streaming Responses
- Markdown Rendering
- Conversation History
- Source References

---

### User Experience

- Responsive UI
- Dark & Light Theme
- Dashboard
- Document Library
- Chat Workspace
- Settings Panel

---

# Architecture

Atlas follows a layered architecture built on Clean Architecture principles.

```text
                    Frontend

                 (Next.js + React)

                        │

                        ▼

                 FastAPI REST API

                        │

        ┌───────────────┼────────────────┐

        ▼               ▼                ▼

Authentication   Document Service   Chat Service

        │               │                │

        ▼               ▼                ▼

 Processing → Embedding → Retrieval → Prompt

                        │

        ┌───────────────┼────────────────┐

        ▼               ▼                ▼

 PostgreSQL       ChromaDB       Local Storage

                        │

                        ▼

                 Large Language Model
```

---

# Naive RAG Pipeline

```text
Upload Document

↓

Validate

↓

Extract Text

↓

Clean Text

↓

Chunk Document

↓

Generate Embeddings

↓

Store in ChromaDB

↓

User Question

↓

Generate Query Embedding

↓

Similarity Search

↓

Retrieve Top-K Chunks

↓

Prompt Construction

↓

LLM

↓

Grounded Response
```

---

# Technology Stack

## Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- Zustand
- TanStack Query

---

## Backend

- FastAPI
- Python
- SQLAlchemy
- Alembic
- Pydantic

---

## Databases

- PostgreSQL
- ChromaDB

---

## AI

- Sentence Transformers
- Gemini
- OpenAI
- Claude
- Ollama
- OpenRouter

---

## DevOps

- Docker
- Docker Compose
- Nginx

---

# Project Structure

```text
atlas/

├── backend/

│   ├── api/

│   ├── core/

│   ├── models/

│   ├── repositories/

│   ├── services/

│   ├── workers/

│   └── tests/

│

├── frontend/

│   ├── app/

│   ├── components/

│   ├── hooks/

│   ├── services/

│   └── styles/

│

├── docs/

│

├── storage/

│

├── docker/

│

├── scripts/

│

└── README.md
```

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/<username>/atlas.git

cd atlas
```

---

## Backend Setup

```bash
cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

Windows

```bash
.venv\Scripts\activate
```

---

## Frontend Setup

```bash
cd frontend

npm install
```

---

## Environment Variables

Create

```
backend/.env
```

Example

```env
DATABASE_URL=postgresql://user:password@localhost:5432/atlas

CHROMA_PATH=./chroma

JWT_SECRET=your-secret-key

JWT_ALGORITHM=HS256

JWT_EXPIRE_MINUTES=15

GOOGLE_API_KEY=your-google-api-key

OPENAI_API_KEY=

ANTHROPIC_API_KEY=
```

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

# Run Frontend

```bash
npm run dev
```

Frontend

```
http://localhost:3000
```

---

# Run with Docker

```bash
docker compose up --build
```

This starts

- Frontend
- Backend
- PostgreSQL
- ChromaDB

# Screenshots

> Screenshots will be added after the first stable release.

## Landing Page

```
docs/images/landing-page.png
```

---

## Dashboard

```
docs/images/dashboard.png
```

---

## Document Library

```
docs/images/document-library.png
```

---

## Upload Page

```
docs/images/upload-page.png
```

---

## Chat Interface

```
docs/images/chat.png
```

---

## Settings

```
docs/images/settings.png
```

---

# API Documentation

Atlas automatically generates API documentation.

## Swagger UI

```
http://localhost:8000/docs
```

---

## ReDoc

```
http://localhost:8000/redoc
```

---

## OpenAPI Schema

```
http://localhost:8000/openapi.json
```

---

# Development Workflow

Atlas follows a feature-branch workflow.

```
main

│

├── develop

│

├── feature/*

│

├── bugfix/*

│

└── release/*
```

---

## Branch Rules

### main

Production-ready code only.

---

### develop

Integration branch.

---

### feature/\*

One feature per branch.

Example

```
feature/document-upload

feature/chat-ui

feature/vector-search
```

---

### bugfix/\*

Example

```
bugfix/login

bugfix/chunking
```

---

# Commit Convention

Atlas follows Conventional Commits.

Examples

```
feat: add document upload

fix: resolve chunk overlap bug

docs: update API specification

refactor: simplify retrieval service

test: add embedding tests

chore: update dependencies
```

---

# Available Scripts

## Backend

Run development server

```bash
uvicorn app.main:app --reload
```

---

Run tests

```bash
pytest
```

---

Format code

```bash
black .
```

---

Sort imports

```bash
isort .
```

---

Static analysis

```bash
ruff check .
```

---

## Frontend

Install packages

```bash
npm install
```

---

Development

```bash
npm run dev
```

---

Production build

```bash
npm run build
```

---

Preview

```bash
npm run start
```

---

Lint

```bash
npm run lint
```

---

# Testing

Atlas includes multiple levels of testing.

- Unit Tests
- Integration Tests
- API Tests
- End-to-End Tests
- Performance Tests
- Security Tests
- RAG Evaluation

Coverage Goal

```
90%+
```

---

# Deployment

Atlas is designed for containerized deployment.

## Development

```bash
docker compose up
```

---

## Production

Recommended stack

- Docker
- Nginx
- PostgreSQL
- ChromaDB

Future options

- Kubernetes
- AWS ECS
- Azure Container Apps
- Google Cloud Run

---

# Documentation

The `/docs` directory contains complete project documentation.

| Document               | Purpose                             |
| ---------------------- | ----------------------------------- |
| PROJECT.md             | Product vision and project overview |
| SRS.md                 | Software Requirements Specification |
| DFD.md                 | Data Flow Diagrams                  |
| Development-Roadmap.md | Step-by-step implementation plan    |
| API-Specification.md   | REST API documentation              |
| Database-Design.md     | Database architecture and schema    |
| System-Architecture.md | Software architecture               |
| UI-UX-Specification.md | User interface guidelines           |
| Testing-Strategy.md    | Testing methodology                 |

---

# Roadmap

## Version 1.0

- User Authentication
- Document Upload
- PDF, DOCX, TXT, Markdown Support
- Text Extraction
- Chunking
- Embeddings
- ChromaDB Integration
- Semantic Search
- AI Chat
- Source Citations

---

## Version 1.1

- Folder Organization
- Bulk Upload
- OCR Support
- Better Search Filters

---

## Version 2.0

- Hybrid Search (BM25 + Vector Search)
- Cross-Encoder Reranking
- Multiple Workspaces
- Document Versioning

---

## Version 3.0

- Graph RAG
- Agentic RAG
- Multi-Agent Workflows
- Multimodal Retrieval
- Team Collaboration
- Enterprise Administration

---

# Contributing

Contributions are welcome.

Development process

1. Fork the repository.
2. Create a feature branch.
3. Implement the feature.
4. Add tests.
5. Update documentation.
6. Open a Pull Request.

All contributions should:

- Follow the project's coding standards.
- Include tests where applicable.
- Keep documentation up to date.
- Pass CI checks before merging.

---

# Coding Standards

Backend

- Python Style Guide (PEP 8)
- Type Hints
- Black
- Ruff
- isort

Frontend

- TypeScript
- ESLint
- Prettier
- Tailwind CSS conventions

---

# Security

Please do not disclose security vulnerabilities publicly.

Report security issues privately to the project maintainers before opening a public issue.

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# Acknowledgements

Atlas is built using the following open-source technologies:

- FastAPI
- Next.js
- React
- PostgreSQL
- ChromaDB
- Sentence Transformers
- Tailwind CSS
- shadcn/ui
- Docker

The project also draws inspiration from modern Retrieval-Augmented Generation research and the broader open-source AI ecosystem.

---

# Future Learning Path

Atlas is the first project in a progressive RAG portfolio.

Planned progression:

1. **Atlas** — Naive RAG
2. **Helix** — Advanced RAG
3. **Nexus** — Modular RAG
4. **Prism** — Hybrid/Enterprise RAG

Each project introduces increasingly sophisticated retrieval techniques while building upon the architectural foundations established in Atlas.

---

# Project Status

| Category              | Status   |
| --------------------- | -------- |
| Documentation         | Complete |
| Architecture          | Designed |
| API Design            | Complete |
| Database Design       | Complete |
| UI/UX Design          | Complete |
| Development           | Planned  |
| Production Deployment | Planned  |

---

# Repository Goals

Atlas aims to serve as:

- A production-quality learning project
- A portfolio project for AI and backend engineering
- A reference implementation of Naive RAG
- A foundation for advanced RAG architectures

---

# Final Notes

Atlas is intentionally designed to emphasize engineering fundamentals before introducing advanced AI techniques. By combining structured software architecture with a straightforward Retrieval-Augmented Generation pipeline, the project provides a maintainable and extensible foundation for future experimentation and production-ready development.

If you are using this repository as a learning resource, follow the **Development-Roadmap.md** and implement each phase in order. Doing so will help you understand not only how RAG works, but also how to build and evolve a complete AI-powered application using modern software engineering practices.
