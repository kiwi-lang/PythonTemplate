Python Seed project
===================

Features:

* Sphinx doc generation
    * Read the docs ready
* Github CI
    * Test Coverage + Doctest
    * black formating
    * pylint
    * isort
    * docs8

* pip installable

```
pip install cookiecutter
cookiecutter https://github.com/kiwi-lang/python_seed
```

## Automation

Auto format your code before pushing

```
tox -e run-block
tox -e run-isort
```
