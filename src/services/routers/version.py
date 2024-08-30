from fastapi import APIRouter
from src.core.version import VERSION

router = APIRouter()


@router.get("/version", response_model=dict)
async def get_version():
    """
    Returns the current version of the API.
    """
    return {"version": VERSION}
