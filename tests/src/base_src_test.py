import pytest
from starlette.testclient import TestClient

from src.main import app


class BaseSrcTest:
    @pytest.fixture
    def client(self):
        self.client = TestClient(app)
