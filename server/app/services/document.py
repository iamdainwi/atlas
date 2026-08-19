"""
Document service — upload, rename, delete (Phase 4 stub).

Full implementation (text extraction, chunking, embedding)
will be built in Phases 5–6.
"""

import os
import shutil
from pathlib import Path
from uuid import UUID, uuid4

from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from app.core.config.settings import settings

from app.core.exceptions import ForbiddenError, NotFoundError
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


def get_document(db: Session, user: User, document_id: str | UUID) -> Document:
    doc = get_document_by_id(db, document_id)
    if not doc:
        raise NotFoundError("Document")
    if str(doc.owner_id) != str(user.id):
        raise ForbiddenError()
    return doc


def rename_document(
    db: Session, user: User, document_id: str | UUID, title: str
) -> Document:
    doc = get_document(db, user, document_id)
    return update_document(db, doc, title=title)


def remove_document(db: Session, user: User, document_id: str | UUID) -> None:
    doc = get_document(db, user, document_id)
    # Also delete the physical file
    if doc.file_path and os.path.exists(doc.file_path):
        try:
            os.remove(doc.file_path)
        except OSError:
            pass
    delete_document(db, doc)


def upload_document(db: Session, user: User, file: UploadFile) -> Document:
    # 1. Validate extension
    filename = file.filename or "untitled"
    ext = Path(filename).suffix.lower()
    if ext not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File type {ext} not allowed. Allowed types: {settings.ALLOWED_EXTENSIONS}",
        )
    
    # 2. Setup storage directory
    user_dir = Path(settings.STORAGE_DIR) / "users" / str(user.id) / "documents"
    user_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. Create unique filename on disk
    doc_id = str(uuid4())
    safe_filename = f"{doc_id}{ext}"
    file_path = user_dir / safe_filename
    
    # 4. Save file
    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)
    
    if size > settings.MAX_UPLOAD_SIZE_BYTES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File too large. Max size is {settings.MAX_UPLOAD_SIZE_BYTES / (1024 * 1024)}MB",
        )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # 5. Create database record
    new_doc = Document(
        id=doc_id,
        owner_id=str(user.id),
        title=filename,
        filename=safe_filename,
        file_path=str(file_path),
        file_type=ext.lstrip("."),
        size=size,
        processing_status="uploaded"
    )
    return create_document(db, new_doc)


def get_document_file_path(db: Session, user: User, document_id: str | UUID) -> str:
    doc = get_document(db, user, document_id)
    if not doc.file_path or not os.path.exists(doc.file_path):
        raise NotFoundError("Document file on disk")
    return doc.file_path


__all__ = ["list_documents", "get_document", "rename_document", "remove_document", "upload_document", "get_document_file_path"]
