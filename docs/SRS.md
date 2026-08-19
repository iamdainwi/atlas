# Software Requirements Specification (SRS)

# Atlas

**Version:** 1.0.0

**Status:** Draft

**Project Type:** Full Stack AI SaaS

**Architecture:** Naive Retrieval-Augmented Generation (Naive RAG)

---

# Revision History

| Version | Date | Description          | Author           |
| ------- | ---- | -------------------- | ---------------- |
| 0.1     | TBD  | Initial Draft        | Development Team |
| 0.5     | TBD  | Feature Complete     | Development Team |
| 1.0     | TBD  | First Stable Release | Development Team |

---

# Table of Contents

1. Introduction
2. Overall Description
3. Functional Requirements
4. External Interface Requirements
5. Non-Functional Requirements
6. Data Requirements
7. Use Cases
8. Acceptance Criteria
9. Assumptions & Constraints
10. Appendix

---

# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the complete software requirements for **Atlas**, an AI-powered Personal Document Library built using the **Naive Retrieval-Augmented Generation (Naive RAG)** architecture.

The purpose of this document is to provide developers, designers, testers, project managers, and future contributors with a precise and comprehensive description of the system's expected behavior, requirements, interfaces, constraints, and quality attributes.

This document serves as the primary reference for the design, development, testing, deployment, and maintenance of Atlas.

---

## 1.2 Scope

Atlas enables users to upload personal documents and interact with them using natural language.

Instead of relying on traditional keyword search, Atlas uses semantic retrieval to locate relevant document passages before generating AI-assisted responses.

The system supports the following document formats:

- PDF
- DOCX
- TXT
- Markdown (.md)

Atlas performs the following major operations:

- User Authentication
- Document Upload
- Text Extraction
- Document Chunking
- Embedding Generation
- Vector Storage
- Semantic Retrieval
- AI Question Answering
- Conversation Management
- Document Organization

Atlas intentionally implements only the **Naive RAG** architecture.

Advanced retrieval techniques such as Hybrid RAG, Graph RAG, Self-RAG, Agentic RAG, and Adaptive RAG are outside the scope of this project.

---

## 1.3 Intended Audience

This document is intended for:

### Software Developers

To understand the functional and technical requirements.

### Frontend Developers

To implement the user interface.

### Backend Developers

To implement APIs and business logic.

### AI Engineers

To implement retrieval, embeddings, and prompt generation.

### QA Engineers

To create test cases and validation criteria.

### DevOps Engineers

To deploy and maintain the application.

### Future Contributors

To understand the architecture before extending the project.

---

## 1.4 Definitions

| Term            | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| RAG             | Retrieval-Augmented Generation                              |
| Naive RAG       | Basic retrieval pipeline without reranking or hybrid search |
| Embedding       | Numerical vector representation of text                     |
| Chunk           | Small segment of a document used for retrieval              |
| Vector Database | Database optimized for similarity search                    |
| Semantic Search | Search based on meaning instead of keywords                 |
| LLM             | Large Language Model                                        |
| Context         | Retrieved document chunks sent to the LLM                   |
| Prompt          | Final instruction sent to the language model                |

---

## 1.5 References

The following documents are related to Atlas:

- PROJECT.md
- Development Roadmap
- DFD
- API Documentation
- FastAPI Documentation
- Next.js Documentation
- ChromaDB Documentation
- PostgreSQL Documentation

---

# 2. Overall Description

## 2.1 Product Perspective

Atlas is a standalone AI-powered web application.

The application consists of three primary layers:

```
Presentation Layer

↓

Application Layer

↓

Data Layer
```

### Presentation Layer

Responsible for:

- User Interface
- User Interaction
- State Management

Technology:

- Next.js
- React
- TypeScript

---

### Application Layer

Responsible for:

- Business Logic
- Authentication
- AI Processing
- Retrieval
- REST APIs

Technology:

- FastAPI

---

### Data Layer

Responsible for:

- User Data
- Metadata
- Embeddings
- Documents

Components:

- PostgreSQL
- ChromaDB
- Local Storage

---

## 2.2 Product Functions

Atlas provides the following major capabilities.

### Authentication

