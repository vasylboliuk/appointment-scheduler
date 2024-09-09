from fastapi import FastAPI
import uvicorn

from src.core.configs import Settings
from src.services.routers.version import router as version_router

app = FastAPI()

# Include the version router
app.include_router(version_router, prefix="/api")


def main():
    """
    Main method represents entry point for start application.

    :return:
    """
    settings = Settings()
    uvicorn.run(app, host=settings.host, port=settings.port)


if __name__ == "__main__":
    main()
