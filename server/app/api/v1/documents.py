"""
Document routes — /api/v1/documents/*

Upload (POST /documents) will be fully implemented in Phase 4/5.
"""

from fastapi import APIRouter, Depends, Query, status, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.common import ApiResponse, success_response
from app.schemas.document import DocumentListResponse, DocumentRead, DocumentRename
from app.services.document import (
    get_document, 
    list_documents, 
    remove_document, 
    rename_document,
    upload_document,
    get_document_file_path
)

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("", response_model=ApiResponse[DocumentRead], status_code=status.HTTP_201_CREATED)
def upload(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    doc = upload_document(db, current_user, file)
    return success_response(DocumentRead.model_validate(doc))


@router.get("", response_model=ApiResponse[DocumentListResponse])
def get_documents(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    type: str | None = Query(None),
    status: str | None = Query(None),
    q: str | None = Query(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    result = list_documents(
        db, current_user, page=page, limit=limit, file_type=type, status=status, q=q
    )
    return success_response(result)


@router.get("/{document_id}", response_model=ApiResponse[DocumentRead])
def get_document_detail(
    document_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    doc = get_document(db, current_user, document_id)
    return success_response(DocumentRead.model_validate(doc))


@router.get("/{document_id}/download")
def download(
    document_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    file_path = get_document_file_path(db, current_user, document_id)
    doc = get_document(db, current_user, document_id)
    return FileResponse(
        path=file_path, 
        filename=doc.filename,
        media_type="application/octet-stream"
    )


@router.patch("/{document_id}", response_model=ApiResponse[DocumentRead])
def rename(
    document_id: str,
    data: DocumentRename,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    doc = rename_document(db, current_user, document_id, data.title)
    return success_response(DocumentRead.model_validate(doc))


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    document_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    remove_document(db, current_user, document_id)
    return None
