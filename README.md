# Ultimate Python Cookiecutter

This project is the ultimate python project scaffolding. It allows you to choose between several use cases, with sub categories
for most python uses, including

- Data Science
- Backend (API) development
- CLIs
- GUIs
- Python API SDKs
- Generic python package

These come with pre-loaded and pre-configured tooling such as code formatters, test frameworks, linters and so on.

This cookiecutter will also help deploying to cloud-native environment with kubernetes resources generation, docker integration, and several CI tools.

## Cookiecutter variables

| Variable             | Type                                                                                          |
| -------------------- | --------------------------------------------------------------------------------------------- |
| `name`               |                                                                                               |
| `slug`               |                                                                                               |
| `friendly_name`      |                                                                                               |
| `description`        |                                                                                               |
| `dependency_manager` | `pdm`, `poetry`                                                                               |
| `license`            | `MIT`, `Proprietary`, `Apache-2.0`, `GPL-3.0`, `AGPL-3.0`, `LGPL-3.0`, `Unlicense`, `MPL-2.0` |
| `author`             |                                                                                               |
| `email`              | matches `/^.+@.+\..+$/gm`                                                                     |
| `python_version`     | matches `/^\d+\.\d+\.\d+$/gm`                                                                 |
| `copyright_year`     | matches `/^\d{4,}$/gm`                                                                        |
| `type`               | `ML`, `API`, `CLI`, `GUI`, `SDK`, `None`                                                      |
| `editor`             | `vscode`, `none`                                                                              |
