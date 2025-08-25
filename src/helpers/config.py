from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Json

class Settings(BaseSettings):
    APP_NAME: str = "mini-RAG"
    APP_VERSION: str = "1.0.0"
    OPENAI_API_KEY: str | None = None

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    model_config = SettingsConfigDict(env_file=".env",env_file_encoding="utf-8",)

def get_settings() -> "Settings":
    return Settings()
