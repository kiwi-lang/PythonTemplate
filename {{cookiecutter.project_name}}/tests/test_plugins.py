"""Plugin discovery tests."""

import {{cookiecutter.project_name}}.plugins
from {{cookiecutter.project_name}}.cli import discover_commands


def test_discover_commands():
    commands = discover_commands()
    assert len(commands) >= 1
