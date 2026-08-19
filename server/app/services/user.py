"""
User service — profile management and account deletion.
"""

from sqlalchemy.orm import Session

from app.core.exceptions import UnauthorizedError
from app.core.security import hash_password, verify_password
from app.models.user import User
from app.repositories.user import delete_user, update_user
from app.schemas.user import PasswordChange, UserUpdate


def update_profile(db: Session, user: User, data: UserUpdate) -> User:
    """Update mutable profile fields (name, avatar_url)."""
    return update_user(
        db,
        user,
        name=data.name,
        avatar_url=data.avatar_url,
    )


def change_password(db: Session, user: User, data: PasswordChange) -> None:
    """Verify current password then update to new hash."""
    if not verify_password(data.current_password, user.password_hash):
        raise UnauthorizedError("Current password is incorrect.")
    update_user(db, user, password_hash=hash_password(data.new_password))


def delete_account(db: Session, user: User) -> None:
    """Permanently delete a user and all associated data (cascade)."""
    delete_user(db, user)


__all__ = ["update_profile", "change_password", "delete_account"]
