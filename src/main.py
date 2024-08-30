from fastapi import FastAPI

from src.services.routers.version import router as version_router

app = FastAPI()

# Include the version router
app.include_router(version_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    from src.core.utils import ConfigLoader

    properties = ConfigLoader.load_application_properties()
    uvicorn.run(app, **properties)