The system shall:

- Register users
- Authenticate users
- Manage sessions
- Authorize requests

---

### Document Management

The system shall:

- Upload documents
- Validate documents
- Store documents
- Delete documents
- Rename documents
- List documents

---

### Processing Pipeline

The system shall:

- Extract text
- Clean extracted content
- Generate chunks
- Create embeddings
- Store vectors

---

### Retrieval

The system shall:

- Generate query embeddings
- Perform similarity search
- Retrieve relevant chunks
- Return contextual information

---

### AI Chat

The system shall:

- Accept natural language questions
- Build prompts
- Query LLM
- Display grounded responses
- Cite document sources

---

### Settings

The system shall allow users to configure:

- Preferred LLM
- Embedding Model
- Temperature
- Top-K Retrieval
- Theme

---

## 2.3 User Classes

Atlas supports one primary user role.

### Registered User

Permissions:

- Upload documents
- Delete documents
- View documents
- Search documents
- Chat with documents
- Update profile
- Modify settings

---

### Administrator (Future)

Permissions:

- Manage users
- Manage storage
- View analytics
- Configure global AI settings

---

## 2.4 Operating Environment

### Client

Supported Browsers:

- Chrome
- Firefox
- Edge
- Safari

Operating Systems:

- Windows
- macOS
- Linux

Responsive Devices:

- Desktop
- Tablet
- Mobile

---

### Server

Operating System:

Ubuntu Linux

Runtime:

Python 3.12+

Application Server:

Uvicorn

Containerization:

Docker

---

### Database

PostgreSQL

Version:

16+

---

### Vector Database

ChromaDB

Latest Stable Release

---

## 2.5 Design Constraints

Atlas shall follow the following constraints.

### Architecture

- Clean Architecture
- Layered Architecture
- Modular Design

---

### Backend

Must use:

- FastAPI

---

### Frontend

Must use:

- Next.js
- TypeScript

---

### Authentication

Must use:

- JWT

---

### Database

Must use:

- PostgreSQL

---

### Vector Storage

Must use:

- ChromaDB

---

### Supported File Types

Only:

- PDF
- DOCX
- TXT
- Markdown

---

## 2.6 Assumptions

The following assumptions are made.

- Users possess stable internet connectivity.
- Users upload only supported document types.
- AI provider APIs are available.
- Embedding models are accessible.
- PostgreSQL is operational.
- ChromaDB is operational.
- Local storage has sufficient capacity.

---

## 2.7 Dependencies

Atlas depends on:

### AI Providers

- Gemini
- OpenAI
- Ollama
- Claude
- OpenRouter

---

### Python Libraries

- PyMuPDF
- python-docx
- sentence-transformers
- langchain
- chromadb

---

### JavaScript Libraries

- React
- Next.js
- Zustand
- Tailwind CSS
- TanStack Query

---

# 3. System Overview

Atlas consists of the following major subsystems.

```
Authentication

↓

Document Management

↓

Document Processing

↓

Embedding Generation

↓

Vector Database

↓

Semantic Retrieval

↓

Prompt Builder

↓

LLM

↓

Chat Interface
```

Each subsystem operates independently while communicating through well-defined interfaces.

---

# 4. System Context

```
                User

                  │

                  ▼

              Frontend

                  │

                  ▼

             FastAPI API

        ┌─────────┼──────────┐

        ▼         ▼          ▼

 Authentication  Storage   Retrieval

        │         │          │

        ▼         ▼          ▼

 PostgreSQL   ChromaDB    LLM APIs
```

---

# 5. High-Level Requirements

Atlas shall satisfy the following high-level objectives.

### HR-01

Provide secure authentication.

---

### HR-02

Support uploading supported documents.

---

### HR-03

Automatically process uploaded documents.

---

### HR-04

Generate vector embeddings.

---

### HR-05

Store vectors efficiently.

---

### HR-06

Retrieve semantically relevant chunks.

---

### HR-07

Generate grounded AI responses.

---

### HR-08

Maintain user conversations.

---

### HR-09

Provide configurable AI settings.

---

### HR-10

Deliver responsive user experience.

---

# 6. Functional Requirements

