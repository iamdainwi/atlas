# Atlas

> An Intelligent Personal Document Library powered by Naive Retrieval-Augmented Generation (Naive RAG)

```
Version: 1.0.0
Status: Planning
Project Type: Full Stack AI SaaS
RAG Type: Naive RAG

```

---

# 1. Project Overview

## 1.1 Introduction

Atlas is an AI-powered Personal Document Library that enables users to upload, organize, search, and interact with their documents using natural language. Instead of manually opening documents and searching through hundreds of pages, users can ask questions in plain English and Atlas retrieves the most relevant document chunks before generating an accurate answer using a Large Language Model (LLM).

Atlas is designed as a learning project for implementing a complete **Naive Retrieval-Augmented Generation (Naive RAG)** pipeline while following production-level software engineering practices. The project emphasizes clean architecture, modularity, scalability, and maintainability rather than simply demonstrating RAG concepts.

The application supports four document formats:

- PDF
- DOCX
- TXT
- Markdown (.md)

Each uploaded document is processed through a document ingestion pipeline where text is extracted, segmented into chunks, converted into vector embeddings, and stored inside a vector database. During querying, Atlas retrieves the most semantically relevant chunks and supplies them as context to the language model, enabling grounded and document-specific responses.

---

# 2. Vision

## Vision Statement

> Build an intelligent personal knowledge assistant capable of transforming static documents into an interactive, searchable, and conversational knowledge base while serving as a production-quality implementation of a Naive RAG architecture.

Atlas aims to bridge the gap between traditional document management systems and modern AI-powered knowledge retrieval systems by allowing users to converse with their personal documents instead of searching through them manually.

---

# 3. Mission

Atlas exists to solve one simple problem:

> **People spend more time searching for information inside documents than actually using that information.**

Traditional search relies on keyword matching.

Humans think in questions.

Atlas allows users to ask questions naturally while AI performs semantic retrieval over their documents.

Examples:

Instead of searching

```

Transformer architecture

```

Users can ask

```

How does the Transformer encoder differ from the decoder?

```

Instead of searching

```

Payment policy

```

Users ask

```

What happens if a customer cancels after 30 days?

```

---

# 4. Problem Statement

Managing large collections of digital documents has become increasingly difficult.

Modern users often possess

- Research papers
- Technical documentation
- Notes
- Company documentation
- Books
- Contracts
- Reports
- Meeting notes

Traditional document management systems provide:

- Folder organization
- File search
- Keyword search

However, they fail to provide:

- Semantic understanding
- Context-aware search
- Conversational interaction
- Knowledge retrieval
- Intelligent summarization

As document collections grow larger, users spend significant time locating information scattered across multiple files.

Large Language Models possess strong reasoning capabilities but cannot reliably answer questions about private documents unless those documents are provided as context.

Naive Retrieval-Augmented Generation solves this limitation by retrieving only the most relevant document chunks and supplying them to the LLM before response generation.

Atlas implements this workflow end-to-end.

---

# 5. Objectives

The primary objectives of Atlas are:

## Educational Objectives

- Understand Naive Retrieval-Augmented Generation
- Learn embedding generation
- Learn semantic search
- Learn vector databases
- Learn document chunking
- Learn prompt engineering
- Learn LLM orchestration
- Learn production AI architecture

---

## Technical Objectives

Build a complete production-ready AI application including

- Authentication
- File upload
- Document processing
- Vector indexing
- Semantic retrieval
- AI chat
- Conversation history
- User management
- REST APIs
- Responsive frontend

---

## Product Objectives

Create a software product that

- Organizes documents
- Enables conversational document search
- Reduces information retrieval time
- Improves productivity
- Demonstrates practical AI engineering

---

# 6. Goals

Atlas is designed to achieve the following goals.

## Functional Goals

- Upload documents
- Store documents securely
- Extract text
- Process documents automatically
- Generate embeddings
- Store vectors
- Search semantically
- Answer user questions
- Display cited document sources
- Maintain conversation history

---

## Engineering Goals

- Modular architecture
- Clean codebase
- SOLID principles
- Reusable components
- Independent services
- Easy extensibility
- Production-ready APIs

---

## AI Goals

- Accurate retrieval
- Context-aware responses
- Low hallucination
- Fast retrieval
- Configurable language models
- Configurable embedding models

