<h1>Python Skeleton</h1>

<p>
  <img src="https://img.shields.io/badge/python-blue?logo=python&logoColor=white" alt="Python Version"/>
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen" alt="Contributions Welcome"/>
  <img src="https://img.shields.io/badge/license-GPL%203.0-red" alt="GPL 3.0 License"/>
  <img src="https://img.shields.io/badge/Ruff-Linter-orange" alt="Ruff Linter"/>
  <img src="https://img.shields.io/badge/Docker-Multi--Stage-blue"/>
</p>

Welcome to **Python Skeleton** – a modern Python project starter template designed to streamline your development process. This template provides a solid foundation for new Python projects, ensuring you get up and running quickly.

- Quickstart project for modern python projects
- Code folder name should match the project title e.g. 'pyskel'
- Teach how to structure projects
- Multi-stage Dockerfile for fast builds

---

## Related documentation
https://packaging.python.org/en/latest/tutorials/packaging-projects/

---

## Disclaimer
**pyskel** is not looking to be an end-all solution to the "perfect" project setup, there is no such thing. It merely seeks to give an idea on how to setup a new python project in an organized and modern way. There are countless linters, formatters, and build backends not shown in this setup.

---

## Structure
```
.
├── pyproject.toml
├── package_name
│   ├── module_folder
│   │   ├── __init__.py
│   │   └── module_name.py
│   ├── __init__.py
│   ├── __main__.py # main program entrypoint
├── tests
│   ├── test_module_name.py
├── tox.ini
```

---

## 🏗️ Install
```
python -m venv venv
source venv/bin/activate
python -m pip install .
python -m pyskel
```

---

## 🧪 Run tests
```
pip install -e .[dev]
tox
```

---

## Lint
```
pip install -e .[dev]
ruff check --fix
```
