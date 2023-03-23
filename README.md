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

## Layout

```
   project
   ├── .github/workflows
   |    ├── publish.yml       # Publish package to PyPi
   |    ├── style.yml         # Test for style (black, isort, pep8)
   |    └── test.yml          # Run unit tests
   ├── docs
   |    ├── conf.py           # Sphinx configuration
   |    ├── requirements.txt  # Sphinx requirements
   |    └── index.rst         # Sphinx main page
   ├── examples
   ├── project                # Project namespace
   |    ├── core              # Project code
   |    |    ├── __init__.py
   |    |    └── somecode.py
   |    ├── data              # Project bundled data
   |    └── plugins           # Project plugin namespace extendable by third parties
   |        └── example
   |            └── __init__.py
   ├── tests                  # Project tests
   |    ├── requirements.txt
   |    └── test_project.py   
   ├── LICENSE                # Project license
   ├── MANIFEST.in            
   ├── README.rst             # README and first page of doc
   ├── requirements.txt       # package requirements
   ├── setup.py               # Project installation definitition
   └── tox.ini                # Automation
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
