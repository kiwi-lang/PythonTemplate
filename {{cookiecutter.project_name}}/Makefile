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

CONDA_ACTIVATE=. $$(conda info --base)/etc/profile.d/conda.sh ; conda activate

front:
	cd {{cookiecutter.project_name}}/ui && npm run dev

back:
	($(CONDA_ACTIVATE) py310; python -m {{cookiecutter.project_name}}.server.main)

alembic_gen:
	cd {{cookiecutter.project_name}}/alembic && alembic revision -m "create account table"

alembic-autogen:
	cd {{cookiecutter.project_name}}/alembic && alembic revision --autogenerate -m "makefile"

alembic-update:
	cd {{cookiecutter.project_name}}/alembic && alembic upgrade head

