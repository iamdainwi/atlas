# API Specification

# Atlas

**Version:** 1.0.0

**Architecture:** REST API

**Backend Framework:** FastAPI

**Authentication:** JWT + Refresh Token

**Content Type:** JSON

**API Version:** v1

---

# Table of Contents

1. API Overview
2. API Standards
3. Authentication
4. Request & Response Format
5. HTTP Status Codes
6. Error Handling
7. Rate Limiting
8. Authentication APIs
9. User APIs

---

# 1. API Overview

Atlas exposes a RESTful API that enables clients to interact with every component of the application.

The API is designed around the following principles:

- RESTful Architecture
- Stateless Communication
- JSON Responses
- JWT Authentication
- Versioned Endpoints
- Consistent Error Format
- Predictable Resource Naming

---

# Base URL

Development

```
http://localhost:8000/api/v1
```

Production

```
https://atlas.example.com/api/v1
```

---

# Content Types

Request

```
application/json
```

File Upload

```
multipart/form-data
```

Response

```
application/json
```

---

# API Versioning

Current Version

```
v1
```

Example

```
/api/v1/documents
```

Future versions

```
/api/v2/documents
```

---

# API Naming Convention

Resources are plural nouns.

Examples

```
/users

/documents

/chats

/messages

/settings
```

HTTP verbs define actions.

| Method | Action         |
| ------ | -------------- |
| GET    | Read           |
| POST   | Create         |
| PUT    | Replace        |
| PATCH  | Partial Update |
| DELETE | Delete         |

---

# 2. API Standards

## Authentication

Protected endpoints require

```
Authorization: Bearer <JWT_TOKEN>
```

---

## Time Format

All timestamps follow

ISO 8601

Example

```json
{
  "created_at": "2026-08-10T14:22:01Z"
}
```

---

## UUID Format

Every primary resource uses UUID.

Example

```
fdcb46e2-72ef-47f6-baf8-44eb8f99dd73
```

---

## Pagination

List endpoints support

```
?page=1

&limit=20
```

---

## Sorting

```
?sort=name

?sort=-created_at
```

Descending order

```
-
```

Ascending order

Default

---

## Filtering

Example

```
?type=pdf

?status=processed
```

---

## Search

```
?q=machine learning
```

---

# 3. Authentication

Atlas uses JWT authentication.

Workflow

```
Register

↓

Login

↓

Access Token

↓

Protected APIs

↓

Refresh Token

↓

New Access Token
```

---

# Access Token

Purpose

Authenticate requests.

Lifetime

15 Minutes

---

# Refresh Token

Purpose

Generate new access token.

Lifetime

7 Days

---

# Authorization Header

```
Authorization: Bearer eyJhbGci...
```

---

# Protected Endpoints

Require JWT

```
GET /documents

POST /chat

GET /settings
```

---

# Public Endpoints

No authentication required.

```
POST /register

POST /login

POST /forgot-password
```

---

# 4. Standard Response Format

Successful Response

```json
{
  "success": true,
  "message": "Operation successful",
  "data": {}
}
```

---

Failed Response

```json
{
  "success": false,
  "error": {
    "code": "DOCUMENT_NOT_FOUND",
    "message": "Document does not exist"
  }
}
```

---

Validation Error

```json
{
  "success": false,
  "errors": [
    {
      "field": "email",
      "message": "Invalid email address"
    }
  ]
}
```

---

# 5. HTTP Status Codes

| Code | Meaning                |
| ---- | ---------------------- |
| 200  | OK                     |
| 201  | Created                |
| 204  | No Content             |
| 400  | Bad Request            |
| 401  | Unauthorized           |
| 403  | Forbidden              |
| 404  | Not Found              |
| 409  | Conflict               |
| 413  | Payload Too Large      |
| 415  | Unsupported Media Type |
| 422  | Validation Error       |
| 429  | Too Many Requests      |
| 500  | Internal Server Error  |
| 503  | Service Unavailable    |

---

# 6. Error Codes

Authentication

```
INVALID_CREDENTIALS

TOKEN_EXPIRED

TOKEN_INVALID

UNAUTHORIZED
```

---

Documents

```
DOCUMENT_NOT_FOUND

DOCUMENT_EXISTS

INVALID_FILE

FILE_TOO_LARGE

PROCESSING_FAILED
```

---

Retrieval

```
NO_DOCUMENTS

NO_MATCH_FOUND

VECTOR_DATABASE_ERROR
```

---

AI

