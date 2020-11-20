#!/usr/bin/env python
from setuptools import setup


if __name__ == '__main__':
    setup(
        name='{{cookiecutter.project_name}}',
        version='0.0.0',
        description='{{cookiecutter.description}}',
        author='{{cookiecutter.author}}',
        packages=[
            '{{cookiecutter.project_name}}',
        ],
        setup_requires=['setuptools'],
        tests_require=['pytest', 'flake8', 'codecov', 'pytest-cov'],
    )