This section defines the functional behavior of Atlas.

Each requirement has a unique identifier.

Requirement Priorities

- Critical
- High
- Medium
- Low

---

# 6.1 Authentication Requirements

## FR-001 User Registration

**Priority**

Critical

**Description**

The system shall allow new users to create an account.

**Preconditions**

None

**Postconditions**

A new user account is created.

**Acceptance Criteria**

- Valid email required
- Password validation passed
- Duplicate email rejected
- User stored successfully

---

## FR-002 User Login

Priority

Critical

Description

The system shall authenticate registered users.

Acceptance Criteria

- Email verified
- Password verified
- JWT generated
- Refresh token generated

---

## FR-003 Google Authentication

Priority

High

Description

The system shall allow authentication using Google OAuth.

---

## FR-004 Logout

Priority

Critical

Description

The system shall terminate the user's session.

Acceptance Criteria

- Refresh token revoked
- Session invalidated

---

## FR-005 Password Reset

Priority

Medium

Description

The system shall allow users to reset forgotten passwords.

---

## FR-006 Profile Update

Priority

Medium

Description

Users shall be able to update

- Name
- Avatar
- Password

---

# 6.2 Document Management Requirements

## FR-007 Upload Document

Priority

Critical

Description

Users shall upload supported documents.

Supported Formats

- PDF
- DOCX
- TXT
- Markdown

Validation

- File extension
- File size
- MIME type

---

## FR-008 Document Validation

Priority

Critical

Description

Uploaded documents shall be validated before processing.

Validation Rules

- Supported type
- Not empty
- Maximum size
- Safe filename

---

## FR-009 Store Document

Priority

Critical

Description

Validated documents shall be stored securely.

Stored Information

- File
- Metadata
- Owner
- Upload time

---

## FR-010 List Documents

Priority

Critical

Description

Users shall view all uploaded documents.

Displayed Information

- Name
- Upload Date
- File Type
- Processing Status
- Size

---

## FR-011 Delete Document

Priority

Critical

Description

Users shall delete uploaded documents.

Deletion includes

- Original file
- Metadata
- Chunks
- Embeddings

---

## FR-012 Rename Document

Priority

Medium

Description

Users shall rename stored documents.

---

## FR-013 Search Documents

Priority

High

Description

Users shall search documents by

- Title
- Filename
- Tags

---

## FR-014 Sort Documents

Priority

Medium

Supported Sorting

- Name
- Upload Date
- Size
- Processing Status

---

## FR-015 Filter Documents

Priority

Medium

Supported Filters

- File Type
- Upload Date
- Processing Status

---

# 6.3 Document Processing Requirements

## FR-016 Automatic Processing

Priority

Critical

Description

After upload the system shall automatically process documents.

Pipeline

Upload

↓

Extraction

↓

Cleaning

↓

Chunking

↓

Embeddings

↓

Storage

---

## FR-017 Text Extraction

Priority

Critical

Description

Atlas shall extract text from

- PDF
- DOCX
- TXT
- Markdown

---

## FR-018 Metadata Extraction

Priority

High

Extract

- Filename
- Page Count
- File Size
- Upload Time

---

## FR-019 Text Cleaning

Priority

High

The system shall

- Remove empty lines
- Normalize whitespace
- Preserve paragraphs
- Remove unsupported characters

---

## FR-020 Chunk Generation

Priority

Critical

Description

Documents shall be divided into overlapping chunks.

Default

Chunk Size

500 Tokens

Overlap

100 Tokens

---

## FR-021 Chunk Metadata

Priority

Critical

Each chunk shall contain

- Chunk ID
- Document ID
- Chunk Number
- Page Number
- Text

---

# 6.4 Embedding Requirements

## FR-022 Embedding Generation

Priority

Critical

The system shall generate embeddings for every chunk.

---

## FR-023 Query Embeddings

Priority

Critical

The system shall generate embeddings for user questions.

---

## FR-024 Embedding Storage

Priority

Critical

Generated embeddings shall be stored inside ChromaDB.

---

## FR-025 Embedding Model Selection

Priority

Medium

Users shall configure preferred embedding models.

---

