"""
Retrieval service — semantic + keyword hybrid search via Chroma Cloud.

Uses RRF (Reciprocal Rank Fusion) with:
  - Dense embeddings: Chroma Cloud Qwen (semantic understanding)
  - Sparse embeddings: Chroma Cloud Splade (keyword matching)

GroupBy document_id ensures we return one best chunk per source document,
preventing large documents from dominating results.
"""

from app.core.chroma import hybrid_search
from app.models.user import User


def search_documents(
    user: User,
    query: str,
    n_results: int = 10,
    document_id: str | None = None,
) -> list[dict]:
    """
    Perform a hybrid search over the user's documents in Chroma Cloud.

    Args:
        user:        The authenticated user — restricts search to their collection.
        query:       The natural-language search query.
        n_results:   Max results to return (default 10).
        document_id: Optional — restrict search to a single document.

    Returns:
        List of results sorted by RRF score (lower = better), each containing:
          {document_id, title, chunk, score, chunk_index}
    """
    if not query or not query.strip():
        return []

    return hybrid_search(
        user_id=str(user.id),
        query=query.strip(),
        n_results=n_results,
        document_id=document_id,
    )


__all__ = ["search_documents"]
