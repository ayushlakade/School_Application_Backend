import logging
import logging.config
import os

LOG_DIR = "logs"
LOG_FILE = "app.log"

# Ensure the logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,  # Keeps existing loggers
    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(name)s] %(levelname)s : %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": f"{LOG_DIR}/{LOG_FILE}",
            "formatter": "default",
            "mode": "a",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)