```
LLM_UNAVAILABLE

PROMPT_TOO_LARGE

RATE_LIMITED

GENERATION_FAILED
```

---

Database

```
DATABASE_ERROR

CONNECTION_FAILED
```

---

# 7. Rate Limiting

Authentication

```
10 requests/minute
```

---

Document Upload

```
20 uploads/hour
```

---

AI Chat

```
60 messages/hour
```

---

Search

```
100 requests/minute
```

---

Exceeded Limit

```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many requests."
  }
}
```

---

# 8. Authentication APIs

---

## Register User

```
POST /auth/register
```

Description

Create a new user account.

---

Request

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "StrongPassword123"
}
```

---

Success

```
201 Created
```

Response

```json
{
  "success": true,
  "message": "Account created successfully.",
  "data": {
    "id": "uuid",
    "email": "john@example.com"
  }
}
```

---

Errors

```
409 Email Already Exists

422 Validation Error
```

---

## Login

```
POST /auth/login
```

---

Request

```json
{
  "email": "john@example.com",
  "password": "StrongPassword123"
}
```

---

Response

```json
{
  "success": true,
  "data": {
    "access_token": "...",
    "refresh_token": "...",
    "expires_in": 900
  }
}
```

---

Errors

```
401 Invalid Credentials

423 Account Locked
```

---

## Refresh Token

```
POST /auth/refresh
```

---

Request

```json
{
  "refresh_token": "..."
}
```

---

Response

```json
{
  "access_token": "...",
  "expires_in": 900
}
```

---

## Logout

```
POST /auth/logout
```

Requires Authentication

---

Response

```
204 No Content
```

---

## Forgot Password

```
POST /auth/forgot-password
```

---

Request

```json
{
  "email": "john@example.com"
}
```

---

Response

```json
{
  "success": true,
  "message": "Password reset email sent."
}
```

---

## Reset Password

```
POST /auth/reset-password
```

---

Request

```json
{
  "token": "reset-token",
  "password": "NewPassword123"
}
```

---

Response

```json
{
  "success": true,
  "message": "Password updated successfully."
}
```

---

# 9. User APIs

---

## Get Current User

```
GET /users/me
```

Authentication

Required

---

Response

```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "name": "John Doe",
    "email": "john@example.com",
    "avatar": "...",
    "created_at": "..."
  }
}
```

---

## Update Profile

```
PUT /users/me
```

---

Request

```json
{
  "name": "John Smith",
  "avatar": "https://..."
}
```

---

Response

```json
{
  "success": true,
  "message": "Profile updated."
}
```

---

## Change Password

```
PATCH /users/me/password
```

---

Request

```json
{
  "current_password": "OldPassword",
  "new_password": "NewPassword123"
}
```

---

Response

```json
{
  "success": true,
  "message": "Password changed successfully."
}
```

---

## Delete Account

```
DELETE /users/me
```

Description

Deletes the user account along with all associated resources.

Deletes

- User
- Documents
- Chats
- Embeddings
- Settings

---

Response

```
204 No Content
```

# 10. Document APIs

This section defines all endpoints related to document management.

---

## Upload Document

```
POST /documents
```

### Description

Uploads a document and starts the document processing pipeline asynchronously.

### Authentication

Required

### Content-Type

```
multipart/form-data
```

### Request

| Field | Type          | Required |
| ----- | ------------- | -------- |
| file  | File          | Yes      |
| title | String        | No       |
| tags  | Array[String] | No       |

### Supported Formats

- PDF
- DOCX
- TXT
- Markdown

### Example Response

```json
{
  "success": true,
  "message": "Document uploaded successfully.",
  "data": {
    "id": "4f2ab7fd",
    "title": "Introduction to RAG",
    "status": "processing"
  }
}
```

### Errors

```
400 Invalid File

401 Unauthorized

413 File Too Large

415 Unsupported Media Type
```

---

## List Documents

```
GET /documents
```

### Description

Returns all documents belonging to the authenticated user.

### Authentication

Required

### Query Parameters

| Parameter | Type    | Description       |
| --------- | ------- | ----------------- |
| page      | Integer | Page Number       |
| limit     | Integer | Items Per Page    |
| sort      | String  | Sort Field        |
| type      | String  | Filter by Type    |
| status    | String  | Processing Status |
| q         | String  | Search by Name    |

### Example

```
GET /documents?page=1&limit=20&type=pdf
```

### Response

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "doc001",
        "title": "RAG Notes",
        "file_type": "pdf",
        "status": "processed",
        "pages": 42,
        "chunks": 158,
        "uploaded_at": "2026-08-15T10:12:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 37
    }
  }
}
```

