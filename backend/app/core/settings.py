"""
Application configuration.
Handles environment variables and global settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Project
    PROJECT_NAME: str = "Adaptive AI Workbench"
    VERSION: str = "0.1.0"
    API_V1_PREFIX: str = "/api/v1"

    # Application
    DEBUG: bool = False

    # Database
    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    OPENAI_API_KEY: str = ""


    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()