---

# 7. Scope

Atlas focuses exclusively on implementing **Naive RAG**.

The project intentionally avoids advanced retrieval techniques such as:

- Hybrid Search
- Graph RAG
- Self RAG
- Corrective RAG
- Agentic RAG
- Adaptive RAG
- Multi-hop Retrieval
- Knowledge Graph Integration

These techniques are reserved for future projects in the RAG series.

The objective of Atlas is to build a perfect implementation of the simplest RAG architecture before progressing to more advanced systems.

---

# 8. Project Type

Atlas is categorized as

- AI Application
- Knowledge Management System
- Personal Document Library
- Full Stack SaaS
- REST API Application
- RAG System
- Semantic Search Engine

---

# 9. Target Users

Atlas is designed primarily for individuals who need intelligent access to their personal document collections.

### Students

Store lecture notes, textbooks, research papers, assignments, and study material.

Example questions

- Explain Chapter 5.
- Summarize this research paper.
- List important formulas.

---

### Researchers

Manage hundreds of research papers.

Example

- Which paper discusses contrastive learning?
- Compare the conclusions of Paper A and Paper B.

---

### Software Engineers

Upload

- API documentation
- Design documents
- RFCs
- Technical notes

Example

- How is authentication implemented?
- Explain the caching mechanism.

---

### Writers

Maintain drafts, notes, references, and manuscripts.

Example

- Find every chapter mentioning this character.
- Summarize my notes about world building.

---

### Business Professionals

Store

- Reports
- Contracts
- Policies
- Meeting notes

Example

- What is the leave policy?
- Which clients renewed their contracts?

---

# 10. Expected Outcomes

After completion, Atlas should allow users to:

- Upload documents
- View document library
- Search documents semantically
- Chat with documents
- Receive grounded AI responses
- View source citations
- Organize documents
- Delete documents
- Track chat history
- Continue previous conversations

The system should provide responses that are based on retrieved document content rather than relying solely on the LLM's pretrained knowledge.

---

# 11. Success Criteria

Atlas will be considered successfully completed when it satisfies the following criteria.

### Functional

- All supported documents can be uploaded.
- Documents are indexed successfully.
- Embeddings are generated correctly.
- Semantic retrieval returns relevant chunks.
- AI answers are grounded in retrieved context.

### Performance

- Document upload under 10 seconds for typical files.
- Query response under 5 seconds.
- Efficient vector search.
- Smooth user experience.

### Quality

- Modular architecture
- Comprehensive documentation
- Clean codebase
- Proper error handling
- Responsive UI
- Secure authentication
- Production-ready deployment

# 12. Core Features

Atlas is built around five major capabilities:

1. Document Management
2. Document Processing Pipeline
3. Semantic Retrieval
4. AI Conversation
5. Knowledge Management

These capabilities together form the complete Naive RAG workflow.

---

# 13. Functional Modules

Atlas is divided into independent modules to ensure scalability, maintainability, and clean architecture.

## 13.1 Authentication Module

Responsible for user identity and access management.

### Features

- User Registration
- User Login
- JWT Authentication
- Refresh Tokens
- Logout
- Password Reset
- Email Verification
- Session Management

### Responsibilities

- Authenticate users
- Protect APIs
- Issue JWT Tokens
- Manage active sessions

---

## 13.2 User Profile Module

Stores user-specific information.

### Features

- Update Profile
- Change Password
- Avatar
- Theme Preference
- API Key Management
- Preferred LLM
- Preferred Embedding Model

---

## 13.3 Document Library Module

Acts as the central storage interface.

Users can

- Upload documents
- Delete documents
- Rename documents
- View metadata
- Search documents
- Filter documents
- Sort documents
- Preview documents

Supported formats

- PDF
- DOCX
- TXT
- Markdown

Stored metadata

- Document Name
- File Size
- Upload Time
- Status
- Processing Status
- Number of Pages
- Number of Chunks
- Tags
- Owner

---

## 13.4 Document Processing Module

This module transforms raw documents into searchable knowledge.

Pipeline

```

Upload

↓

Validation

↓

Temporary Storage

↓

Text Extraction

↓

Cleaning

↓

Chunking

↓

Embedding Generation

↓

Vector Storage

↓

Ready for Querying
```

### Responsibilities

