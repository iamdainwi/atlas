"""
Chat repository.
"""

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.chat import Chat


def create_chat(db: Session, chat: Chat) -> Chat:
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat


def get_chat_by_id(db: Session, chat_id: str | UUID) -> Chat | None:
    return db.query(Chat).filter(Chat.id == str(chat_id)).first()


def get_chats_by_owner(
    db: Session, owner_id: str | UUID
) -> list[Chat]:
    return (
        db.query(Chat)
        .filter(Chat.owner_id == str(owner_id))
        .order_by(Chat.updated_at.desc())
        .all()
    )


def update_chat(db: Session, chat: Chat, **kwargs) -> Chat:
    for key, value in kwargs.items():
        setattr(chat, key, value)
    db.commit()
    db.refresh(chat)
    return chat


def delete_chat(db: Session, chat: Chat) -> None:
    db.delete(chat)
    db.commit()


__all__ = [
    "create_chat",
    "get_chat_by_id",
    "get_chats_by_owner",
    "update_chat",
    "delete_chat",
]