# 6.5 Retrieval Requirements

## FR-026 Semantic Search

Priority

Critical

The system shall perform similarity search using vector embeddings.

---

## FR-027 Top-K Retrieval

Priority

Critical

The system shall retrieve the K most relevant chunks.

Default

K = 5

---

## FR-028 Similarity Threshold

Priority

Medium

Users may configure retrieval threshold.

---

## FR-029 Context Assembly

Priority

Critical

Retrieved chunks shall be merged before prompt generation.

---

## FR-030 Retrieval Metadata

Priority

High

Every retrieved chunk shall include

- Source
- Page Number
- Document Name

---

# 6.6 Prompt Construction Requirements

## FR-031 Prompt Template

Priority

Critical

The system shall construct prompts using

System Prompt

-

Retrieved Context

-

Conversation History

-

User Question

---

## FR-032 Token Budget

Priority

High

Prompt size shall remain within LLM limits.

---

## FR-033 Prompt Sanitization

Priority

Medium

Special characters shall be escaped when necessary.

---

# 6.7 AI Response Requirements

## FR-034 Generate Response

Priority

Critical

The system shall send prompts to the configured LLM.

---

## FR-035 Streaming Responses

Priority

High

Responses shall stream incrementally.

---

## FR-036 Markdown Rendering

Priority

High

Responses shall support Markdown formatting.

---

## FR-037 Code Highlighting

Priority

Medium

Code blocks shall use syntax highlighting.

---

## FR-038 Source Citation

Priority

Critical

Every answer shall display supporting document sources.

Displayed Information

- Document Name
- Page Number
- Chunk Number

---

## FR-039 Retry Response

Priority

Medium

Users shall regenerate responses.

---

# 6.8 Chat Requirements

## FR-040 Create Conversation

Priority

Critical

Users shall start new chats.

---

## FR-041 Conversation History

Priority

Critical

The system shall store chat history.

---

## FR-042 Rename Conversation

Priority

Medium

Users shall rename conversations.

---

## FR-043 Delete Conversation

Priority

High

Users shall permanently delete chats.

---

## FR-044 Continue Conversation

Priority

Critical

Users shall continue previous chats.

---

## FR-045 Export Conversation

Priority

Low

Users shall export conversations.

Supported Formats

- Markdown
- PDF (Future)

---

# 6.9 Settings Requirements

## FR-046 Theme Selection

Priority

Medium

Supported

- Light
- Dark
- System

---

## FR-047 LLM Configuration

Priority

High

Users shall configure

- Model
- Temperature
- Maximum Tokens

---

## FR-048 Retrieval Configuration

Priority

Medium

Users shall configure

- Top-K
- Chunk Size
- Chunk Overlap

---

## FR-049 API Keys

Priority

Medium

Users shall securely manage API keys.

---

## FR-050 User Preferences

Priority

Medium

Preferences shall persist across sessions.

---

# 7. Business Rules

## BR-001

Only authenticated users may upload documents.

---

## BR-002

A document belongs to exactly one user.

---

## BR-003

Only document owners may delete documents.

---

## BR-004

Deleted documents must remove associated embeddings.

---

## BR-005

A question cannot be processed unless at least one document has been indexed.

---

## BR-006

Users cannot access another user's documents.

---

## BR-007

Only supported document formats are accepted.

---

## BR-008

Only successfully processed documents are eligible for retrieval.

---

## BR-009

A failed processing job shall not create embeddings.

---

## BR-010

Every AI response must include at least one cited source if retrieval succeeds.

# 8. External Interface Requirements

This section defines how Atlas interacts with users, external systems, databases, storage services, and AI providers.

---

# 8.1 User Interface Requirements

The user interface shall be responsive, intuitive, and accessible across modern devices.

## UI-001 Authentication Interface

The system shall provide:

- Login Screen
- Registration Screen
- Forgot Password Screen
- Password Reset Screen
- Google Sign-In

---

## UI-002 Dashboard Interface

The dashboard shall display

- Total Documents
- Storage Usage
- Recent Documents
- Recent Conversations
- Processing Queue
- Quick Actions

---

## UI-003 Document Library Interface

The document library shall provide

