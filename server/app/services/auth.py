"""
Authentication service — register, login, refresh, logout.
"""

from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, UnauthorizedError
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.core.config.settings import settings
from app.models.setting import Setting
from app.models.user import User
from app.repositories.setting import create_setting
from app.repositories.user import create_user, get_user_by_email
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from jose import JWTError


def register_user(db: Session, data: RegisterRequest) -> User:
    """Create a new user account. Raises ConflictError if email is taken."""
    if get_user_by_email(db, data.email):
        raise ConflictError(
            code="EMAIL_ALREADY_EXISTS",
            message="An account with this email already exists.",
        )

    user = User(
        name=data.name,
        email=str(data.email),
        password_hash=hash_password(data.password),
    )
    created = create_user(db, user)

    # Auto-create default settings for new user
    default_setting = Setting(owner_id=created.id)
    create_setting(db, default_setting)

    return created


def login_user(db: Session, data: LoginRequest) -> TokenResponse:
    """Authenticate a user and return JWT tokens. Raises UnauthorizedError on failure."""
    user = get_user_by_email(db, str(data.email))
    if not user or not verify_password(data.password, user.password_hash):
        raise UnauthorizedError("Invalid email or password.")

    access_token = create_access_token(str(user.id))
    refresh_token = create_refresh_token(str(user.id))

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )


def refresh_access_token(refresh_token: str) -> dict:
    """Validate a refresh token and issue a new access token."""
    try:
        payload = decode_token(refresh_token)
        if payload.get("type") != "refresh":
            raise UnauthorizedError("Invalid token type.")
        user_id: str = payload["sub"]
    except (JWTError, KeyError):
        raise UnauthorizedError("Refresh token is invalid or expired.")

    new_access = create_access_token(user_id)
    return {
        "access_token": new_access,
        "token_type": "bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    }


__all__ = ["register_user", "login_user", "refresh_access_token"]
