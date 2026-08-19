**What**: Based on the docs and the current server state, here's exactly what remains to build.

**Why**: We've completed **Phase 1 (Foundation)** and **Phase 2 (Authentication)** from the roadmap. The server has a clean architecture, all 6 DB tables, JWT auth, and user/settings APIs. Everything from Phase 3 onwards still needs to be built.

**How**: Here's the full remaining roadmap mapped to your docs:

---

## ✅ Done
| Phase | What |
|---|---|
| Phase 1 | Project structure, FastAPI setup, Clean architecture, SQLite |
| Phase 2 | Register, Login, JWT (access + refresh), `/me`, password change, account delete, settings |

---

## 🔲 Remaining (in order — don't skip phases)

### Phase 3 — File Storage
| Task | Details |
|---|---|
| `POST /api/v1/documents` | Accept `multipart/form-data`, validate file type (pdf/docx/txt/md), save to `storage/users/{user_id}/documents/` |
| File type validation | Reject anything not in `[pdf, docx, txt, md]`, enforce size limit |
| Document metadata | Save to `documents` table with `processing_status = "uploaded"` |
| `GET /api/v1/documents/{id}/download` | Stream the original file back |

---

### Phase 4 — Document Processing Pipeline
| Task | Details |
|---|---|
| Text extraction | PDF → `PyMuPDF (fitz)`, DOCX → `python-docx`, TXT/MD → plain read |
| Text cleaning | Strip noise, extra whitespace, formatting artifacts |
| Chunking | Fixed-size overlapping chunks (500 tokens / 100 overlap) |
| `ProcessingJob` tracking | Update `progress` 0→100, `current_step`, `status` |
| `GET /api/v1/documents/{id}/status` | Return live processing status |
| Background processing | Run pipeline in a background thread/worker after upload |

---

### Phase 5 — Embeddings
| Task | Details |
|---|---|
| Embedding service | Load `BAAI/bge-small-en-v1.5` via `sentence-transformers` |
| Batch embed chunks | Generate 768-dim vectors for every chunk |
| Install ChromaDB | `uv add chromadb sentence-transformers` |
| Store in ChromaDB | Collection: `atlas_documents`, metadata per chunk: `user_id`, `document_id`, `filename`, `page`, `chunk_index` |

---

### Phase 6 — Semantic Retrieval
| Task | Details |
|---|---|
| Query embedding | Embed user's question with same model |
| Similarity search | ChromaDB `collection.query()` → Top-K chunks |
| `POST /api/v1/search` | Public search endpoint (debug retrieval quality) |
| Retrieval service | `app/services/retrieval.py` |

---

### Phase 7 — Prompt Construction + LLM
| Task | Details |
|---|---|
| Prompt service | System prompt + retrieved context + chat history + user question |
| Token budgeting | Count tokens, truncate context if needed |
| LLM service | Connect to Ollama (`langchain-ollama` already installed) |
| Chat APIs | `POST /api/v1/chats`, `GET /api/v1/chats`, `POST /api/v1/chats/{id}/messages` |
| Streaming | Stream LLM tokens back to client via SSE |

---

### Phase 8 — Chat History
| Task | Details |
|---|---|
| Persist messages | Save user + assistant messages to `messages` table |
| Load conversation | Send last N messages as history in prompt |
| Chat management | Rename chat, delete chat, list chats |

---

### Phase 9 — Frontend (Next.js)
| Pages | Login, Register, Document Library, Upload, Chat, Settings |

---

### Phase 10 — Polish & Deployment
| Task | Details |
|---|---|
| Docker Compose | FastAPI + ChromaDB containers |
| Alembic migrations | Replace `create_all()` with proper migrations |
| Error handling | Edge cases, retry logic for LLM/embeddings |

---

> [!TIP]
> **Start with Phase 3** — `POST /api/v1/documents` file upload. Everything after (processing, embedding, retrieval, chat) depends on documents being stored. Just say "build Phase 3" and I'll implement it.

Viewed AGENTS.md:1-10