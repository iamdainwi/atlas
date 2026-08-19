"""
Setting repository.
"""

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.setting import Setting


def get_setting_by_owner(db: Session, owner_id: str | UUID) -> Setting | None:
    return db.query(Setting).filter(Setting.owner_id == str(owner_id)).first()


def create_setting(db: Session, setting: Setting) -> Setting:
    db.add(setting)
    db.commit()
    db.refresh(setting)
    return setting


def update_setting(db: Session, setting: Setting, **kwargs) -> Setting:
    for key, value in kwargs.items():
        if value is not None:
            setattr(setting, key, value)
    db.commit()
    db.refresh(setting)
    return setting


__all__ = ["get_setting_by_owner", "create_setting", "update_setting"]
