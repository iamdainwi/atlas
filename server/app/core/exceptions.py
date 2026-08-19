"""
Custom exception classes for Atlas.
All domain errors should extend AtlasException so that the global
exception handler can produce consistent JSON responses.
"""


class AtlasException(Exception):
    """Base exception for all Atlas domain errors."""

    def __init__(self, code: str, message: str, status_code: int = 400):
        self.code = code
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class NotFoundError(AtlasException):
    def __init__(self, resource: str = "Resource"):
        super().__init__(
            code=f"{resource.upper()}_NOT_FOUND",
            message=f"{resource} not found.",
            status_code=404,
        )


class ConflictError(AtlasException):
    def __init__(self, code: str, message: str):
        super().__init__(code=code, message=message, status_code=409)


class UnauthorizedError(AtlasException):
    def __init__(self, message: str = "Unauthorized."):
        super().__init__(code="UNAUTHORIZED", message=message, status_code=401)


class ForbiddenError(AtlasException):
    def __init__(self, message: str = "Forbidden."):
        super().__init__(code="FORBIDDEN", message=message, status_code=403)


class ValidationError(AtlasException):
    def __init__(self, message: str):
        super().__init__(code="VALIDATION_ERROR", message=message, status_code=422)


__all__ = [
    "AtlasException",
    "NotFoundError",
    "ConflictError",
    "UnauthorizedError",
    "ForbiddenError",
    "ValidationError",
]