- Grid View
- List View
- Search Bar
- Filters
- Sorting
- Upload Button
- Delete Action
- Rename Action
- Preview Action

---

## UI-004 Upload Interface

The upload page shall support

- Drag and Drop
- Browse Files
- Upload Progress
- Validation Errors
- Processing Status

---

## UI-005 Chat Interface

The chat interface shall provide

- Conversation Sidebar
- Chat Messages
- Message Input
- Streaming Responses
- Source References
- Markdown Rendering
- Copy Response
- Retry Response

---

## UI-006 Settings Interface

Users shall configure

- Theme
- LLM Provider
- Embedding Model
- Temperature
- Top-K
- Chunk Size
- API Keys

---

# 8.2 Software Interface Requirements

Atlas communicates with several software systems.

---

## SI-001 PostgreSQL

Purpose

Store structured application data.

Responsibilities

- User Accounts
- Documents
- Chats
- Settings
- Processing Jobs

Communication

SQLAlchemy ORM

---

## SI-002 ChromaDB

Purpose

Store embeddings.

Responsibilities

- Insert Vectors
- Delete Vectors
- Similarity Search

---

## SI-003 Local File Storage

Purpose

Store uploaded documents.

Operations

- Save
- Read
- Delete
- Rename

---

## SI-004 LLM Providers

Supported Providers

- Gemini
- OpenAI
- Anthropic Claude
- Ollama
- OpenRouter

Responsibilities

- Generate responses
- Stream responses

---

## SI-005 Embedding Models

Supported Models

- BAAI/bge-small-en-v1.5
- all-MiniLM-L6-v2
- nomic-embed-text

Responsibilities

- Chunk Embeddings
- Query Embeddings

---

# 8.3 API Interface Requirements

Atlas exposes REST APIs.

Authentication

JWT Bearer Token

Content Type

application/json

File Upload

multipart/form-data

---

## Authentication APIs

POST

```
/api/auth/register
```

POST

```
/api/auth/login
```

POST

```
/api/auth/logout
```

POST

```
/api/auth/refresh
```

---

## Document APIs

POST

```
/api/documents
```

GET

```
/api/documents
```

GET

```
/api/documents/{id}
```

PUT

```
/api/documents/{id}
```

DELETE

```
/api/documents/{id}
```

---

## Chat APIs

POST

```
/api/chat
```

POST

```
/api/chat/{id}/message
```

GET

```
/api/chat/{id}
```

DELETE

```
/api/chat/{id}
```

---

## Search API

POST

```
/api/search
```

---

## Settings API

GET

```
/api/settings
```

PUT

```
/api/settings
```

---

# 8.4 Hardware Requirements

## Minimum Client Requirements

CPU

Dual Core

Memory

4 GB RAM

Storage

500 MB Free Space

Internet

Broadband Connection

Browser

Latest Chrome, Firefox, Safari, or Edge

---

## Recommended Client

CPU

Quad Core

Memory

8 GB RAM

Browser

Latest Stable Version

---

## Server Requirements

CPU

4 Cores

Memory

8 GB RAM

Storage

100 GB SSD

Operating System

Ubuntu 22.04+

Docker

Latest Stable Release

---

# 9. Non-Functional Requirements

Non-functional requirements define the quality attributes of Atlas.

---

# 9.1 Performance Requirements

## NFR-001 Upload Performance

Priority

Critical

Requirement

The system shall upload a 50 MB document in under 10 seconds under normal network conditions.

---

## NFR-002 Processing Time

Priority

Critical

Requirement

Documents should be completely processed within 30 seconds for average-sized files.

---

## NFR-003 Query Response Time

Priority

Critical

Requirement

Average AI response time shall be less than 5 seconds excluding third-party API latency.

---

## NFR-004 Similarity Search

Priority

Critical

Requirement

Vector search shall complete within 500 milliseconds for collections up to 100,000 chunks.

---

## NFR-005 Dashboard Loading

Priority

High

Requirement

Dashboard shall load within 2 seconds.

---

# 9.2 Reliability Requirements

## NFR-006 Availability

Requirement

Application availability shall be at least

99%

Future Goal

99.9%

---

