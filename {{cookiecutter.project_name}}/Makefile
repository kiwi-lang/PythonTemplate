PROJECT = {{cookiecutter.project_name}}

.PHONY: install dev front back build-ui test lint clean

install:
	uv pip install -e ".[dev]"

dev: front back

front:
	cd $(PROJECT)/ui && npm run dev

back:
	$(PROJECT) serve

build-ui:
	cd $(PROJECT)/ui && npm ci && VITE_API_URL= VITE_BASE_PATH=/ npm run build

build: build-ui
	python -m build

test:
	pytest tests/

lint:
	ruff check .
	ruff format --check .

format:
	ruff check --fix .
	ruff format .

# Alembic targets
alembic-gen:
	cd $(PROJECT)/alembic && alembic revision -m "$(msg)"

alembic-autogen:
	cd $(PROJECT)/alembic && alembic revision --autogenerate -m "$(msg)"

alembic-upgrade:
	cd $(PROJECT)/alembic && alembic upgrade head

clean:
	rm -rf dist/ build/ *.egg-info
	rm -rf $(PROJECT)/server/static
	find . -type d -name __pycache__ -exec rm -rf {} +
