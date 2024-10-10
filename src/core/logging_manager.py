"""Logging Manager.

This module provides classes to represent logging configuration.
"""

import json
import logging
import os
import sys
from datetime import datetime

import colorlog

from src.core.constants import CommonPaths


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

    _LOG_FILE_NAME = "appointment-scheduler.log"

    @staticmethod
    def init_logger_json_format():
        """Setup logger in custom JSON format.

        :return:
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        log_format = "%(log_color)s%(asctime)s - %(name)s - [%(levelname)s] -  %(filename)s:%(lineno)d - %(message)s"
        color_formatter = colorlog.ColoredFormatter(
            log_format,
            log_colors={"DEBUG": "cyan", "INFO": "green", "WARNING": "yellow", "ERROR": "red", "CRITICAL": "bold_red"},
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # File handler
        if not os.path.exists(CommonPaths.log_path):
            os.makedirs(CommonPaths.log_path)
        file_handler = logging.FileHandler(
            CommonPaths.log_path.joinpath(LoggingManager._LOG_FILE_NAME), encoding="utf-8"
        )
        console_handler = PrintHandler()

        handlers = [file_handler, console_handler]
        logging.basicConfig(level=logging.INFO, handlers=handlers, encoding="utf-8", force=True)
        for handler in logging.root.handlers:
            handler.setFormatter(color_formatter)
            handler.setFormatter(CustomJsonFormatter())

    @staticmethod
    def setup_logger_string_format():
        """Setup logger in custom string format.

        :return:
        """
        root_logger = logging.getLogger(__name__)
        root_logger.setLevel(logging.DEBUG)

        log_format = "%(log_color)s%(asctime)s - %(name)s - [%(levelname)s] -  %(filename)s:%(lineno)d - %(message)s"
        formatter = colorlog.ColoredFormatter(
            log_format,
            log_colors={"DEBUG": "cyan", "INFO": "green", "WARNING": "yellow", "ERROR": "red", "CRITICAL": "bold_red"},
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        if not os.path.exists(CommonPaths.log_path):
            os.makedirs(CommonPaths.log_path)

        file_handler = logging.FileHandler(
            CommonPaths.log_path.joinpath(LoggingManager._LOG_FILE_NAME), encoding="utf-8"
        )
        console_handler = PrintHandler()
        handlers = [file_handler, console_handler]
        logging.basicConfig(level=logging.INFO, handlers=handlers, encoding="utf-8", force=True)
        for handler in logging.root.handlers:
            handler.setFormatter(formatter)

        # Access the FastAPI logger
        fastapi_logger = logging.getLogger("fastapi")
        handler = PrintHandler()
        handler.setFormatter(formatter)

        fastapi_logger.handlers = []
        fastapi_logger.addHandler(handler)
        fastapi_logger.setLevel(logging.INFO)

        # Access the uvicorn logger
        uvicorn_logger = logging.getLogger("uvicorn.error")
        handler = PrintHandler()
        handler.setFormatter(formatter)

        uvicorn_logger.handlers = []
        uvicorn_logger.addHandler(handler)
        uvicorn_logger.setLevel(logging.INFO)
