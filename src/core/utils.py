"""Utils.

This module provides classes to represent utils.
"""

from src.core.constants import CommonPaths


class ConfigLoader:
    @staticmethod
    def load_application_properties(config_name="app.properties") -> dict:
        """
        Load application properties.
        :param config_name:
        :return: dict of properties
        """
        resources_dir_path = CommonPaths.project_root
        file_path = resources_dir_path.joinpath(config_name)
        properties = {}
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                key, value = line.split("=", 1)
                properties[key.strip()] = value.strip()
        return properties
