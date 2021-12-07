"""Top level module for {{cookiecutter.project_name}}"""

__descr__ = "{{cookiecutter.description}}"
__version__ = "{{cookiecutter.version}}"
__license__ = "{{cookiecutter.license}}"
__author__ = u"{{cookiecutter.author}}"
__author_email__ = "{{cookiecutter.email}}"
__copyright__ = u"{{cookiecutter.copyright}} {{cookiecutter.author}}"
__url__ = "{{cookiecutter.url}}"


def my_function(lhs: int, rhs: int) -> int:
    """Add two numbers together

    Parameters
    ----------
    lhs: int
        first integer

    rhs: int
        second integer

    Raises
    ------
    value errror if lhs == 0

    Examples
    --------

    >>> my_function(1, 2)
    3
    >>> my_function(0, 2)
    Traceback (most recent call last):
      ...
    ValueError

    """
    if lhs == 0:
        raise ValueError()

    return lhs + rhs
