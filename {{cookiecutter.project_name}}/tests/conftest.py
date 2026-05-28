"""Shared test fixtures."""

import pytest
from fastapi.testclient import TestClient

from {{cookiecutter.project_name}}.server.app import create_app


@pytest.fixture
def client():
    app = create_app()
    with TestClient(app) as c:
        yield c