---

## Get Document Details

```
GET /documents/{document_id}
```

### Description

Returns metadata of a specific document.

### Authentication

Required

### Response

```json
{
  "success": true,
  "data": {
    "id": "doc001",
    "title": "Machine Learning Notes",
    "filename": "ml.pdf",
    "size": 2458123,
    "pages": 75,
    "chunks": 296,
    "status": "processed",
    "uploaded_at": "2026-08-10T08:10:22Z"
  }
}
```

---

## Rename Document

```
PATCH /documents/{document_id}
```

### Request

```json
{
  "title": "Deep Learning Notes"
}
```

### Response

```json
{
  "success": true,
  "message": "Document renamed successfully."
}
```

---

## Delete Document

```
DELETE /documents/{document_id}
```

### Description

Deletes

- Original document
- Metadata
- Chunks
- Embeddings

### Response

```
204 No Content
```

---

## Download Document

```
GET /documents/{document_id}/download
```

### Description

Downloads the original uploaded file.

### Response

Binary File

---

## Preview Document

```
GET /documents/{document_id}/preview
```

### Description

Returns preview data for the document.

### Response

```json
{
  "title": "RAG Guide",
  "pages": 40,
  "preview": "Retrieval-Augmented Generation is..."
}
```

---

# 11. Processing APIs

These APIs expose the document ingestion pipeline.

---

## Get Processing Status

```
GET /documents/{document_id}/status
```

### Response

```json
{
  "status": "processing",
  "progress": 65,
  "current_step": "Generating Embeddings"
}
```

---

## Processing States

Possible values

```
uploaded

validating

extracting

cleaning

chunking

embedding

storing

processed

failed
```

---

## Get Processing Log

```
GET /documents/{document_id}/logs
```

### Response

```json
{
  "events": [
    {
      "step": "Extraction",
      "status": "Completed"
    },
    {
      "step": "Chunking",
      "status": "Completed"
    }
  ]
}
```

---

# 12. Search APIs

---

## Semantic Search

```
POST /search
```

### Description

Performs semantic retrieval without invoking the LLM.

Useful for debugging retrieval quality.

### Request

```json
{
  "query": "Explain retrieval augmented generation",
  "top_k": 5
}
```

### Response

```json
{
  "success": true,
  "data": [
    {
      "document_id": "doc001",
      "page": 12,
      "score": 0.93,
      "text": "Retrieval-Augmented Generation..."
    }
  ]
}
```

---

## Search Documents

```
GET /search/documents
```

### Description

Search document metadata.

### Query Parameters

```
?q=transformer
```

---

## Search Chunks

```
GET /search/chunks
```

### Description

Search indexed chunks directly.

---

# 13. Retrieval APIs

---

## Retrieve Context

```
POST /retrieval/context
```

### Description

Returns retrieved chunks before prompt construction.

### Request

```json
{
  "query": "Explain embeddings",
  "top_k": 5
}
```

### Response

```json
{
  "chunks": [
    {
      "document": "AI Notes",
      "page": 18,
      "chunk": 45,
      "score": 0.94,
      "content": "Embeddings convert text..."
    }
  ]
}
```

---

## Generate Query Embedding

```
POST /retrieval/query-embedding
```

### Description

Generates an embedding for a query.

Primarily intended for debugging and development.

### Request

```json
{
  "query": "Vector databases"
}
```

### Response

```json
{
  "dimension": 768,
  "embedding_generated": true
}
```

---

# 14. Library APIs

---

## Get Storage Statistics

```
GET /library/storage
```

### Response

```json
{
  "documents": 48,
  "storage_used": "820 MB",
  "remaining_storage": "9.2 GB"
}
```

---

## Get Recent Documents

```
GET /library/recent
```

### Response

```json
{
  "documents": [
    {
      "title": "FastAPI Guide",
      "uploaded_at": "2026-08-15T09:10:00Z"
    }
  ]
}
```

---

## Get Document Types

```
GET /library/types
```

### Response

```json
{
  "pdf": 24,
  "docx": 8,
  "txt": 10,
  "markdown": 6
}
```

---

# 15. Pagination Standard

Every paginated endpoint returns

```json
{
  "pagination": {
    "page": 1,
    "limit": 20,
    "total_items": 154,
    "total_pages": 8,
    "has_next": true,
    "has_previous": false
  }
}
```

