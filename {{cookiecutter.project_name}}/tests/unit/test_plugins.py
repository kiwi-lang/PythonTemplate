import {{cookiecutter.project_name}}.plugins
from {{cookiecutter.project_name}}.core import discover_plugins


def test_plugins():
    plugins = discover_plugins({{cookiecutter.project_name}}.plugins)

    assert len(plugins) == 1
