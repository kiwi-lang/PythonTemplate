"""Top level module for {{cookiecutter.project_name}}"""

import importlib
import json
import pkgutil

import importlib_resources

__descr__ = "{{cookiecutter.description}}"
__version__ = "{{cookiecutter.version}}"
__license__ = "{{cookiecutter.license}}"
__author__ = "{{cookiecutter.author}}"
__author_email__ = "{{cookiecutter.email}}"
__copyright__ = "{{cookiecutter.copyright}} {{cookiecutter.author}}"
__url__ = "{{cookiecutter.url}}"


def discover_plugins(module):
    """Discover uetools plugins"""
    path = module.__path__
    name = module.__name__

    plugins = {}

    for _, name, _ in pkgutil.iter_modules(path, name + "."):
        plugins[name] = importlib.import_module(name)
        print(f" - Found plugin: {name}")

    return plugins


data_path = importlib_resources.files("{{cookiecutter.project_name}}.data")

with open(data_path / "data.json", encoding="utf-8") as file:
    print(json.dumps(json.load(file), indent=2))
