"""conftest file."""

import os
import sys

import pytest
from starlette.testclient import TestClient

from src.core.constants import CommonPaths
from src.core.logging_manager import LoggingManager
from src.main import app


def _setup_logger_for_tests():
    """Setup logger for tests."""
    sys.path.append(str(CommonPaths.project_root))
    # create log folder if not exists
    project_root = CommonPaths.project_root.parent
    tests_path = CommonPaths.tests_path
    tests_log_path = tests_path.joinpath("logs")
    os.makedirs(tests_log_path, exist_ok=True)
    os.makedirs(project_root.joinpath("logs"), exist_ok=True)  # create log dir in project root
    # replace log file path with tests package
    config = LoggingManager.get_logger_configurations()
    origin_config_file_path = config["handlers"]["file"]["filename"]
    config["handlers"]["file"]["filename"] = str(tests_path.joinpath(origin_config_file_path))
    LoggingManager.init_logger(config)


@pytest.fixture(scope="session", autouse=True)
def setup():
    """Setup before all tests."""
    _setup_logger_for_tests()


@pytest.fixture(scope="session")
def client() -> TestClient:
    """Test Client to execute api test."""
    yield TestClient(app)
