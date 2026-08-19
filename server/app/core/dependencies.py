"""
FastAPI dependency functions shared across all routers.
"""

from typing import Generator

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from sqlalchemy.orm import Session

from app.core.config.database import SessionLocal
from app.core.exceptions import UnauthorizedError
from app.core.security import decode_token
from app.models.user import User
from app.repositories.user import get_user_by_id

# ---------------------------------------------------------------------------
# Database session dependency
# ---------------------------------------------------------------------------

_bearer = HTTPBearer()


def get_db() -> Generator[Session, None, None]:
    """Yield a database session and close it after the request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Authentication dependency
# ---------------------------------------------------------------------------


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(_bearer),
    db: Session = Depends(get_db),
) -> User:
    """
    Extract the JWT from the Authorization header, validate it, and return
    the corresponding User.  Raises 401 on any failure.
    """
    token = credentials.credentials
    try:
        payload = decode_token(token)
        if payload.get("type") != "access":
            raise UnauthorizedError("Invalid token type.")
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise UnauthorizedError("Token missing subject.")
    except JWTError:
        raise UnauthorizedError("Token is invalid or expired.")

    user = get_user_by_id(db, user_id)
    if user is None:
        raise UnauthorizedError("User not found.")

    return user


__all__ = ["get_db", "get_current_user"]
