"""
Chat & Message request/response Pydantic schemas.
"""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


# ── Chat ──────────────────────────────────────────────────────────────────

class ChatRead(BaseModel):
    id: UUID
    title: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ChatCreate(BaseModel):
    title: str = Field(default="New Chat", max_length=255)


class ChatRename(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)


# ── Message ───────────────────────────────────────────────────────────────

class MessageRead(BaseModel):
    id: UUID
    role: str
    content: str
    token_count: int | None
    created_at: datetime

    model_config = {"from_attributes": True}


class MessageCreate(BaseModel):
    content: str = Field(..., min_length=1)


__all__ = [
    "ChatRead",
    "ChatCreate",
    "ChatRename",
    "MessageRead",
    "MessageCreate",
]
