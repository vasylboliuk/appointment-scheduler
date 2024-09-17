import pytest
from assertpy import assert_that
from fastapi import status

from tests.src.base_src_test import BaseSrcTest


@pytest.mark.api
class TestVersion(BaseSrcTest):
    """
    Unit Tests class to cover Version endpoint.
    """

    def test_get_version(self, client):
        response = self.client.get("api/version")
        # validation
        assert_that(response.status_code).is_equal_to(status.HTTP_200_OK)
        assert_that(response.json()).contains("version")
