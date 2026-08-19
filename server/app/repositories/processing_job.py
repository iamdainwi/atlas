"""
ProcessingJob repository.
"""

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.processing_job import ProcessingJob


def create_job(db: Session, job: ProcessingJob) -> ProcessingJob:
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def get_job_by_document(db: Session, document_id: str | UUID) -> ProcessingJob | None:
    return (
        db.query(ProcessingJob)
        .filter(ProcessingJob.document_id == str(document_id))
        .order_by(ProcessingJob.started_at.desc())
        .first()
    )


def update_job(db: Session, job: ProcessingJob, **kwargs) -> ProcessingJob:
    for key, value in kwargs.items():
        setattr(job, key, value)
    db.commit()
    db.refresh(job)
    return job


__all__ = ["create_job", "get_job_by_document", "update_job"]
