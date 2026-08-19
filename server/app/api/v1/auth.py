"""
Authentication routes — /api/v1/auth/*
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.auth import (
    AccessTokenResponse,
    LoginRequest,
    RefreshRequest,
    RegisterRequest,
    TokenResponse,
)
from app.schemas.common import ApiResponse, success_response
from app.schemas.user import UserRead
from app.services.auth import login_user, refresh_access_token, register_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=ApiResponse[UserRead],
    status_code=status.HTTP_201_CREATED,
)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    user = register_user(db, data)
    return success_response(UserRead.model_validate(user))


@router.post("/login", response_model=ApiResponse[TokenResponse])
def login(data: LoginRequest, db: Session = Depends(get_db)):
    tokens = login_user(db, data)
    return success_response(tokens)


@router.post("/refresh", response_model=ApiResponse[AccessTokenResponse])
def refresh(data: RefreshRequest):
    result = refresh_access_token(data.refresh_token)
    return success_response(result)


@router.post(
    "/logout",
    status_code=status.HTTP_204_NO_CONTENT,
)
def logout(_current_user: User = Depends(get_current_user)):
    # Stateless JWT — client drops the token.
    # Token blocklist can be added here in a future phase.
    return None
