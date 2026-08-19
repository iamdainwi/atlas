# Development Roadmap

# Atlas

> Production Roadmap for Building a Naive Retrieval-Augmented Generation (Naive RAG) System

Version: 1.0

Status: Planning

---

# Table of Contents

1. Introduction
2. Development Philosophy
3. Learning Objectives
4. Prerequisites
5. Project Setup
6. Development Phases
7. Git Workflow
8. Milestones
9. Deployment
10. Completion Checklist

---

# 1. Introduction

This roadmap provides the complete implementation plan for Atlas.

Rather than jumping directly into AI or RAG, Atlas is developed exactly like a real SaaS product.

Every phase builds upon the previous phase.

By the end of this roadmap you will have learned

- Full Stack Development
- Authentication
- FastAPI
- Next.js
- PostgreSQL
- ChromaDB
- Document Processing
- Embeddings
- Semantic Search
- Retrieval-Augmented Generation
- Docker Deployment

The roadmap is intentionally incremental.

Do **not** skip phases.

---

# 2. Development Philosophy

Atlas follows the principle

> Build the foundation first, AI second.

Many developers begin by integrating an LLM immediately.

Atlas does the opposite.

The order is

```
Infrastructure

↓

Authentication

↓

Database

↓

Storage

↓

Document Management

↓

Processing Pipeline

↓

Embeddings

↓

Retrieval

↓

LLM

↓

Optimization

↓

Deployment
```

Each layer must be stable before the next one is introduced.

---

# 3. Learning Objectives

By completing Atlas you should understand

### Backend

- FastAPI
- REST APIs
- Authentication
- JWT
- Background Jobs
- PostgreSQL
- SQLAlchemy

---

### Frontend

- Next.js
- TypeScript
- Tailwind CSS
- React Query
- Zustand
- Responsive Design

---

### AI

- Embeddings
- Chunking
- Vector Databases
- Similarity Search
- Prompt Engineering
- RAG Pipeline

---

### DevOps

- Docker
- Docker Compose
- Environment Variables
- Deployment

---

# 4. Prerequisites

Before starting Atlas you should know

## Required

- Python
- TypeScript
- JavaScript
- SQL
- Git
- HTTP
- REST APIs

---

## Helpful

- Docker
- React
- FastAPI
- PostgreSQL

---

# 5. Project Setup

## Step 1

Create repository

```
atlas/
```

---

## Step 2

Initialize Git

```
git init
```

---

## Step 3

Create folders

```
frontend/

backend/

docs/

docker/

scripts/

tests/

storage/
```

---

## Step 4

Create README

Describe

- Project
- Installation
- Architecture
- Features

---

## Step 5

Configure Git Ignore

Ignore

- node_modules
- **pycache**
- .env
- uploads
- logs
- build files

---

# Development Phases

Atlas consists of eleven development phases.

Each phase should be completed before moving to the next.

---

# Phase 1

# Project Foundation

Estimated Time

2–3 Days

---

## Goal

Create a clean project structure.

---

## Backend Tasks

- FastAPI Setup
- Environment Variables
- Logging
- Configuration
- Dependency Injection

---

## Frontend Tasks

- Next.js Setup
- Tailwind CSS
- Shadcn UI
- Routing
- Layout

---

## Deliverables

Working frontend

Working backend

Health endpoint

---

## Git Commits

```
Initial project structure

Setup FastAPI

Setup Next.js

Configure Tailwind

Configure Docker
```

---

## Exit Criteria

Frontend starts

Backend starts

Project structure complete

---

# Phase 2

# Authentication

Estimated Time

4–5 Days

---

## Goal

Implement secure authentication.

---

## Backend

Create

- User Model
- JWT
- Password Hashing
- Login API
- Register API

---

## Frontend

Pages

- Login
- Register
- Forgot Password

Components

- Forms
- Validation
- Error Handling

---

## Database

Create

Users Table

Sessions Table

---

## APIs

```
POST /register

POST /login

POST /logout

GET /me
```

---

## Testing

✔ Register

✔ Login

✔ JWT

✔ Protected Routes

---

## Exit Criteria

User authentication complete.

---

# Phase 3

# Database & Storage

Estimated Time

3 Days

---

## Goal

Store documents securely.

---

## Backend

Implement

- PostgreSQL Connection
- SQLAlchemy Models
- Alembic Migration
- Local File Storage

---

## Database Tables

- Users

- Documents

- Chats

- Settings

---

## File Storage

```
storage/

users/

documents/
```

---

## APIs

```
Upload

Delete

Rename

List
```

---

## Testing

Upload file

Delete file

Read metadata

---

## Exit Criteria

Files persist correctly.

---

# Phase 4

# Document Management

Estimated Time

4 Days

---

## Goal

Build document library.

---

## Backend

Implement

- Upload API
- Delete API
- Rename API
- Search API

---

## Frontend

Pages

Document Library

Upload Page

Document Details

---

## Components

Upload Button

Progress Bar