## NFR-007 Fault Recovery

Requirement

Unexpected failures shall not corrupt

- Documents
- Metadata
- Embeddings

---

## NFR-008 Backup

Requirement

Database backups shall be supported.

Future

Automatic scheduled backups.

---

# 9.3 Scalability Requirements

## NFR-009 Horizontal Scalability

Backend services shall support horizontal scaling.

---

## NFR-010 Storage Scalability

The storage architecture shall allow migration from local storage to cloud storage without application redesign.

---

## NFR-011 Vector Scalability

The vector database shall support migration to enterprise vector databases such as Pinecone or Milvus.

---

# 9.4 Security Requirements

## NFR-012 Authentication

Only authenticated users may access protected resources.

---

## NFR-013 Authorization

Users may access only their own

- Documents
- Chats
- Settings

---

## NFR-014 Password Security

Passwords shall be stored using

bcrypt

---

## NFR-015 Transport Security

All communication shall occur over HTTPS.

---

## NFR-016 Input Validation

All incoming requests shall be validated before processing.

---

## NFR-017 File Validation

Uploaded files shall be validated using

- MIME Type
- Extension
- Size

---

## NFR-018 JWT Security

JWT tokens shall have configurable expiration times.

---

# 9.5 Usability Requirements

## NFR-019 Ease of Use

The interface shall require no technical knowledge for basic usage.

---

## NFR-020 Responsive Design

The interface shall adapt to

- Desktop
- Tablet
- Mobile

---

## NFR-021 Accessibility

The interface shall follow WCAG 2.1 Level AA guidelines where practical.

---

## NFR-022 Theme Support

Users shall switch between

- Light
- Dark
- System Theme

---

# 9.6 Maintainability Requirements

## NFR-023 Modular Architecture

Application components shall remain independently maintainable.

---

## NFR-024 Documentation

Every public API and service shall be documented.

---

## NFR-025 Code Standards

The project shall follow

- SOLID Principles
- Clean Architecture
- Type Safety
- Static Analysis

---

# 9.7 Portability Requirements

## NFR-026 Containerization

Application deployment shall use Docker.

---

## NFR-027 Operating Systems

Backend shall run on

- Linux
- macOS
- Windows

---

## NFR-028 Database Independence

Business logic shall remain independent of database implementation.

---

# 9.8 Observability Requirements

## NFR-029 Logging

System logs shall include

- Authentication Events
- Upload Events
- Processing Events
- Retrieval Events
- Errors

---

## NFR-030 Monitoring

System shall expose metrics for

- API Latency
- Processing Time
- Memory Usage
- CPU Usage
- Error Rate

---

# 9.9 Compatibility Requirements

Atlas shall support

Browsers

- Chrome
- Firefox
- Edge
- Safari

File Types

- PDF
- DOCX
- TXT
- Markdown

Operating Systems

- Windows
- macOS
- Linux

---

# 9.10 Compliance Requirements

Atlas shall comply with

- REST API Best Practices
- HTTP Standards
- JSON Specification
- OAuth 2.0
- JWT Standards

---

# 10. Data Requirements

Atlas manages three categories of data.

## User Data

Includes

- Profile
- Preferences
- Authentication Information

---

## Document Data

Includes

- Original Files
- Metadata
- Processing Status
- Chunk Count

---

## AI Data

Includes

- Embeddings
- Vector Metadata
- Chat History
- Retrieval Results

---

## Data Retention

Documents remain stored until explicitly deleted by the owner.

Associated vectors, chunks, and metadata shall be permanently removed when the corresponding document is deleted.

---

## Data Integrity

The system shall maintain consistency between:

- Original Documents
- PostgreSQL Metadata
- ChromaDB Embeddings

No orphaned records or vectors shall remain after successful deletion.

# 11. Use Cases

This section describes how users interact with Atlas to accomplish specific goals.

---

# UC-001 User Registration

## Goal

Create a new Atlas account.

### Primary Actor

User

### Preconditions

- User is not registered.
- Internet connection is available.

### Trigger

User clicks **Register**.

### Main Flow

1. User enters name.
2. User enters email.
3. User enters password.
4. System validates input.
5. System creates account.
6. System stores user information.
7. System redirects user to login/dashboard.

