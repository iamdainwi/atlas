"""
Setting ORM model — maps to the `settings` table.
One-to-one relationship with User.
"""

from uuid import uuid4

from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Setting(Base):
    __tablename__ = "settings"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    owner_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True,
    )
    theme: Mapped[str] = mapped_column(String(20), default="dark", nullable=False)
    llm_provider: Mapped[str] = mapped_column(String(30), default="ollama", nullable=False)
    embedding_model: Mapped[str] = mapped_column(
        String(100), default="BAAI/bge-small-en-v1.5", nullable=False
    )
    temperature: Mapped[float] = mapped_column(Float, default=0.7, nullable=False)
    top_k: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    chunk_size: Mapped[int] = mapped_column(Integer, default=500, nullable=False)
    overlap: Mapped[int] = mapped_column(Integer, default=100, nullable=False)

    owner: Mapped["User"] = relationship("User", back_populates="setting")  # type: ignore[name-defined]  # noqa: F821


__all__ = ["Setting"]