Search

Filters

Sorting

Document Cards

---

## Deliverables

Complete document management system.

---

## Git Commits

```
Add upload endpoint

Build document library

Add search

Implement filters
```

---

## Exit Criteria

Users manage documents successfully.

---

# Phase 5

# Document Processing Pipeline

Estimated Time

5–6 Days

---

## Goal

Transform uploaded files into searchable text.

---

## Build Pipeline

```
Upload

↓

Validation

↓

Extraction

↓

Cleaning

↓

Chunking
```

---

## Backend Tasks

PDF Extraction

DOCX Extraction

TXT Reader

Markdown Parser

---

## Libraries

PyMuPDF

python-docx

markdown

---

## Chunking

Implement

- Chunk Size
- Overlap
- Metadata

---

## Testing

Verify

Extraction

Chunk Count

Page Numbers

---

## Deliverables

Complete ingestion pipeline.

---

## Exit Criteria

Documents converted into chunks.

# Phase 6

# Embedding Generation

Estimated Time

4–5 Days

---

## Goal

Convert every document chunk into a numerical vector representation that can later be searched using semantic similarity.

This is the first AI-specific phase of Atlas.

---

## Concepts to Learn

- What are embeddings?
- Dense vector representations
- Sentence Transformers
- Cosine Similarity
- Embedding dimensions
- Batch inference

---

## Backend Tasks

Create

```
Embedding Service

Embedding Interface

Embedding Configuration

Embedding Cache

Batch Processing
```

---

## Responsibilities

The Embedding Service shall

- Load embedding model
- Generate chunk embeddings
- Generate query embeddings
- Batch process documents
- Handle model initialization
- Retry failed generations

---

## Default Model

```
BAAI/bge-small-en-v1.5
```

Future Support

- all-MiniLM-L6-v2
- bge-base
- jina-embeddings
- nomic-embed-text

---

## Processing Flow

```
Chunks

↓

Embedding Model

↓

768-Dimensional Vector

↓

Vector Database
```

---

## Files to Create

```
services/

embedding/

├── service.py

├── models.py

├── interface.py

├── utils.py
```

---

## APIs

No public APIs.

Embedding generation is triggered internally after chunk generation.

---

## Testing Checklist

✔ Embeddings generated

✔ Correct dimensions

✔ Batch processing

✔ Error handling

✔ Retry mechanism

---

## Git Commits

```
Create embedding service

Load embedding model

Generate chunk embeddings

Implement batch embeddings
```

---

## Exit Criteria

Every document chunk successfully generates embeddings.

---

# Phase 7

# Vector Database

Estimated Time

3–4 Days

---

## Goal

Store embeddings and enable semantic similarity search.

---

## Concepts

- Vector Databases
- Similarity Search
- Metadata Filtering
- Collections
- Indexing

---

## Technology

ChromaDB

---

## Backend Tasks

Create

- Collection Manager
- Vector Storage
- Similarity Search
- Delete Embeddings
- Update Embeddings

---

## Metadata

Store

```
Document ID

User ID

Chunk ID

Chunk Number

Page Number

Filename

Text

Embedding
```

---

## Files

```
services/

retrieval/

├── chroma.py

├── collections.py

├── search.py

├── delete.py
```

---

## APIs

Internal

```
Store Embeddings

Delete Embeddings

Search Embeddings
```

---

## Testing

✔ Store vectors

✔ Delete vectors

✔ Similarity search

✔ Metadata retrieval

---

## Git Commits

```
Configure ChromaDB

Store vectors

Delete vectors

Search vectors
```

---

## Exit Criteria

Embeddings successfully stored and retrieved.

---

# Phase 8

# Semantic Retrieval

Estimated Time

5 Days

---

## Goal

Retrieve the most relevant document chunks based on semantic similarity.

---

## Concepts

- Query Embeddings
- Cosine Similarity
- Top-K Search
- Retrieval Pipeline

---

## Retrieval Flow

```
Question

↓

Query Embedding

↓

Similarity Search

↓

Top K Chunks

↓

Return Context
```

---

## Backend Tasks

Implement

- Query embedding generation
- Top-K retrieval
- Similarity threshold
- Metadata filtering
- Context ranking

---

## Configuration

```
Top-K

Chunk Size

Similarity Threshold
```

---

## Files

```
services/

retrieval/

├── retrieve.py

├── ranking.py

├── filters.py
```

---

## APIs

```
POST

/api/search
```

---

## Testing

✔ Correct chunk retrieval

✔ Metadata filtering

✔ Multiple documents

✔ Empty results

---

## Git Commits

```
Generate query embeddings

Implement similarity search

Return top-k chunks
```

---

## Exit Criteria

Questions retrieve the correct document chunks.

---

# Phase 9

# AI Chat Integration

Estimated Time

6–7 Days

---

## Goal

Connect the retrieval pipeline with a Large Language Model.

---

## Concepts

- Prompt Engineering
- Context Window
- Grounding
- Streaming Responses