### Alternative Flows

- Email already exists.
- Weak password.
- Invalid email format.

### Postconditions

- Account successfully created.

---

# UC-002 User Login

## Goal

Authenticate the user.

### Primary Actor

Registered User

### Main Flow

1. User enters credentials.
2. System validates credentials.
3. JWT token generated.
4. Session created.
5. Dashboard displayed.

### Exceptions

- Incorrect password.
- User not found.
- Server unavailable.

---

# UC-003 Upload Document

## Goal

Upload a supported document.

### Primary Actor

Authenticated User

### Preconditions

- User logged in.

### Main Flow

1. Open Upload page.
2. Select document.
3. Validate file.
4. Store file.
5. Start processing pipeline.
6. Show processing status.
7. Document becomes searchable.

### Alternative Flow

Invalid document type.

System rejects upload.

### Postconditions

Document stored successfully.

---

# UC-004 Process Document

## Goal

Convert uploaded document into searchable knowledge.

### Actor

System

### Main Flow

1. Read document.
2. Extract text.
3. Clean content.
4. Generate chunks.
5. Generate embeddings.
6. Store vectors.
7. Update processing status.

### Failure Cases

- Extraction failed.
- Embedding model unavailable.
- Vector database offline.

---

# UC-005 View Document Library

## Goal

Browse uploaded documents.

### Actor

Authenticated User

### Main Flow

1. Open Library.
2. Retrieve document list.
3. Display metadata.
4. Search, filter, or sort documents.

---

# UC-006 Ask Question

## Goal

Ask questions about uploaded documents.

### Actor

Authenticated User

### Preconditions

At least one processed document exists.

### Main Flow

1. User types question.
2. Query embedding generated.
3. Similarity search executed.
4. Top-K chunks retrieved.
5. Prompt constructed.
6. Prompt sent to LLM.
7. AI response returned.
8. Sources displayed.

### Alternative Flow

No relevant documents found.

System informs the user.

---

# UC-007 Continue Conversation

## Goal

Resume an existing chat.

### Main Flow

1. Open previous conversation.
2. Load messages.
3. Continue asking questions.
4. Maintain conversational context.

---

# UC-008 Delete Document

## Goal

Remove a document completely.

### Main Flow

1. User selects Delete.
2. Confirmation dialog displayed.
3. File deleted.
4. Metadata deleted.
5. Embeddings removed.
6. Library refreshed.

### Postconditions

Document no longer exists.

---

# UC-009 Configure AI Settings

## Goal

Customize Atlas behavior.

### User can modify

- Temperature
- LLM
- Embedding Model
- Top-K
- Theme

---

# UC-010 Logout

## Goal

End current session.

### Main Flow

1. User clicks Logout.
2. Tokens revoked.
3. Session terminated.
4. Redirect to Login.

---

# 12. Acceptance Criteria

The project will be accepted when all critical requirements are satisfied.

## Authentication

- User registration works.
- Login succeeds with valid credentials.
- Protected routes require authentication.
- Logout invalidates session.

---

## Document Management

- Supported files upload successfully.
- Invalid files are rejected.
- Documents appear in library.
- Documents can be deleted.
- Documents can be renamed.

---

## Processing Pipeline

- Text extraction succeeds.
- Chunk generation completes.
- Embeddings generated.
- ChromaDB updated.
- Metadata stored.

---

## Retrieval

- Semantic search returns relevant chunks.
- Retrieved chunks belong to the requesting user.
- Retrieval latency meets performance targets.

---

## AI Chat

- Questions receive grounded responses.
- Sources are displayed.
- Markdown renders correctly.
- Streaming responses function correctly.

---

## Settings

- Theme changes persist.
- AI settings persist.
- Retrieval settings are applied.

---

## Performance

- Upload latency within limits.
- Retrieval latency within limits.
- Dashboard loads efficiently.

---

## Security

- Unauthorized users cannot access resources.
- JWT validation works.
- Passwords are encrypted.
- File validation prevents unsupported uploads.

---

# 13. Assumptions

The following assumptions apply to Atlas.

