"""
Document request/response Pydantic schemas.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class DocumentRead(BaseModel):
    id: str
    title: str
    filename: str
    file_type: str
    size: int
    page_count: int
    chunk_count: int
    processing_status: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class DocumentRename(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)


class DocumentListResponse(BaseModel):
    items: list[DocumentRead]
    total: int
    page: int
    limit: int


__all__ = ["DocumentRead", "DocumentRename", "DocumentListResponse"]
