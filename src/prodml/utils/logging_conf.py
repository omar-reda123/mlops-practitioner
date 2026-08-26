import logging
import sys
from logging.handlers import RotatingFileHandler
from prodml.utils.config import settings


def setup_logging() -> logging.Logger:
  
    log_level = logging.DEBUG if settings.DEBUG else logging.INFO
    log_format = "%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

    logger = logging.getLogger("prodml")
    logger.setLevel(log_level)

    if logger.hasHandlers():
        logger.handlers.clear()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    log_file_path = settings.LOGS_DIR / "logs.log"
    file_handler = RotatingFileHandler(
        filename=str(log_file_path),
        maxBytes=10 * 1024 * 1024,  
        backupCount=5,              
        encoding="utf-8",
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False

    logger.info("Logging initialized successfully (Standard logging).")
    return logger


logger = setup_logging()