- Validate file
- Extract text
- Remove formatting noise
- Split into chunks
- Generate embeddings
- Store vectors
- Track processing progress

---

## 13.5 Chunking Module

Responsible for splitting documents into manageable semantic units.

Atlas uses fixed-size overlapping chunking.

Example

Chunk Size

500 tokens

Overlap

100 tokens

Benefits

- Preserves context
- Improves retrieval quality
- Reduces hallucination
- Better semantic similarity

---

## 13.6 Embedding Module

Converts text into vector representations.

Responsibilities

- Load embedding model
- Generate embeddings
- Batch processing
- Cache embeddings
- Handle retries

Default Model

Sentence Transformers

Configurable by administrator.

---

## 13.7 Vector Database Module

Stores embeddings.

Responsibilities

- Store vectors
- Delete vectors
- Update vectors
- Perform similarity search
- Return Top-K chunks

Default Database

ChromaDB

Future support

- Pinecone
- Weaviate
- Milvus
- Qdrant

---

## 13.8 Retrieval Module

Responsible for semantic search.

Workflow

Receive Query

↓

Generate Query Embedding

↓

Similarity Search

↓

Retrieve Top-K Chunks

↓

Return Relevant Context

Default

Top 5 chunks

Configurable

Top K

Similarity Threshold

Maximum Context Length

---

## 13.9 Prompt Construction Module

Creates prompts sent to the LLM.

Prompt Template

System Prompt

↓

Retrieved Context

↓

Conversation History

↓

User Question

↓

Final Prompt

Responsibilities

- Inject retrieved chunks
- Maintain chat history
- Prevent prompt overflow
- Token counting

---

## 13.10 LLM Module

Communicates with the language model.

Supported Providers

- OpenAI
- Gemini
- Ollama
- Anthropic Claude
- OpenRouter

Responsibilities

- Send prompt
- Receive response
- Streaming
- Retry failed requests

---

## 13.11 Chat Module

Provides conversational interface.

Features

- New Chat
- Continue Chat
- Delete Chat
- Rename Chat
- Export Chat
- Markdown Rendering
- Code Highlighting

Conversation Memory

Current conversation only.

(No advanced memory because Atlas is Naive RAG.)

---

## 13.12 Search Module

Provides document discovery.

Supports

Document Name

Content Search

Tag Search

Metadata Search

Upload Date

---

## 13.13 Settings Module

Allows customization.

Settings include

Theme

Language

Embedding Model

LLM

Temperature

Maximum Tokens

Top K

Chunk Size

Overlap Size

---

# 14. User Stories

## Authentication

As a user,

I want to create an account

So that my documents remain private.

---

As a user,

I want to login securely

So that only I can access my knowledge base.

---

## Document Upload

As a user,

I want to upload PDF files

So that Atlas can answer questions about them.

---

As a user,

I want to upload DOCX files

So that my reports become searchable.

---

As a user,

I want upload multiple documents

So that I can build a personal knowledge library.

---

## Processing

As a user,

I want Atlas to automatically process documents

So that I don't manually configure embeddings.

---

## Chat

As a user,

I want to ask questions naturally

So that I don't search manually.

---

As a user,

I want Atlas to cite its sources

So that I can verify every answer.

---

## Search

As a user,

I want semantic search

So that related information is found even when keywords differ.

---

## Library

As a user,

I want to organize my documents

So that my library remains manageable.

---

# 15. User Journey

## Step 1

User registers.

↓

## Step 2

User logs in.

↓

## Step 3

Dashboard opens.

↓

## Step 4

User uploads document.

↓

## Step 5

Atlas validates document.

↓

## Step 6

Atlas extracts text.

↓

## Step 7

Atlas creates chunks.

↓

## Step 8

Atlas generates embeddings.

↓

## Step 9

Vectors stored in ChromaDB.

↓

## Step 10

Document marked Ready.

↓

## Step 11

User opens Chat.

↓

## Step 12

User asks question.

↓

## Step 13

Atlas retrieves relevant chunks.

↓

## Step 14

Atlas builds prompt.

↓

## Step 15

LLM generates grounded response.

↓

## Step 16

Atlas displays

- Answer
- Sources
- Confidence indicators (future enhancement)

---

# 16. End-to-End System Workflow

