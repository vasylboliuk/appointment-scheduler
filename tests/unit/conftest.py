"""conftest file."""

import pytest
from starlette.testclient import TestClient

from src.core.logging_manager import LoggingManager
from src.main import app


@pytest.fixture(scope="session")
def setup(request):
    """Setup before all tests."""
    LoggingManager.setup_logger_string_format()


@pytest.fixture(scope="session")
def client() -> TestClient:
    """Test Client to execute api test."""
    yield TestClient(app)
