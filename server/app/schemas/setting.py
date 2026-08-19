"""
Setting request/response Pydantic schemas.
"""

from pydantic import BaseModel, Field


class SettingRead(BaseModel):
    id: str
    theme: str
    llm_provider: str
    embedding_model: str
    temperature: float
    top_k: int
    chunk_size: int
    overlap: int

    model_config = {"from_attributes": True}


class SettingUpdate(BaseModel):
    theme: str | None = None
    llm_provider: str | None = None
    embedding_model: str | None = None
    temperature: float | None = Field(None, ge=0.0, le=2.0)
    top_k: int | None = Field(None, ge=1, le=20)
    chunk_size: int | None = Field(None, ge=100, le=2000)
    overlap: int | None = Field(None, ge=0, le=500)


__all__ = ["SettingRead", "SettingUpdate"]
