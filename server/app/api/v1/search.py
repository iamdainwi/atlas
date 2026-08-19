"""
Search routes — /api/v1/search
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.common import ApiResponse, success_response
from app.services.retrieval import search_documents

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("", response_model=ApiResponse[list[dict]])
def search(
    q: str = Query(..., min_length=1, description="Natural language search query"),
    n: int = Query(10, ge=1, le=50, description="Number of results"),
    document_id: str | None = Query(None, description="Restrict search to a single document"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Hybrid semantic + keyword search over the user's processed documents.

    Uses Chroma Cloud with:
      - Dense embeddings (Qwen) for semantic understanding
      - Sparse embeddings (Splade) for keyword matching
      - RRF to combine both rankings
      - GroupBy to deduplicate chunks from the same document
    """
    results = search_documents(
        user=current_user,
        query=q,
        n_results=n,
        document_id=document_id,
    )
    return success_response(results)
