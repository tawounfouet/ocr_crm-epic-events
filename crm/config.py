import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./epic_events.db")

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440")
    )

    # Sentry
    SENTRY_DSN: str = os.getenv("SENTRY_DSN", "")
    SENTRY_ENVIRONMENT: str = os.getenv("SENTRY_ENVIRONMENT", "development")

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    class Config:
        case_sensitive = True


settings = Settings()
