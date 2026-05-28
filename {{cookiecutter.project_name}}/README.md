# {{cookiecutter.project_name}}

[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_name}})
[![Python Versions](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_name}})
[![Tests](https://github.com/{{cookiecutter.github}}/{{cookiecutter.project_name}}/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/{{cookiecutter.github}}/{{cookiecutter.project_name}}/actions/workflows/test.yml)
[![Codecov](https://codecov.io/gh/{{cookiecutter.github}}/{{cookiecutter.project_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github}}/{{cookiecutter.project_name}})

{{cookiecutter.description}}

```bash
pip install {{cookiecutter.project_name}}
```

## Quick Start

```bash
# Clone and setup
git clone https://github.com/{{cookiecutter.github}}/{{cookiecutter.project_name}}.git
cd {{cookiecutter.project_name}}

# Create virtual environment
uv venv .uv
source .uv/bin/activate

# Install
make install
cd {{cookiecutter.project_name}}/ui && npm install && cd ../..

# Run development servers
make front  # Terminal 1: UI on :3000
make back   # Terminal 2: API on :5001
```

## Build

```bash
make build  # Builds UI + Python wheel with bundled frontend
```

## License

{{cookiecutter.license}}