- Users upload only supported document formats.
- Internet connectivity is available.
- AI provider APIs are operational.
- Vector database is available.
- Storage has sufficient free space.
- Authentication service is functioning correctly.

---

# 14. Constraints

## Technical Constraints

- FastAPI backend
- Next.js frontend
- PostgreSQL database
- ChromaDB vector database
- Local document storage
- JWT authentication

---

## Functional Constraints

Atlas supports only

- PDF
- DOCX
- TXT
- Markdown

Atlas implements only

- Naive RAG

Advanced retrieval strategies are intentionally excluded.

---

## Operational Constraints

- Internet required for cloud LLM providers.
- API keys required for commercial AI providers.
- Local storage capacity limits document library size.

---

# 15. Risks

| Risk                        | Impact | Mitigation                         |
| --------------------------- | ------ | ---------------------------------- |
| LLM API outage              | High   | Support multiple providers         |
| Embedding model unavailable | Medium | Configurable embedding models      |
| ChromaDB corruption         | High   | Regular backups                    |
| Large document uploads      | Medium | Background processing              |
| High API latency            | Medium | Streaming responses & caching      |
| Unauthorized access         | High   | JWT authentication & authorization |
| Storage exhaustion          | Medium | Monitor usage & cleanup            |

---

# 16. Requirement Traceability Matrix

| Requirement | Related Module      | Test Case  |
| ----------- | ------------------- | ---------- |
| FR-001      | Authentication      | TC-AUTH-01 |
| FR-007      | Document Upload     | TC-DOC-01  |
| FR-016      | Processing Pipeline | TC-PROC-01 |
| FR-022      | Embedding Service   | TC-EMB-01  |
| FR-026      | Retrieval Engine    | TC-RET-01  |
| FR-034      | LLM Service         | TC-AI-01   |
| FR-038      | Source Citation     | TC-AI-02   |
| FR-041      | Chat History        | TC-CHAT-01 |
| FR-046      | Theme               | TC-SET-01  |

---

# 17. Future Requirements

These requirements are intentionally excluded from Version 1.0 but may be included in future releases.

## Version 1.1

- Folder organization
- Bulk document upload
- Document tags
- OCR support for scanned PDFs

---

## Version 2.0

- Hybrid Search
- BM25 Retrieval
- Cross-document reasoning
- Document versioning

---

## Version 3.0

- Graph RAG
- Agentic RAG
- Multi-modal Retrieval
- Enterprise workspaces
- Team collaboration
- Role-based access control

---

# 18. Appendix

## Supported File Types

| Extension | Supported |
| --------- | --------- |
| PDF       | Yes       |
| DOCX      | Yes       |
| TXT       | Yes       |
| MD        | Yes       |

---

## Supported Browsers

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

---

## Supported Platforms

- Windows
- Linux
- macOS

---

## Abbreviations

| Abbreviation | Meaning                           |
| ------------ | --------------------------------- |
| API          | Application Programming Interface |
| JWT          | JSON Web Token                    |
| LLM          | Large Language Model              |
| OCR          | Optical Character Recognition     |
| RAG          | Retrieval-Augmented Generation    |
| UI           | User Interface                    |
| UX           | User Experience                   |
| DB           | Database                          |

---

# 19. Approval

| Role               | Responsibility                   |
| ------------------ | -------------------------------- |
| Product Owner      | Approves functional scope        |
| Software Architect | Approves system architecture     |
| Backend Lead       | Approves backend implementation  |
| Frontend Lead      | Approves frontend implementation |
| AI Engineer        | Approves RAG pipeline            |
| QA Lead            | Approves test coverage           |

---

# 20. Conclusion

This Software Requirements Specification defines the complete functional and non-functional requirements for **Atlas**, a production-oriented implementation of a Naive Retrieval-Augmented Generation system.

The requirements establish a clear contract between stakeholders and the development team, ensuring that the application is built with consistency, maintainability, scalability, and quality in mind. Together with the accompanying `PROJECT.md`, `DFD.md`, and `Development-Roadmap.md`, this SRS provides the foundation for the complete software development lifecycle—from planning and implementation to testing, deployment, and future enhancements.
