from jinja2.ext import Extension
from jinja2.environment import Environment


class LicenseClassifierExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters['to_license_classifier'] = self.to_license_classifier

    def to_license_classifier(self, license: str) -> str:
        classifiers = {
            "MIT": "License :: OSI Approved :: MIT License",
            "Proprietary": "License :: Other/Proprietary License",
            "Apache-2.0": "License :: OSI Approved :: Apache Software License",
            "GPL-3.0": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "AGPL-3.0": "License :: OSI Approved :: GNU Affero General Public License v3",
            "LGPL-3.0": "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Unlicense": "License :: OSI Approved :: The Unlicense (Unlicense)",
            "MPL-2.0": "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        }
        return classifiers.get(license, "License :: Other/Proprietary License")
