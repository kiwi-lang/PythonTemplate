import TemplateExample.plugins
from TemplateExample.core import discover_plugins


def test_plugins():
    plugins = discover_plugins(TemplateExample.plugins)

    assert len(plugins) == 1
