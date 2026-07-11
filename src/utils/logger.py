"""
Application logging configuration.

Every module in the project should obtain its logger from this file.

Example:
    from utils.logger import get_logger

    logger = get_logger(__name__)
"""

import logging
from pathlib import Path


# Directory where log files will be stored.
LOG_DIR = Path("data/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger.

    Args:
        name: Usually __name__.

    Returns:
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers if the logger already exists.
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Write logs to the terminal.
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Write logs to a file.
    file_handler = logging.FileHandler(
        LOG_DIR / "pipeline.log",
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Prevent duplicate messages from the root logger.
    logger.propagate = False

    return logger