import pytest
from assertpy import assert_that

from src.core.constants import CommonPaths
from src.core.utils import FileUtil
from tests.src.base_src_test import BaseSrcTest


@pytest.mark.core
class TestUtils(BaseSrcTest):
    """
    Unit Tests class to cover Utils methods.
    """

    def test_read_yaml_file(self):
        file_path = CommonPaths.resource_path.joinpath("app_config.yml")
        file_content = FileUtil.read_yaml_file(file_path)
        # validation
        assert_that(file_content).is_not_none()
        assert_that(file_content).is_not_empty()
        assert_that(file_content).contains("host", "port")
