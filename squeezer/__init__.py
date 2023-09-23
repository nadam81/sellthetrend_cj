import os

from importlib import metadata
from pathlib import Path

__version__ = metadata.version("squeezer")

WORKDIR = Path(os.getenv("WORKDIR", Path.cwd()))
DATADIR = WORKDIR / "data"