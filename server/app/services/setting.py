"""
Settings service — get or create user preferences, update them.
"""

from sqlalchemy.orm import Session

from app.models.setting import Setting
from app.models.user import User
from app.repositories.setting import create_setting, get_setting_by_owner, update_setting
from app.schemas.setting import SettingUpdate


def get_or_create_settings(db: Session, user: User) -> Setting:
    """Return user settings, creating defaults if none exist yet."""
    setting = get_setting_by_owner(db, user.id)
    if not setting:
        setting = Setting(owner_id=user.id)
        setting = create_setting(db, setting)
    return setting


def update_settings(db: Session, user: User, data: SettingUpdate) -> Setting:
    setting = get_or_create_settings(db, user)
    update_kwargs = data.model_dump(exclude_none=True)
    return update_setting(db, setting, **update_kwargs)


__all__ = ["get_or_create_settings", "update_settings"]
