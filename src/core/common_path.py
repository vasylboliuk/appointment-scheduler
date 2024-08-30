from pathlib import Path


class CommonPaths:
    project_root = Path(__file__).resolve().parent
    resource_path = project_root.joinpath("resources")
