"""Logging Manager.

This module provides classes to represent logging configuration.
"""

import json
import logging
import logging.config
import sys
from datetime import datetime

from src.core.configs import Settings


class PrintHandler(logging.StreamHandler):
    """Custom Print handler."""

    def emit(self, record):
        """Custom print handler.

        :param record:
        :return:
        """
        msg = self.format(record)
        print(msg)
        sys.stdout.flush()
        sys.stderr.flush()


class CustomJsonFormatter(logging.Formatter):
    """Custom JSON formatter."""

    def format(self, record: logging.LogRecord):
        """Custom json format for log message.

        :param record:
        :return:
        """
        log_message = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": record.name,
            "level": record.levelname,
            "filename": f"{record.filename}:{record.lineno}",
            "message": record.getMessage(),
        }
        return json.dumps(log_message)


class LoggingManager:
    """Custom Loging Manager."""

    @staticmethod
    def get_logger_configurations() -> dict:
        """Retrieve logger configuration."""
        settings = Settings()
        logger_configuration = settings.loggerConfiguration
        return logger_configuration

    @staticmethod
    def init_logger(configurations: dict):
        """Init logger by configurations."""
        logging.config.dictConfig(configurations)
        logger = logging.getLogger(__name__)
        return logger

    @staticmethod
    def setup_logger(**kwargs):
        """Setup application logger."""
        logger_configuration = LoggingManager.get_logger_configurations()
        logger = LoggingManager.init_logger(logger_configuration)
        return logger
