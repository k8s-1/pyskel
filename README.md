<p align="center">
  # 🚀 Python Skeleton
</p>

<br></br>

<p align="center">
  <img src="https://img.shields.io/badge/python-blue?logo=python&logoColor=white" alt="Python Version"/>
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen" alt="Contributions Welcome"/>
  <img src="https://img.shields.io/badge/license-GPL%203.0-red" alt="GPL 3.0 License"/>
</p>

<br></br>

Welcome to **Python Skeleton** – a modern Python project starter template designed to streamline your development process. This template provides a solid foundation for new Python projects, ensuring you get up and running quickly.

- Quickstart project for modern python projects
- Code folder name should match the project title e.g. 'pyskel'
- Teach beginner pythoneers how to structure projects

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
pip install tox pytest
tox
```
