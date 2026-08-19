"""
Document ORM model — maps to the `documents` table.
"""

from uuid import uuid4

from sqlalchemy import BigInteger, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Document(Base, TimestampMixin):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    owner_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(Text, nullable=False)
    file_type: Mapped[str] = mapped_column(String(10), nullable=False, index=True)
    size: Mapped[int] = mapped_column(BigInteger, nullable=False)
    page_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    chunk_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    # Status: uploaded | validating | extracting | cleaning | chunking
    #         | embedding | storing | processed | failed
    processing_status: Mapped[str] = mapped_column(
        String(20), default="uploaded", nullable=False, index=True
    )

    # Relationships
    owner: Mapped["User"] = relationship("User", back_populates="documents")  # type: ignore[name-defined]  # noqa: F821
    processing_jobs: Mapped[list["ProcessingJob"]] = relationship(  # type: ignore[name-defined]  # noqa: F821
        "ProcessingJob", back_populates="document", cascade="all, delete-orphan"
    )


__all__ = ["Document"]
