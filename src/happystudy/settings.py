"""Settings."""

# pylint: disable=too-few-public-methods

import pathlib
from typing import Optional

import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    """Application settings class."""

    debug: bool = False
    testing: bool = False
    log_dir: Optional[pathlib.Path] = None

    class Config:
        """Config metadata for the settings."""

        case_sensitive: bool = False
        env_prefix: str = "HS_"


settings = Settings()
