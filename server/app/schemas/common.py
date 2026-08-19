"""
Standard API response envelope used across all Atlas endpoints.
"""

from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Any | None = None


class ApiResponse(BaseModel, Generic[T]):
    success: bool
    data: T | None = None
    error: ErrorDetail | None = None


def success_response(data: T, message: str | None = None) -> ApiResponse[T]:
    return ApiResponse(success=True, data=data, error=None)


def error_response(
    code: str, message: str, details: Any = None
) -> ApiResponse[None]:
    return ApiResponse(
        success=False,
        data=None,
        error=ErrorDetail(code=code, message=message, details=details),
    )


__all__ = [
    "ApiResponse",
    "ErrorDetail",
    "success_response",
    "error_response",
]
