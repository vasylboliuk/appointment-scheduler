"""test version file."""

import pytest
from assertpy import assert_that
from fastapi import status


@pytest.mark.api
class TestVersion:
    """Unit Tests class to cover Version endpoint."""

    def test_get_version(self, client):
        """Test: Verify retrieve version.

        :param client:
        :return:
        """
        response = client.get("api/version")
        # validation
        assert_that(response.status_code).is_equal_to(status.HTTP_200_OK)
        assert_that(response.json()).contains("version")
