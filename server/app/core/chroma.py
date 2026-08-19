"""
Chroma Cloud service.

Provides a per-user collection with:
  - Dense embeddings via Chroma Cloud Qwen (semantic search)
  - Sparse embeddings via Chroma Cloud Splade (keyword search)
  - Hybrid search using Reciprocal Rank Fusion (RRF)
  - GroupBy deduplication to return one best chunk per document

Collection naming strategy:
  Each user has their own collection sharded by user_id:
    atlas_user_{user_id}

This ensures strict data isolation — users never see each other's data.
"""

import os
import logging

import chromadb
from chromadb import Schema, SparseVectorIndexConfig, K
from chromadb.execution.expression import GroupBy, MinK, Search, Knn, Rrf
from chromadb.utils.embedding_functions import (
    ChromaCloudQwenEmbeddingFunction,
    ChromaCloudSpladeEmbeddingFunction,
)

from app.core.config.settings import settings

logger = logging.getLogger(__name__)

# Set the API key env var so the EF wrappers can pick it up
os.environ.setdefault("CHROMA_API_KEY", settings.CHROMA_API_KEY)


def _build_schema() -> Schema:
    """Build a Chroma Cloud Schema with dense (Qwen) + sparse (Splade) indexes."""
    schema = Schema()

    # Sparse index — Splade for keyword-based retrieval
    sparse_ef = ChromaCloudSpladeEmbeddingFunction()
    schema.create_index(
        config=SparseVectorIndexConfig(
            source_key=K.DOCUMENT,
            embedding_function=sparse_ef,
        ),
        key="sparse_embedding",
    )
    return schema


def _get_client() -> chromadb.CloudClient:
    return chromadb.CloudClient(
        tenant=settings.CHROMA_TENANT,
        database=settings.CHROMA_DATABASE,
        api_key=settings.CHROMA_API_KEY,
    )


def _dense_ef() -> ChromaCloudQwenEmbeddingFunction:
    """Qwen dense embedding function — used when creating/querying the collection."""
    from chromadb.utils.embedding_functions import ChromaCloudQwenEmbeddingModel
    return ChromaCloudQwenEmbeddingFunction(
        model=ChromaCloudQwenEmbeddingModel.QWEN3_EMBEDDING_0p6B,
        task="text_matching",
    )


def get_or_create_user_collection(user_id: str):
    """
    Get or create a Chroma Cloud collection for a specific user.

    Naming: atlas_user_{user_id}
    Schema: dense (Qwen) + sparse (Splade) for hybrid search.
    """
    client = _get_client()
    collection_name = f"atlas_user_{user_id.replace('-', '_')}"

    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=_dense_ef(),
        schema=_build_schema(),
    )
    logger.info("[Chroma] Collection: %s", collection_name)
    return collection


def add_chunks_to_chroma(
    user_id: str,
    document_id: str,
    document_title: str,
    chunks: list[str],
) -> None:
    """
    Upsert document chunks into the user's Chroma collection.

    Metadata per chunk:
      - document_id: for GroupBy deduplication
      - chunk_index: ordering within the document
      - title: document title for display in search results
      - user_id: extra safety guard

    Chroma has a 16 KiB per document limit, so chunks must be pre-split.
    """
    if not chunks:
        logger.warning("[Chroma] No chunks to add for document %s", document_id)
        return

    collection = get_or_create_user_collection(user_id)

    ids = [f"{document_id}_chunk_{i}" for i in range(len(chunks))]
    metadatas = [
        {
            "document_id": document_id,
            "chunk_index": i,
            "title": document_title,
            "user_id": user_id,
        }
        for i in range(len(chunks))
    ]

    # Upsert in batches of 100 to avoid hitting request size limits
    batch_size = 100
    for start in range(0, len(chunks), batch_size):
        end = start + batch_size
        collection.upsert(
            ids=ids[start:end],
            documents=chunks[start:end],
            metadatas=metadatas[start:end],
        )
        logger.info(
            "[Chroma] Upserted chunks %d–%d for document %s",
            start, min(end, len(chunks)) - 1, document_id,
        )


def delete_document_from_chroma(user_id: str, document_id: str) -> None:
    """Remove all chunks for a document from the user's collection."""
    try:
        client = _get_client()
        collection_name = f"atlas_user_{user_id.replace('-', '_')}"
        collection = client.get_collection(
            name=collection_name,
            embedding_function=_dense_ef(),
        )
        collection.delete(where={"document_id": document_id})
        logger.info("[Chroma] Deleted all chunks for document %s", document_id)
    except Exception as e:
        logger.warning("[Chroma] Could not delete document %s: %s", document_id, e)


def hybrid_search(
    user_id: str,
    query: str,
    n_results: int = 10,
    document_id: str | None = None,
) -> list[dict]:
    """
    Hybrid search using dense (Qwen) + sparse (Splade) RRF with GroupBy deduplication.

    Returns one best chunk per unique document_id, so we don't flood the
    results with many chunks from the same large document.

    Args:
        user_id:     The user performing the search (restricts to their collection).
        query:       The user's natural-language query.
        n_results:   Maximum number of documents to return (after dedup).
        document_id: Optional — restrict search to a single document's chunks.

    Returns:
        List of dicts with keys: document_id, title, chunk, score, chunk_index
    """
    client = _get_client()
    collection_name = f"atlas_user_{user_id.replace('-', '_')}"

    try:
        collection = client.get_collection(
            name=collection_name,
            embedding_function=_dense_ef(),
        )
    except Exception:
        logger.warning("[Chroma] Collection not found for user %s", user_id)
        return []

    # Build hybrid RRF ranking: 70% dense (semantic) + 30% sparse (keyword)
    hybrid_rank = Rrf(
        ranks=[
            Knn(query=query, key="#embedding", return_rank=True, limit=200, default=1000),
            Knn(query=query, key="sparse_embedding", return_rank=True, limit=200, default=1000),
        ],
        weights=[0.7, 0.3],
        k=60,
    )

    # Build search — optionally filter by document_id
    search = Search().rank(hybrid_rank)

    if document_id:
        search = search.where(K("document_id") == document_id)

    # GroupBy document_id → deduplicate, keep 1 best chunk per document
    search = (
        search
        .group_by(GroupBy(
            keys=K("document_id"),
            aggregate=MinK(keys=K.SCORE, k=1),
        ))
        .limit(n_results)
        .select(K.DOCUMENT, K.SCORE, "document_id", "title", "chunk_index")
    )

    try:
        results = collection.search(search)
        rows = results.rows()[0] if results.rows() else []
    except Exception as e:
        logger.error("[Chroma] Search failed: %s", e)
        return []

    output = []
    for row in rows:
        meta = row.get("metadata", {})
        output.append({
            "document_id": meta.get("document_id", ""),
            "title": meta.get("title", ""),
            "chunk": row.get("document", ""),
            "score": row.get("score", 0.0),
            "chunk_index": meta.get("chunk_index", 0),
        })

    return output


__all__ = [
    "get_or_create_user_collection",
    "add_chunks_to_chroma",
    "delete_document_from_chroma",
    "hybrid_search",
]
