"""
AWS S3 storage service.
Handles all file operations (upload, download, delete, presigned URLs) via boto3.
"""

import boto3
from botocore.exceptions import ClientError
from fastapi import HTTPException, status

from app.core.config.settings import settings


class S3StorageService:
    """Thin wrapper around boto3 S3 client."""

    def __init__(self) -> None:
        self._client = boto3.client(
            "s3",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        self._bucket = settings.AWS_S3_BUCKET_NAME

    def upload_fileobj(self, file_obj, s3_key: str, content_type: str = "application/octet-stream") -> str:
        """Upload a file-like object and return the S3 key."""
        try:
            self._client.upload_fileobj(
                file_obj,
                self._bucket,
                s3_key,
                ExtraArgs={"ContentType": content_type},
            )
            return s3_key
        except ClientError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"S3 upload failed: {e.response['Error']['Message']}",
            )

    def download_bytes(self, s3_key: str) -> bytes:
        """Download an S3 object and return its raw bytes."""
        try:
            response = self._client.get_object(Bucket=self._bucket, Key=s3_key)
            return response["Body"].read()
        except ClientError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"S3 object not found: {e.response['Error']['Message']}",
            )

    def delete_file(self, s3_key: str) -> None:
        """Delete an S3 object. Silently ignores missing keys."""
        try:
            self._client.delete_object(Bucket=self._bucket, Key=s3_key)
        except ClientError:
            pass  # Best-effort delete

    def generate_presigned_url(self, s3_key: str, expires_in: int = 3600) -> str:
        """Generate a presigned URL for temporary direct browser download."""
        try:
            return self._client.generate_presigned_url(
                "get_object",
                Params={"Bucket": self._bucket, "Key": s3_key},
                ExpiresIn=expires_in,
            )
        except ClientError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Could not generate download URL: {e.response['Error']['Message']}",
            )


# Singleton instance used across the app
s3_storage = S3StorageService()

__all__ = ["S3StorageService", "s3_storage"]