```

User

↓

Uploads Document

↓

API Gateway

↓

Authentication

↓

File Storage

↓

Document Processing Service

↓

Text Extraction

↓

Chunking

↓

Embedding Generation

↓

Vector Database

↓

Document Ready

↓

User Question

↓

Query Embedding

↓

Similarity Search

↓

Top K Chunks

↓

Prompt Builder

↓

LLM

↓

Grounded Response

↓

Frontend

```

---

# 17. RAG Pipeline

Atlas follows a classic Naive RAG architecture consisting of two major pipelines.

## Indexing Pipeline

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

↓

Embedding

↓

Vector Storage

```

---

## Retrieval Pipeline

```

User Query

↓

Embedding

↓

Similarity Search

↓

Retrieve Chunks

↓

Prompt Construction

↓

LLM

↓

Answer Generation

```

---

# 18. High-Level Architecture

```

                 Frontend (Next.js)

                        │

                        ▼

                FastAPI Backend

                        │

        ┌───────────────┼────────────────┐

        ▼               ▼                ▼

Authentication Document Service Chat Service

        │               │                │

        ▼               ▼                ▼

PostgreSQL Local Storage LLM Provider

                        │

                        ▼

                Processing Pipeline

                        │

      Extraction → Chunking → Embeddings

                        │

                        ▼

                   ChromaDB

                        │

                        ▼

                Semantic Retrieval

                        │

                        ▼

                 Prompt Builder

                        │

                        ▼

                    AI Response

```

---

# 19. Component Responsibilities

| Component           | Responsibility          |
| ------------------- | ----------------------- |
| Frontend            | User Interface          |
| FastAPI             | Business Logic          |
| PostgreSQL          | Structured Data         |
| Local Storage       | Original Documents      |
| Processing Pipeline | Text Preparation        |
| Embedding Service   | Vector Generation       |
| ChromaDB            | Semantic Index          |
| Retrieval Engine    | Similarity Search       |
| Prompt Builder      | Context Assembly        |
| LLM Provider        | Final Response          |
| Authentication      | Identity & Security     |
| Chat Service        | Conversation Management |

# 20. Technology Stack

Atlas is designed with a modern, scalable, and production-oriented technology stack. Every technology has been selected based on maturity, community support, performance, and ease of integration with Retrieval-Augmented Generation systems.

---

## 20.1 Frontend

### Framework

- Next.js 15

### Language

- TypeScript

### UI Library

- React 19

### Styling

- Tailwind CSS
- Shadcn UI
- Radix UI

### State Management

- Zustand

### Data Fetching

- TanStack Query

### Form Handling

- React Hook Form
- Zod Validation

### Charts

- Recharts

### Icons

- Lucide Icons

### Notifications

- Sonner

### Markdown Rendering

- react-markdown
- rehype-highlight

---

## Why Next.js?

- Server Components
- Excellent performance
- Routing
- SEO support
- API Routes (optional)
- Mature ecosystem

---

# 20.2 Backend

### Framework

FastAPI

### Language

Python

### Validation

Pydantic

### Authentication

JWT

OAuth 2.0

### Background Jobs

Celery

### Cache

Redis

### File Processing

Python libraries

- PyMuPDF
- python-docx
- markdown
- Unstructured

---

## Why FastAPI?

- Extremely fast
- Automatic OpenAPI documentation
- Async support
- Excellent typing
- Perfect for AI services

---

# 20.3 AI Stack

### Embedding Models

Default

```

BAAI/bge-small-en-v1.5

```

Optional

- all-MiniLM-L6-v2
- bge-base
- nomic-embed-text
- jina-embeddings

---

### LLM Providers

Atlas is provider agnostic.

Supported

- Google Gemini
- OpenAI GPT
- Anthropic Claude
- Ollama
- OpenRouter

---

### Vector Database

Default

ChromaDB

Future Support

- Pinecone
- Weaviate
- Milvus
- Qdrant

---

# 20.4 Database

Primary Database

PostgreSQL

Purpose

- User accounts
- Documents
- Metadata
- Chats
- Settings

---

Vector Database

ChromaDB

Purpose

- Store embeddings
- Similarity search

---

Cache

Redis

Purpose

- Session cache
- Rate limiting
- Background tasks
- Temporary processing

---

# 20.5 Infrastructure

Containerization

Docker

Reverse Proxy

Nginx

Deployment

Docker Compose

Cloud

AWS / Azure / DigitalOcean

Storage

Local Storage

Future

Amazon S3

---

# 21. Project Structure

```

