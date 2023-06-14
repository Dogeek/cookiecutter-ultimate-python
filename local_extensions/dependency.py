from functools import lru_cache
import json
from urllib.request import urlopen
from typing import Dict, List

from jinja2.ext import Extension
from jinja2.environment import Environment


DEP_MAPPING = {
    "generic": [],
    "api": [
        "fastapi",
        "uvicorn",
        "pydantic",
        "tortoise-orm",
        "fastapi-admin",
        "orjson",
        "ujson",
        "itsdangerous",
        "jinja2",
        "httpx",
    ],
    "ml": [
        "tensorflow",
        "keras",
        "pandas",
        "numpy",
        "scikit-learn",
        "plotly",
    ],
    "cli": [
        "typer",
        "rich",
        "shellingham",
        "xdgconfig",
    ],
    "gui": [
        "pyqt5",
        "pyqt5-tools",
        "PyQtWebEngine",
    ],
    "sdk": [
        "requests",
        "pydantic",
        "ujson",
    ],
}

DEV_DEP_MAPPING = {
    "generic": [
        "black",
        "isort",
        "flake8",
    ],
}


class DependencyExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["deps"] = self.get_dependencies

    @lru_cache(maxsize=128, typed=True)
    def get_latest_version(self, package_name: str) -> str:
        releases = json.loads(
            urlopen(
                f"https://pypi.org/pypi/{package_name}/json"
            ).read()
        )["releases"]
        return sorted(releases, key=lambda x: x, reverse=True)[0]

    def get_next_major_version(self, package_name: str) -> str:
        latest_version = self.get_latest_version(package_name)
        major, *_ = latest_version.split(".")
        return f"{int(major) + 1}.0.0"

    def get_formatted_dependencies(self, mgr_type: str, mapping: Dict[str, List[str]]) -> str:
        dependency_manager, project_type = mgr_type.split(":")
        deps = mapping.get(project_type.lower(), mapping.get("generic", []))
        toml = "\n".join(
            f"{dep} = \"^{self.get_latest_version(dep)}\""
            for dep in deps
        )
        pep621 = "\n".join(
            f"{dep} >= {self.get_latest_version(dep)}, <{self.get_next_major_version(dep)}"
            for dep in deps
        )
        if dependency_manager == "poetry":
            return toml
        elif dependency_manager == "pdm":
            return pep621

    def get_dependencies(self, mgr_type: str):
        return self.get_formatted_dependencies(mgr_type, DEP_MAPPING)

    def get_dev_dependencies(self, mgr_type: str) -> str:
        return self.get_formatted_dependencies(mgr_type, DEV_DEP_MAPPING)