import tomllib
from pathlib import Path

UHAHAMBLE_ROOT = Path(__file__).parent.parent
__version__ = tomllib.loads((UHAHAMBLE_ROOT / "pyproject.toml").read_text())\
    ["tool"]["poetry"]["version"]
