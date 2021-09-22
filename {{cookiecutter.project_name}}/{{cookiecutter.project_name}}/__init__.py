__descr__ = '{{cookiecutter.description}}'
__version__ = '{{cookiecutter.version}}'
__license__ = '{{cookiecutter.license}}'
__author__ = u'{{cookiecutter.author}}'
__author_short__ = u'{{cookiecutter.author_short}}'
__author_email__ = '{{cookiecutter.email}}'
__copyright__ = u'{{cookiecutter.copyright}} {{cookiecutter.author}}'
__url__ = '{{cookiecutter.url}}'




def my_function(a: int, b: int) -> int:
    """Add two numbers together

    Parameters
    ----------
    a: int
        first integer

    b: int
        second integer

    Raises
    ------
    value errror if a == 0 

    Examples
    --------

    >>> my_function(1, 2)
    3
    >>> my_function(0, 2)
    Traceback (most recent call last):
      ...
    ValueError

    """
    if a == 0:
        raise ValueError()

    return a + b