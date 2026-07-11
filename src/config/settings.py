"""
Application configuration.

Loads configuration from environment variables.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Application settings."""

    postgres_user: str = os.environ["POSTGRES_USER"]
    postgres_password: str = os.environ["POSTGRES_PASSWORD"]
    postgres_db: str = os.environ["POSTGRES_DB"]
    postgres_port: int = int(os.environ["POSTGRES_PORT"])

    base_url: str = os.getenv(
        "BASE_URL",
        "https://realpython.github.io/fake-jobs/",
    )

    request_timeout: int = int(
        os.getenv("REQUEST_TIMEOUT", 30)
    )

    max_retries: int = int(
        os.getenv("MAX_RETRIES", 3)
    )


settings = Settings()