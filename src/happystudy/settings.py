"""Settings."""

# pylint: disable=too-few-public-methods

import pathlib
from typing import Optional

import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    """Application settings class."""

    debug: bool = False
    log_dir: Optional[pathlib.Path] = None

    model_config = {
        "case_sensitive": False,
        "env_prefix": "HS_",
    }


settings = Settings()
