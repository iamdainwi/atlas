"""
Settings routes — /api/v1/settings
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.common import ApiResponse, success_response
from app.schemas.setting import SettingRead, SettingUpdate
from app.services.setting import get_or_create_settings, update_settings

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.get("", response_model=ApiResponse[SettingRead])
def get_settings(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    setting = get_or_create_settings(db, current_user)
    return success_response(SettingRead.model_validate(setting))


@router.put("", response_model=ApiResponse[SettingRead])
def update_my_settings(
    data: SettingUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    setting = update_settings(db, current_user, data)
    return success_response(SettingRead.model_validate(setting))
