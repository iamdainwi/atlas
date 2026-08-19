"""
User routes — /api/v1/users/*
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.common import ApiResponse, success_response
from app.schemas.user import PasswordChange, UserRead, UserUpdate
from app.services.user import change_password, delete_account, update_profile

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=ApiResponse[UserRead])
def get_me(current_user: User = Depends(get_current_user)):
    return success_response(UserRead.model_validate(current_user))


@router.put("/me", response_model=ApiResponse[UserRead])
def update_me(
    data: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    updated = update_profile(db, current_user, data)
    return success_response(UserRead.model_validate(updated))


@router.patch("/me/password", status_code=status.HTTP_204_NO_CONTENT)
def change_my_password(
    data: PasswordChange,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    change_password(db, current_user, data)
    return None


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_me(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    delete_account(db, current_user)
    return None