Atlas/

│

├── frontend/

├── backend/

├── docker/

├── docs/

├── scripts/

├── tests/

├── assets/

├── .github/

├── README.md

└── docker-compose.yml

```

---

# 22. Frontend Folder Structure

```

frontend/

│

├── app/

├── components/

│ ├── chat/

│ ├── dashboard/

│ ├── documents/

│ ├── ui/

│ ├── layout/

│ └── settings/

│

├── hooks/

├── lib/

├── services/

├── store/

├── types/

├── styles/

├── utils/

├── constants/

├── public/

└── middleware.ts

```

---

# 23. Backend Folder Structure

```

backend/

│

├── app/

│

├── api/

│

├── auth/

│

├── core/

│

├── database/

│

├── models/

│

├── schemas/

│

├── services/

│

│ ├── ingestion/

│ ├── retrieval/

│ ├── embedding/

│ ├── chunking/

│ ├── llm/

│ ├── prompt/

│ └── storage/

│

├── workers/

├── utils/

├── middleware/

├── config/

├── tests/

└── main.py

```

---

# 24. Database Design

Atlas uses two databases.

## Relational Database

PostgreSQL

Stores structured information.

### Tables

- users
- sessions
- documents
- document_tags
- chats
- chat_messages
- settings
- api_keys
- processing_jobs

---

## Vector Database

ChromaDB

Stores

- Chunk Text
- Embeddings
- Metadata

---

# 25. Relational Database Schema

## Users

| Column        | Type      |
| ------------- | --------- |
| id            | UUID      |
| name          | VARCHAR   |
| email         | VARCHAR   |
| password_hash | TEXT      |
| avatar        | TEXT      |
| provider      | VARCHAR   |
| created_at    | TIMESTAMP |
| updated_at    | TIMESTAMP |

---

## Documents

| Column            | Type      |
| ----------------- | --------- |
| id                | UUID      |
| owner_id          | UUID      |
| title             | VARCHAR   |
| filename          | VARCHAR   |
| file_type         | VARCHAR   |
| size              | BIGINT    |
| pages             | INTEGER   |
| chunk_count       | INTEGER   |
| processing_status | VARCHAR   |
| uploaded_at       | TIMESTAMP |

---

## Chats

| Column     | Type      |
| ---------- | --------- |
| id         | UUID      |
| user_id    | UUID      |
| title      | VARCHAR   |
| created_at | TIMESTAMP |

---

## Messages

| Column     | Type      |
| ---------- | --------- |
| id         | UUID      |
| chat_id    | UUID      |
| role       | VARCHAR   |
| content    | TEXT      |
| created_at | TIMESTAMP |

---

## Settings

| Column          | Type    |
| --------------- | ------- |
| id              | UUID    |
| user_id         | UUID    |
| theme           | VARCHAR |
| llm_provider    | VARCHAR |
| embedding_model | VARCHAR |
| temperature     | FLOAT   |
| top_k           | INTEGER |

---

# 26. ChromaDB Metadata Schema

Each vector stores:

```

Chunk ID

Document ID

User ID

Chunk Index

Chunk Text

Embedding Vector

Page Number

Source File

Created Time

```

Metadata Example

```json
{
  "document_id": "doc_001",
  "chunk_index": 15,
  "page": 7,
  "filename": "rag.pdf",
  "user_id": "user_001"
}
```

---

# 27. File Storage Structure

```
storage/

│

├── users/

│

├── user_001/

│

│   ├── documents/

│   ├── thumbnails/

│   └── exports/

│

├── temp/

└── logs/
```

---

# 28. REST API Specification

## Authentication

```
POST /api/auth/register

POST /api/auth/login

POST /api/auth/logout

POST /api/auth/google

POST /api/auth/refresh
```

---

## User

```
GET /api/user

PUT /api/user

DELETE /api/user
```

---

## Documents

```
POST /api/documents

GET /api/documents

GET /api/documents/{id}

PUT /api/documents/{id}

DELETE /api/documents/{id}
```

---

## Chat

```
POST /api/chat

GET /api/chat

GET /api/chat/{id}

