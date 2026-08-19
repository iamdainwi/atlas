"""
Message repository.
"""

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.message import Message


def create_message(db: Session, message: Message) -> Message:
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_messages_by_chat(
    db: Session, chat_id: str | UUID
) -> list[Message]:
    return (
        db.query(Message)
        .filter(Message.chat_id == str(chat_id))
        .order_by(Message.created_at.asc())
        .all()
    )


__all__ = ["create_message", "get_messages_by_chat"]
