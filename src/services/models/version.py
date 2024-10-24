"""Version model."""

from pydantic import BaseModel


class VersionResponse(BaseModel):
    """Version response model.

    Temp Doc to remove.

    """

    version: str