---

# 16. Sorting Standard

Ascending

```
?sort=name
```

Descending

```
?sort=-created_at
```

Supported Fields

- name
- created_at
- updated_at
- size
- pages
- chunks

---

# 17. Filtering Standard

Examples

```
?type=pdf

?status=processed

?status=processing

?pages_gt=50

?size_lt=5000000
```

Multiple filters

```
?type=pdf&status=processed
```

---

# 18. API Workflow (Document Upload)

```
POST /documents

↓

Validate File

↓

Store Original Document

↓

Create Metadata

↓

Start Background Processing

↓

Return

202 Accepted
```

---

# 19. API Workflow (Semantic Search)

```
POST /search

↓

Generate Query Embedding

↓

Search ChromaDB

↓

Return Top-K Chunks
```

---

# 20. API Workflow (Retrieval Pipeline)

```
Question

↓

Generate Query Embedding

↓

Similarity Search

↓

Retrieve Context

↓

Return Chunks
```

# 21. Chat APIs

This section defines all endpoints related to conversations with Atlas.

---

## Create Chat

```
POST /chats
```

### Description

Creates a new conversation.

### Authentication

Required

### Request

```json
{
  "title": "Research Discussion"
}
```

### Response

```json
{
  "success": true,
  "data": {
    "id": "chat_001",
    "title": "Research Discussion",
    "created_at": "2026-08-15T14:20:00Z"
  }
}
```

---

## List Chats

```
GET /chats
```

### Query Parameters

| Parameter | Description      |
| --------- | ---------------- |
| page      | Page Number      |
| limit     | Results Per Page |
| q         | Search Title     |
| sort      | Sort Chats       |

---

### Response

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "chat001",
        "title": "Machine Learning",
        "updated_at": "2026-08-15T10:00:00Z"
      }
    ]
  }
}
```

---

## Get Chat

```
GET /chats/{chat_id}
```

### Description

Returns conversation metadata.

---

## Rename Chat

```
PATCH /chats/{chat_id}
```

### Request

```json
{
  "title": "RAG Research"
}
```

---

## Delete Chat

```
DELETE /chats/{chat_id}
```

### Description

Deletes

- Chat
- Messages

Response

```
204 No Content
```

---

# 22. Message APIs

---

## Send Message

```
POST /chats/{chat_id}/messages
```

### Description

Processes a user message using the complete Naive RAG pipeline.

Pipeline

```
Question

↓

Query Embedding

↓

Similarity Search

↓

Retrieve Chunks

↓

Prompt Builder

↓

LLM

↓

Response
```

---

### Request

```json
{
  "message": "Explain Retrieval-Augmented Generation."
}
```

---

### Response

```json
{
  "success": true,
  "data": {
    "message_id": "msg001",
    "role": "assistant",
    "content": "Retrieval-Augmented Generation (RAG)...",
    "sources": [
      {
        "document": "RAG Guide.pdf",
        "page": 7,
        "chunk": 18
      }
    ]
  }
}
```

---

## Get Messages

```
GET /chats/{chat_id}/messages
```

### Description

Returns complete conversation history.

---

## Delete Message

```
DELETE /messages/{message_id}
```

### Description

Deletes a single message from a conversation.

---

## Regenerate Response

```
POST /messages/{message_id}/regenerate
```

### Description

Regenerates the previous assistant response using the same user message.

---

# 23. Streaming API

Atlas supports Server-Sent Events (SSE) for real-time AI responses.

---

## Stream Response

```
POST /chats/{chat_id}/stream
```

### Content Type

```
text/event-stream
```

### Event Sequence

```
message_start

↓

token

↓

token

↓

token

↓

sources

↓

message_end
```

---

### Example

```
event: token

data: Retrieval

event: token

data: Augmented

event: token

