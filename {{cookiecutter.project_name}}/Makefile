install:
	pip install -e .[all]
	pip install -r requirements.txt
	pip install -r docs/requirements.txt
	pip install -r tests/requirements.txt

doc: build-doc

build-doc:
	sphinx-build -W --color -c docs/ -b html docs/ _build/html

serve-doc:
	sphinx-serve

update-doc: build-doc serve-doc

tests-doc:
	COVERAGE_FILE=.coverage.docstring coverage run --parallel-mode -m pytest --cov={{cookiecutter.project_name}} --doctest-modules {{cookiecutter.project_name}}

tests-integration:
	COVERAGE_FILE=.coverage.integration coverage run --parallel-mode -m pytest --cov={{cookiecutter.project_name}} tests/integration

tests-end-to-end:
	COVERAGE_FILE=.coverage.end2end coverage run --parallel-mode -m pytest --cov={{cookiecutter.project_name}} tests/end2end

tests-unit:
	COVERAGE_FILE=.coverage.unit coverage run --parallel-mode -m pytest --cov={{cookiecutter.project_name}} tests/unit

tests-combine:
	coverage combine
	coverage report -m
	coverage xml

tests-codecov: tests-combine
	codecov

tests-all: tests-doc tests-unit tests-integration tests-end-to-end

tests: tests-all tests-codecov
