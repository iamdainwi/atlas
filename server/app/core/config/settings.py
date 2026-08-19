from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Database
    DATABASE_URL: str = "sqlite:///./atlas.db"

    # JWT
    SECRET_KEY: str = "change-me-in-production-use-a-long-random-string"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Ollama (AI)
    OLLAMA_API_KEY: str = ""
    OLLAMA_BASE_URL: str = "http://localhost:11434"

    # App
    APP_NAME: str = "Atlas"
    DEBUG: bool = True

    # File validation
    ALLOWED_EXTENSIONS: set[str] = {".pdf", ".docx", ".txt", ".md"}
    MAX_UPLOAD_SIZE_BYTES: int = 10 * 1024 * 1024  # 10 MB

    # AWS S3 Storage
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_REGION: str = "us-east-1"
    AWS_S3_BUCKET_NAME: str = "atlas-document-bucket"

    # Chroma Cloud
    CHROMA_HOST: str = "api.trychroma.com"
    CHROMA_API_KEY: str = ""
    CHROMA_TENANT: str = ""
    CHROMA_DATABASE: str = "atlas"


settings = Settings()

__all__ = ["settings", "Settings"]
