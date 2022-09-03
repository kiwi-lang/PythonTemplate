Python Seed project
===================

Features:

* Sphinx doc generation
    * Read the docs ready
* Github CI
    * Test Coverage + Doctest
    * black formatting
    * pylint
    * isort
    * docs8

* pip installable

```
pip install cookiecutter
cookiecutter https://github.com/kiwi-lang/PythonTemplate

```

## Automation

* Auto format your code before pushing

```
tox -e checks
```

*  PYPI publishing automation
    * Add ``TEST_PYPI_PASSWORD`` and ``PYPI_PASSWORD`` secrets to the publish job
    * Manually start the publish workflow for the tag you want to release


## Plugins

User can extend you library using plugins


## Data

You can add user data using the ``data`` folder inside your module