---

## Prompt Structure

```
System Prompt

+

Retrieved Context

+

Conversation History

+

Current Question
```

↓

LLM

↓

Response

---

## Backend Tasks

Implement

- Prompt Builder
- LLM Service
- Provider Interface
- Streaming API

---

## Supported Providers

- Gemini
- OpenAI
- Claude
- Ollama
- OpenRouter

---

## Frontend

Create

Chat Page

Message List

Input Box

Streaming Renderer

Source Viewer

---

## APIs

```
POST

/api/chat

POST

/api/chat/{id}/message
```

---

## Testing

✔ Prompt generation

✔ Streaming

✔ Source citations

✔ Chat history

---

## Git Commits

```
Integrate Gemini

Build prompt service

Create chat interface

Display citations
```

---

## Exit Criteria

Users can ask questions and receive grounded AI responses.

---

# Phase 10

# Dashboard & User Experience

Estimated Time

5 Days

---

## Goal

Transform Atlas into a polished SaaS application.

---

## Dashboard Widgets

- Total Documents
- Storage Used
- Total Chats
- Recent Uploads
- Processing Queue

---

## Features

Document Search

Filters

Sorting

Settings

Theme

Profile

---

## Pages

```
Dashboard

Library

Upload

Chat

Settings

Profile
```

---

## UI Components

Navbar

Sidebar

Document Card

Search Bar

Settings Panel

Toast Notifications

Loading Skeletons

Dialogs

---

## Testing

✔ Navigation

✔ Responsive Layout

✔ Theme

✔ Search

---

## Git Commits

```
Create dashboard

Implement settings

Improve responsive UI

Add loading states
```

---

## Exit Criteria

Atlas provides a complete user experience.

---

# Phase 11

# Testing, Optimization & Deployment

Estimated Time

6–8 Days

---

## Goal

Prepare Atlas for production deployment.

---

## Testing

### Unit Testing

- Services
- Utilities
- APIs

---

### Integration Testing

- Upload Pipeline
- Retrieval
- Authentication
- AI Chat

---

### End-to-End Testing

Scenario

```
Register

↓

Login

↓

Upload

↓

Process

↓

Ask Question

↓

Delete Document
```

---

## Performance Optimization

Backend

- Async APIs
- Batch Processing
- Connection Pooling

Frontend

- Lazy Loading
- Memoization
- Code Splitting

Retrieval

- Cache embeddings
- Optimize Top-K

---

## Security Review

Verify

- JWT
- Authorization
- File Validation
- Input Sanitization
- HTTPS

---

## Deployment

Build

```
Docker Images

↓

Docker Compose

↓

Nginx

↓

Production Server
```

---

## Deliverables

- Docker Compose
- Environment Variables
- Production Build
- README
- Documentation

---

## Git Commits

```
Add tests

Optimize performance

Dockerize application

Deploy Atlas v1.0
```

---

## Exit Criteria

Application deployed successfully.

---

# Git Workflow

## Branch Strategy

```
main

develop

feature/*

bugfix/*

release/*
```

---

## Commit Convention

```
feat:

fix:

docs:

refactor:

test:

chore:
```

---

# Suggested Milestones

| Milestone | Outcome               |
| --------- | --------------------- |
| M1        | Project Setup         |
| M2        | Authentication        |
| M3        | Database & Storage    |
| M4        | Document Library      |
| M5        | Processing Pipeline   |
| M6        | Embedding Generation  |
| M7        | Vector Database       |
| M8        | Semantic Retrieval    |
| M9        | AI Chat               |
| M10       | Dashboard & UX        |
| M11       | Testing               |
| M12       | Production Deployment |

---

# Final Project Completion Checklist

## Backend

- [ ] Authentication
- [ ] REST APIs
- [ ] PostgreSQL
- [ ] File Storage
- [ ] Processing Pipeline
- [ ] Chunking
- [ ] Embedding Generation
- [ ] ChromaDB Integration
- [ ] Retrieval Engine
- [ ] Prompt Builder
- [ ] LLM Integration

---

## Frontend

- [ ] Authentication
- [ ] Dashboard
- [ ] Document Library
- [ ] Upload Page
- [ ] Chat Interface
- [ ] Settings
- [ ] Profile
- [ ] Responsive Design

---

## AI

- [ ] Embedding Model
- [ ] Semantic Search
- [ ] Context Retrieval
- [ ] Prompt Engineering
- [ ] Source Citations

---

## Deployment

- [ ] Docker
- [ ] Environment Variables
- [ ] Production Configuration
- [ ] Documentation
- [ ] Testing

---

# Roadmap Summary

Atlas is built in eleven incremental phases. Each phase introduces a distinct layer of the system, ensuring that infrastructure, data management, retrieval, and AI capabilities are developed in a stable and maintainable order.

Following this roadmap results in a production-ready implementation of a **Naive Retrieval-Augmented Generation (Naive RAG)** application that can serve as the foundation for more advanced RAG projects in the future.
