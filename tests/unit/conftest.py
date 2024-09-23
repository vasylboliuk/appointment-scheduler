"""conftest file."""

import pytest
from starlette.testclient import TestClient

from src.main import app


@pytest.fixture(scope="session")
def client() -> TestClient:
    """Test Client to execute api test."""
    yield TestClient(app)
