# Python Skeleton
<p align="center">
  <img src="https://raw.githubusercontent.com/python/python-docs-theme/main/images/python-logo.png" alt="Python Logo" width="200"/>
  <h1>🚀 Python Skeleton</h1>
</p>

Welcome to **Python Skeleton** – a modern Python project starter template designed to streamline your development process. This template provides a solid foundation for new Python projects, ensuring you get up and running quickly.

- Quickstart project for modern python projects
- Code folder name should match the project title e.g. 'pyskel'

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


## 🏗️ Install
```
python -m venv venv
source venv/bin/activate
python -m pip install .
python -m pyskel
```

## 🧪 Run tests
```
pip install tox pytest
tox
```
