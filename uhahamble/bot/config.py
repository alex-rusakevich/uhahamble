import logging
import logging.config
import multiprocessing
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from redis import StrictRedis

load_dotenv()

DEBUG: bool = bool(os.environ.get("DEBUG", True))

BOT_TOKEN = os.environ["BOT_TOKEN"]

PROGRAM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOG_LVL = "DEBUG" if DEBUG else "INFO"
LOG_DIR = Path(PROGRAM_DIR, "logs")

LOG_DIR.mkdir(parents=True, exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "default": {
            "level": LOG_LVL,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "log.txt",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
            "formatter": "standard",
        },
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {
            "handlers": ["default", "console"],
            "level": LOG_LVL,
            "propagate": True,
        },
    },
}

logging.config.dictConfig(LOGGING)

logger = logging.getLogger(__name__)

REDIS_PREFIX = os.environ.get("REDIS_PREFIX")
NO_CACHE: bool = bool(os.environ.get("NO_CACHE", False))
redis = StrictRedis()

logger.info(f"Cache disabled: {NO_CACHE}")

THREADS_COUNT = multiprocessing.cpu_count()
