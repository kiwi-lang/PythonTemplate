"""Top level module for TemplateExample"""

import importlib
import json
import pkgutil

import importlib_resources

__descr__ = "TemplateDescription"
__version__ = "0.0.1"
__license__ = "TemplateLicense"
__author__ = "TemplateAuthor"
__author_email__ = "TemplateEmail"
__copyright__ = "1234 TemplateAuthor"
__url__ = "TemplateUrl"


def discover_plugins(module):
    """Discover uetools plugins"""
    path = module.__path__
    name = module.__name__

    plugins = {}

    for _, name, _ in pkgutil.iter_modules(path, name + "."):
        plugins[name] = importlib.import_module(name)
        print(f" - Found plugin: {name}")

    return plugins


data_path = importlib_resources.files("TemplateExample.data")

with open(data_path / "data.json", encoding="utf-8") as file:
    print(json.dumps(json.load(file), indent=2))
