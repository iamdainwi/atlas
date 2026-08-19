"""
Document repository — all database operations for the Document model.
"""

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.document import Document


def create_document(db: Session, document: Document) -> Document:
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


def get_document_by_id(db: Session, document_id: str | UUID) -> Document | None:
    return db.query(Document).filter(Document.id == str(document_id)).first()


def get_documents_by_owner(
    db: Session,
    owner_id: str | UUID,
    page: int = 1,
    limit: int = 20,
    file_type: str | None = None,
    status: str | None = None,
    q: str | None = None,
) -> tuple[list[Document], int]:
    query = db.query(Document).filter(Document.owner_id == str(owner_id))
    if file_type:
        query = query.filter(Document.file_type == file_type)
    if status:
        query = query.filter(Document.processing_status == status)
    if q:
        query = query.filter(Document.title.ilike(f"%{q}%"))
    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()
    return items, total


def update_document(db: Session, document: Document, **kwargs) -> Document:
    for key, value in kwargs.items():
        if value is not None:
            setattr(document, key, value)
    db.commit()
    db.refresh(document)
    return document


def delete_document(db: Session, document: Document) -> None:
    db.delete(document)
    db.commit()


__all__ = [
    "create_document",
    "get_document_by_id",
    "get_documents_by_owner",
    "update_document",
    "delete_document",
]
