"""
User request/response Pydantic schemas.
"""

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserRead(BaseModel):
    id: str
    name: str
    email: EmailStr
    avatar_url: str | None
    provider: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=120)
    avatar_url: str | None = None


class PasswordChange(BaseModel):
    current_password: str
    new_password: str = Field(..., min_length=8, max_length=128)


__all__ = ["UserRead", "UserUpdate", "PasswordChange"]
