"""Utils.

This module provides classes to represent utils.
"""

import yaml


class FileUtil:
    """File Util class represents methods working with files."""

    @staticmethod
    def read_yaml_file(file_path: str) -> dict:
        """Read yaml file by "file_path".

        :param file_path:
        :return:
        """
        with open(file_path, "r", encoding="utf-8") as f:
            file_data = yaml.safe_load(f.read())
        return file_data