DELETE /api/chat/{id}
```

---

## Messages

```
POST /api/chat/{id}/message

GET /api/chat/{id}/messages
```

---

## Search

```
POST /api/search
```

---

## Settings

```
GET /api/settings

PUT /api/settings
```

---

# 29. Frontend Pages

Atlas consists of the following pages.

## Public

- Landing Page
- Login
- Register
- Forgot Password
- Reset Password

---

## Protected

- Dashboard
- Documents
- Upload
- Chat
- Search
- Settings
- Profile

---

# 30. Dashboard Layout

```
+--------------------------------------+

Sidebar

|

| Dashboard

| Documents

| Chat

| Search

| Settings

|

+----------------------+---------------+

Navbar

---------------------------------------

Quick Stats

Recent Documents

Recent Chats

Storage Usage

Processing Queue

---------------------------------------

Footer
```

---

# 31. Backend Services

Atlas backend is divided into specialized services.

## Authentication Service

Responsible for

- JWT
- OAuth
- Authorization

---

## Storage Service

Responsible for

- Saving files
- Deleting files
- Moving files

---

## Ingestion Service

Responsible for

- Reading documents
- Cleaning text
- Metadata extraction

---

## Chunking Service

Responsible for

- Splitting text
- Overlap
- Token counting

---

## Embedding Service

Responsible for

- Generating vectors
- Batch embeddings
- Retry logic

---

## Retrieval Service

Responsible for

- Similarity Search
- Ranking
- Context Selection

---

## Prompt Service

Responsible for

- Prompt templates
- Context formatting
- Token budgeting

---

## Chat Service

Responsible for

- Conversations
- Streaming
- Chat history

---

## Settings Service

Responsible for

- User preferences
- AI configuration
- Theme configuration

---

# 32. Background Workers

Long-running tasks are executed asynchronously.

Jobs include

- Document Processing
- Embedding Generation
- Thumbnail Generation (future)
- Export Jobs
- Cleanup Jobs
- Backup Jobs

Celery workers consume tasks from Redis queues.

---

# 33. Design Patterns Used

Atlas follows established software design patterns.

## Architectural Patterns

- Layered Architecture
- Clean Architecture
- Repository Pattern
- Dependency Injection
- Service Layer Pattern

---

## AI Patterns

- Retrieval-Augmented Generation
- Prompt Template Pattern
- Embedding Pipeline
- Semantic Retrieval Pipeline
- Vector Indexing Pipeline

---

## Frontend Patterns

- Component Composition
- Container-Presenter Pattern
- Custom Hooks
- Feature-Based Modules
- Client State + Server State Separation

---

# 34. Engineering Principles

The project follows these principles.

- SOLID Principles
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple)
- YAGNI (You Aren't Gonna Need It)
- Separation of Concerns
- Single Responsibility
- Loose Coupling
- High Cohesion

These principles ensure Atlas remains maintainable as more advanced RAG techniques are introduced in future projects.

# 35. User Interface & User Experience

Atlas follows a clean, modern, and productivity-focused design philosophy.

## Design Principles

- Minimalistic Interface
- Fast Navigation
- AI-first Experience
- Responsive Layout
- Accessibility (WCAG 2.1)
- Consistent Design Language
- Low Cognitive Load

---

## Color Palette

### Light Theme

- Background: White
- Surface: Gray-50
- Primary: Blue-600
- Secondary: Slate-600
- Success: Green-600
- Warning: Amber-500
- Error: Red-600

---

### Dark Theme

- Background: Zinc-950
- Surface: Zinc-900
- Primary: Blue-500
- Secondary: Slate-300
- Success: Green-500
- Warning: Amber-400
- Error: Red-500

---

## Navigation Structure

```
Dashboard

