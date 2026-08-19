"""
User ORM model — maps to the `users` table.
"""

from uuid import uuid4

from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    avatar_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    provider: Mapped[str] = mapped_column(String(30), default="local", nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Relationships
    documents: Mapped[list["Document"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        "Document", back_populates="owner", cascade="all, delete-orphan"
    )
    chats: Mapped[list["Chat"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        "Chat", back_populates="owner", cascade="all, delete-orphan"
    )
    setting: Mapped["Setting | None"] = relationship(  # type: ignore[name-defined]  # noqa: F821
        "Setting", back_populates="owner", cascade="all, delete-orphan", uselist=False
    )


__all__ = ["User"]
