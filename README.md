<h1 algin="center">🚀 Python Skeleton</h1>

Welcome to **Python Skeleton** – a modern Python project starter template designed to streamline your development process. This template provides a solid foundation for new Python projects, ensuring you get up and running quickly.

- Quickstart project for modern python projects
- Code folder name should match the project title e.g. 'pyskel'
- Teach beginner pythoneers how to structure projects

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
