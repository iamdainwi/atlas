"""
Document routes — /api/v1/documents/*
"""

from fastapi import APIRouter, Depends, Query, status, UploadFile, File
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.common import ApiResponse, success_response
from app.schemas.document import DocumentListResponse, DocumentRead, DocumentRename, ProcessingJobRead
from app.services.document import (
    get_document,
    list_documents,
    remove_document,
    rename_document,
    upload_document,
    get_document_presigned_url,
)

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("", response_model=ApiResponse[DocumentRead], status_code=status.HTTP_201_CREATED)
def upload(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Upload a document to S3 and kick off the processing pipeline."""
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
    """Redirect the browser to a short-lived S3 presigned URL."""
    presigned_url = get_document_presigned_url(db, current_user, document_id)
    return RedirectResponse(url=presigned_url)


@router.get("/{document_id}/status", response_model=ApiResponse[ProcessingJobRead])
def get_processing_status(
    document_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return the latest processing job status for a document."""
    from app.models.processing_job import ProcessingJob
    # Ensure user owns the document
    get_document(db, current_user, document_id)
    job = (
        db.query(ProcessingJob)
        .filter(ProcessingJob.document_id == document_id)
        .order_by(ProcessingJob.started_at.desc())
        .first()
    )
    if not job:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="No processing job found for this document.")
    return success_response(ProcessingJobRead.model_validate(job))


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
    """Delete from DB and S3."""
    remove_document(db, current_user, document_id)
    return None