data: Generation
```

---

# 24. LLM APIs

These endpoints are primarily intended for administration and diagnostics.

---

## Get Available Models

```
GET /llm/models
```

### Response

```json
{
  "providers": ["Gemini", "OpenAI", "Claude", "Ollama"]
}
```

---

## Test LLM Connection

```
POST /llm/test
```

### Description

Checks whether the configured LLM provider is reachable.

---

### Response

```json
{
  "provider": "Gemini",
  "status": "Connected"
}
```

---

# 25. Settings APIs

---

## Get Settings

```
GET /settings
```

### Response

```json
{
  "theme": "dark",
  "llm_provider": "Gemini",
  "embedding_model": "BAAI/bge-small-en-v1.5",
  "temperature": 0.2,
  "top_k": 5
}
```

---

## Update Settings

```
PUT /settings
```

### Request

```json
{
  "theme": "light",
  "temperature": 0.4,
  "top_k": 8
}
```

---

## Reset Settings

```
POST /settings/reset
```

### Description

Restores all user settings to default values.

---

# 26. Health APIs

---

## Health Check

```
GET /health
```

### Response

```json
{
  "status": "healthy"
}
```

---

## Readiness Check

```
GET /health/ready
```

Checks

- PostgreSQL
- ChromaDB
- Local Storage
- LLM Provider

---

## Liveness Check

```
GET /health/live
```

Used by

- Docker
- Kubernetes
- Load Balancers

---

# 27. Administration APIs

These endpoints are reserved for future administrator functionality.

---

## Dashboard Statistics

```
GET /admin/statistics
```

Returns

- Total Users
- Total Documents
- Total Chats
- Storage Usage

---

## Processing Queue

```
GET /admin/jobs
```

Returns

- Running Jobs
- Failed Jobs
- Completed Jobs

---

## Retry Processing Job

```
POST /admin/jobs/{job_id}/retry
```

---

# 28. Webhook Events (Future)

Atlas may publish events for external integrations.

Examples

```
document.uploaded

document.processed

document.deleted

chat.created

chat.completed
```

---

# 29. API Security

All protected endpoints require:

- JWT Authentication
- Ownership Validation
- Request Validation

---

### Request Validation

Every request is validated for:

- Required fields
- Data types
- Length limits
- Allowed values

---

### File Upload Validation

Atlas validates:

- Extension
- MIME type
- Maximum file size
- Filename

---

### Prompt Protection

The backend sanitizes retrieved context before prompt construction to reduce prompt injection risks.

---

# 30. API Documentation

Atlas automatically exposes OpenAPI documentation.

Swagger UI

```
GET /docs
```

ReDoc

```
GET /redoc
```

OpenAPI Schema

```
GET /openapi.json
```

---

# 31. Versioning Policy

Current

```
v1
```

Future

```
v2
```

Breaking changes are introduced only in a new API version.

Older versions remain supported during a defined deprecation period.

---

# 32. Deprecation Policy

Deprecated endpoints include response headers indicating:

- Deprecation status
- Sunset date
- Replacement endpoint

Example

```
Deprecation: true

Sunset: 2027-01-01
```

---

# 33. API Lifecycle

```
Client

↓

Authentication

↓

Authorization

↓

Validation

↓

Business Logic

↓

Database / Vector Database

↓

LLM

↓

Response Formatter

↓

JSON Response
```

---

# 34. Complete API Endpoint Summary

## Authentication

- POST /auth/register
- POST /auth/login
- POST /auth/logout
- POST /auth/refresh
- POST /auth/forgot-password
- POST /auth/reset-password

---

## Users

- GET /users/me
- PUT /users/me
- PATCH /users/me/password
- DELETE /users/me

---

## Documents

- POST /documents
- GET /documents
- GET /documents/{id}
- PATCH /documents/{id}
- DELETE /documents/{id}
- GET /documents/{id}/download
- GET /documents/{id}/preview
- GET /documents/{id}/status
- GET /documents/{id}/logs

---

## Search

- POST /search
- GET /search/documents
- GET /search/chunks

---

## Retrieval

- POST /retrieval/context
- POST /retrieval/query-embedding

---

## Chats

- POST /chats
- GET /chats
- GET /chats/{id}
- PATCH /chats/{id}
- DELETE /chats/{id}

---

## Messages

- POST /chats/{id}/messages
- GET /chats/{id}/messages
- DELETE /messages/{id}
- POST /messages/{id}/regenerate

---

## Streaming

- POST /chats/{id}/stream

---

## Settings

- GET /settings
- PUT /settings
- POST /settings/reset

---

## Health

- GET /health
- GET /health/live
- GET /health/ready

---

## Admin (Future)

- GET /admin/statistics
- GET /admin/jobs
- POST /admin/jobs/{job_id}/retry

---

# 35. Conclusion

This API specification defines the complete REST interface for Atlas. It establishes consistent endpoint design, authentication, request and response formats, error handling, versioning, and security practices. Together with the `PROJECT.md`, `SRS.md`, `DFD.md`, and `Development-Roadmap.md`, it provides a complete contract for frontend, backend, and AI service implementation.
