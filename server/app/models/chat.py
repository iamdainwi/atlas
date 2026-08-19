"""
Chat ORM model — maps to the `chats` table.
"""

from uuid import uuid4

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Chat(Base, TimestampMixin):
    __tablename__ = "chats"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    owner_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(255), default="New Chat", nullable=False)

    owner: Mapped["User"] = relationship("User", back_populates="chats")  # type: ignore[name-defined]  # noqa: F821
    messages: Mapped[list["Message"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        "Message", back_populates="chat", cascade="all, delete-orphan"
    )


__all__ = ["Chat"]
