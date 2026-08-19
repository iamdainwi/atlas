"""
Document service — upload to S3, list, get, rename, delete.

Phase 4: After upload, fires a background processing pipeline
         (text extraction → chunking) via a daemon thread.
"""

import mimetypes
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from app.core.config.settings import settings
from app.core.exceptions import ForbiddenError, NotFoundError
from app.core.storage import s3_storage
from app.models.document import Document
from app.models.user import User
from app.repositories.document import (
    create_document,
    delete_document,
    get_document_by_id,
    get_documents_by_owner,
    update_document,
)
from app.schemas.document import DocumentListResponse, DocumentRead


# ─── List / Get ──────────────────────────────────────────────────────────────

def list_documents(
    db: Session,
    user: User,
    page: int = 1,
    limit: int = 20,
    file_type: str | None = None,
    status: str | None = None,
    q: str | None = None,
) -> DocumentListResponse:
    items, total = get_documents_by_owner(
        db, user.id, page=page, limit=limit, file_type=file_type, status=status, q=q
    )
    return DocumentListResponse(
        items=[DocumentRead.model_validate(d) for d in items],
        total=total,
        page=page,
        limit=limit,
    )


def get_document(db: Session, user: User, document_id: str) -> Document:
    doc = get_document_by_id(db, document_id)
    if not doc:
        raise NotFoundError("Document")
    if str(doc.owner_id) != str(user.id):
        raise ForbiddenError()
    return doc


# ─── Upload ───────────────────────────────────────────────────────────────────

def upload_document(db: Session, user: User, file: UploadFile) -> Document:
    # 1. Validate extension
    filename = file.filename or "untitled"
    ext = Path(filename).suffix.lower()
    if ext not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type '{ext}' not allowed. Allowed: {sorted(settings.ALLOWED_EXTENSIONS)}",
        )

    # 2. Check file size
    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)
    if size > settings.MAX_UPLOAD_SIZE_BYTES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File too large. Max size is {settings.MAX_UPLOAD_SIZE_BYTES // (1024 * 1024)} MB.",
        )

    # 3. Build S3 key: users/{user_id}/documents/{uuid}.ext
    doc_id = str(uuid4())
    safe_name = f"{doc_id}{ext}"
    s3_key = f"users/{user.id}/documents/{safe_name}"
    content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"

    # 4. Upload to S3
    s3_storage.upload_fileobj(file.file, s3_key, content_type=content_type)

    # 5. Create DB record
    new_doc = Document(
        id=doc_id,
        owner_id=str(user.id),
        title=filename,
        filename=safe_name,
        s3_key=s3_key,
        file_type=ext.lstrip("."),
        size=size,
        processing_status="uploaded",
    )
    doc = create_document(db, new_doc)

    # 6. Fire background processing pipeline
    from app.workers.document_pipeline import launch_pipeline
    launch_pipeline(doc_id)

    return doc


# ─── Rename / Delete ─────────────────────────────────────────────────────────

def rename_document(db: Session, user: User, document_id: str, title: str) -> Document:
    doc = get_document(db, user, document_id)
    return update_document(db, doc, title=title)


def remove_document(db: Session, user: User, document_id: str) -> None:
    doc = get_document(db, user, document_id)
    # Delete from S3
    if doc.s3_key:
        s3_storage.delete_file(doc.s3_key)
    # Delete all chunks from Chroma Cloud
    from app.core.chroma import delete_document_from_chroma
    delete_document_from_chroma(user_id=str(user.id), document_id=document_id)
    delete_document(db, doc)


# ─── Download ────────────────────────────────────────────────────────────────

def get_document_presigned_url(db: Session, user: User, document_id: str) -> str:
    """Generate a short-lived S3 presigned URL for direct browser download."""
    doc = get_document(db, user, document_id)
    return s3_storage.generate_presigned_url(doc.s3_key, expires_in=300)  # 5 min


__all__ = [
    "list_documents",
    "get_document",
    "upload_document",
    "rename_document",
    "remove_document",
    "get_document_presigned_url",
]