├── Documents
│     ├── Upload
│     ├── Library
│     └── Details
│
├── Chat
│
├── Search
│
├── Settings
│
└── Profile
```

---

# 36. Screen Specifications

## 36.1 Landing Page

Purpose

Introduce Atlas and convert visitors into users.

Sections

- Hero Section
- Features
- How Atlas Works
- Supported Formats
- Technology Stack
- Pricing (Future)
- FAQ
- Footer

CTA Buttons

- Get Started
- View GitHub
- Documentation

---

## 36.2 Login Page

Features

- Email Login
- Password Login
- Google OAuth
- Forgot Password
- Remember Me

---

## 36.3 Dashboard

Displays system overview.

Widgets

- Total Documents
- Storage Used
- Total Chats
- Processing Queue
- Recent Uploads
- Recent Conversations
- Quick Actions

---

## 36.4 Document Library

Displays uploaded documents.

Features

- Grid/List View
- Search
- Filters
- Sort
- Upload
- Delete
- Rename
- Preview

Each Document Card Displays

- Name
- Type
- Upload Date
- Processing Status
- Number of Pages
- Number of Chunks

---

## 36.5 Upload Screen

Features

- Drag & Drop
- Browse Files
- Upload Progress
- Validation
- Processing Status

Accepted Formats

- PDF
- DOCX
- TXT
- Markdown

---

## 36.6 Chat Screen

Main Components

```
+--------------------------------------+

Conversation Sidebar

|

Chat Window

|

Sources Panel

|

Input Box

+--------------------------------------+
```

Features

- Streaming Responses
- Markdown Support
- Code Highlighting
- Copy Response
- Retry Response
- View Sources

---

## 36.7 Settings

Categories

- Profile
- Theme
- AI Models
- Retrieval
- API Keys
- Account
- Security

---

# 37. Document Ingestion Workflow

The ingestion pipeline is responsible for converting uploaded files into searchable knowledge.

## Step 1

User uploads a file.

↓

## Step 2

Backend validates

- File Type
- File Size
- Virus Scan (Future)

↓

## Step 3

Document stored temporarily.

↓

## Step 4

Text Extraction

↓

## Step 5

Metadata Extraction

↓

## Step 6

Text Cleaning

↓

## Step 7

Chunk Generation

↓

## Step 8

Embedding Generation

↓

## Step 9

Vector Storage

↓

## Step 10

Metadata Storage

↓

## Step 11

Processing Completed

---

# 38. Query Processing Workflow

```
User Question

↓

Authentication

↓

Generate Query Embedding

↓

Search ChromaDB

↓

Retrieve Top-K Chunks

↓

Rank Results

↓

Construct Prompt

↓

Send to LLM

↓

Receive Response

↓

Return Answer + Sources
```

---

# 39. Security Architecture

Atlas prioritizes user privacy and document security.

## Authentication

- JWT Access Tokens
- Refresh Tokens
- Google OAuth

---

## Authorization

Each request is verified using

- User Identity
- Resource Ownership
- Access Token

---

## Password Security

Passwords are never stored in plain text.

Hashing Algorithm

- bcrypt

---

## API Security

- HTTPS
- Rate Limiting
- Request Validation
- Input Sanitization
- CORS Protection

---

## File Security

- File Type Validation
- File Size Limits
- Filename Sanitization
- Secure Storage Paths

---

## AI Security

Prevent

- Prompt Injection
- Malicious Context
- Token Abuse
- Excessive Requests

Future

- Content Moderation
- Jailbreak Detection

---

# 40. Performance Optimization

Atlas is optimized for responsiveness.

## Backend

- Async FastAPI
- Background Workers
- Connection Pooling
- Batch Embeddings
- Efficient Database Queries

---

## Frontend

- Lazy Loading
- Code Splitting
- React Memoization
- Image Optimization
- Infinite Scrolling

---

## Retrieval

- Cached Embeddings
- Vector Index Optimization
- Configurable Top-K
- Chunk Caching

---

# 41. Error Handling Strategy

Every operation returns meaningful feedback.

## Upload Errors

Examples

- Unsupported file type
- File too large
- Upload interrupted

---

## Processing Errors

Examples

- Extraction failed
- Embedding generation failed
- Vector storage unavailable

---

## Chat Errors

Examples

- LLM unavailable
- API timeout
- Token limit exceeded

---

## User Errors

Examples

- Invalid credentials
- Unauthorized access
- Expired session

---

# 42. Logging Strategy

Atlas maintains structured logs.

Log Categories

- Authentication
- Uploads
- Processing
- Retrieval
- AI Requests
- Errors
- Performance

Log Levels

- INFO
- DEBUG
- WARNING
- ERROR
- CRITICAL

---

# 43. Monitoring

Metrics to monitor

Application

- CPU Usage
- Memory Usage
- Active Users
- API Response Time

AI

- Retrieval Time
- Embedding Time
- LLM Response Time
- Token Usage

Database

- Query Latency
- Connection Count
- Storage Usage

---

# 44. Testing Strategy

## Unit Testing

Test

- Services
- Utilities
- API Logic
- Chunking
- Embeddings

---

## Integration Testing

Verify

- Upload Pipeline
- Authentication
- Retrieval Pipeline
- Chat Workflow

---

## End-to-End Testing

Scenarios

- Register
- Login
- Upload
- Process
- Ask Question
- Delete Document

---

## Performance Testing

Measure

- Upload Speed
- Query Latency
- Vector Search Speed
- Concurrent Users

---

# 45. Deployment Architecture

```
                Internet
                    │
                    ▼
              Nginx Reverse Proxy
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   Next.js App   FastAPI API   Redis
                    │
        ┌───────────┼───────────┐
        ▼                       ▼
 PostgreSQL               ChromaDB
        │
        ▼
 Local Document Storage
