"""Version model."""

from pydantic import BaseModel


class VersionResponse(BaseModel):
    """Version response model.

    Some text.
    """

    version: str
