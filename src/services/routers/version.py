from fastapi import APIRouter
from src.core.__version__ import VERSION
from src.services.models.version import Version

router = APIRouter()


@router.get("/version", response_model=Version)
async def get_version():
    """
    Returns the current version of the API.
    """
    return Version(version=VERSION)