```

Deployment Components

- Docker
- Docker Compose
- Nginx
- SSL Certificates
- Environment Variables

Future

- Kubernetes
- AWS ECS
- CI/CD Pipeline

---

# 46. Future Scope

Atlas intentionally focuses on **Naive RAG**. Future enhancements may evolve it into more advanced systems.

### Short-Term Enhancements

- Folder Organization
- Document Tags
- OCR for Scanned PDFs
- Export Chat
- Share Documents
- Bulk Upload
- Multi-file Querying

---

### Medium-Term Enhancements

- Hybrid Search (BM25 + Vector)
- Reranking Models
- Better Chunking Strategies
- Streaming Uploads
- Document Versioning

---

### Long-Term Enhancements

- Graph RAG
- Agentic Workflows
- Self-RAG
- Adaptive Retrieval
- Multimodal Retrieval
- Enterprise Knowledge Bases
- Team Workspaces
- Role-Based Access Control

---

# 47. Development Guidelines

All contributors should follow these practices.

## Code Quality

- Type-safe code
- Strong typing
- Clear naming conventions
- Modular architecture
- Reusable components
- Comprehensive documentation

---

## Git Workflow

Branch Strategy

- main
- develop
- feature/\*
- fix/\*
- release/\*

Commit Style

- feat:
- fix:
- refactor:
- docs:
- test:
- chore:

---

## Documentation Standards

Every module should include

- Purpose
- Dependencies
- Inputs
- Outputs
- Error Cases
- Usage Examples

---

# 48. Deliverables

The completed Atlas project will include:

## Source Code

- Frontend (Next.js)
- Backend (FastAPI)
- AI Services
- Database Migrations
- Docker Configuration

---

## Documentation

- README.md
- PROJECT.md
- SRS.md
- DFD.md
- Development-Roadmap.md
- API Documentation
- Architecture Diagrams

---

## Deployment

- Docker Compose
- Production Configuration
- Environment Templates

---

## Testing

- Unit Tests
- Integration Tests
- End-to-End Tests

---

# 49. Project Milestones

| Milestone | Description                  |
| --------- | ---------------------------- |
| M1        | Project Setup                |
| M2        | Authentication Module        |
| M3        | Document Upload & Storage    |
| M4        | Document Processing Pipeline |
| M5        | Embedding & Vector Database  |
| M6        | Semantic Retrieval           |
| M7        | AI Chat Interface            |
| M8        | Dashboard & Library          |
| M9        | Testing & Optimization       |
| M10       | Deployment & Documentation   |

---

# 50. Conclusion

Atlas is a production-oriented implementation of a **Naive Retrieval-Augmented Generation (Naive RAG)** system. It demonstrates how modern AI applications can transform static document collections into interactive knowledge bases through semantic retrieval and grounded language model responses.

Beyond serving as a functional personal document library, Atlas is intended as the foundational project in a broader RAG portfolio. Its architecture emphasizes modularity, maintainability, and extensibility, allowing more advanced retrieval techniques—such as Hybrid RAG, Graph RAG, Agentic RAG, Self-RAG, and Adaptive RAG—to be explored in future projects without redesigning the core system.

By combining a modern web stack, scalable backend services, vector search, and configurable language models, Atlas provides both a practical productivity tool and a comprehensive reference implementation for learning Retrieval-Augmented Generation.
