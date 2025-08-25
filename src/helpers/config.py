from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    APP_NAME:str ="mini-RAG"
    APP_VERSION:str  = "1.0.0"
    OPENAI_API_KEY:str | None = None
        
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
        
def get_settings():
    return Settings()
        