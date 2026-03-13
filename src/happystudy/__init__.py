"""Happy Study

Happy's Study Tools
"""

from importlib import metadata as meta

from .settings import settings

__version__: str = str(meta.version(__name__))

__all__ = ["__version__", "settings"]
