from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config.settings import settings

DATABASE_URL: str = settings.DATABASE_URL

# SQLite: check_same_thread=False needed for multi-threaded FastAPI
_connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=_connect_args)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

__all__ = ["engine", "SessionLocal"]