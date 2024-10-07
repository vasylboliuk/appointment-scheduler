"""main file."""

import logging

import uvicorn
from fastapi import FastAPI

from src.core.configs import Settings
from src.core.logging_manager import LoggingManager
from src.services.routers.version import router as version_router

app = FastAPI()

# Include the version router
app.include_router(version_router, prefix="/api")


def main():
    """Main method represents entry point for start application.

    :return:
    """
    settings = Settings()
    LoggingManager.setup_logger_string_format()
    logging.info("Starting application...")
    uvicorn.run(
        app, host=settings.host, port=settings.port, log_config=None
    )  # log_config=None enable own custom logs for this lib


if __name__ == "__main__":
    main()
