#!/usr/bin/env python
import os
from pathlib import Path

from setuptools import setup

with open("{{cookiecutter.project_name}}/core/__init__.py") as file:
    for line in file.readlines():
        if "version" in line:
            version = line.split("=")[1].strip().replace('"', "")
            break

assert (
    os.path.exists(os.path.join("{{cookiecutter.project_name}}", "__init__.py")) is False
), "{{cookiecutter.project_name}} is a namespace not a module"

extra_requires = {"plugins": ["importlib_resources"]}
extra_requires["all"] = sorted(set(sum(extra_requires.values(), [])))

if __name__ == "__main__":
    setup(
        name="{{cookiecutter.project_name}}",
        version=version,
        extras_require=extra_requires,
        description="{{cookiecutter.description}}",
        long_description=(Path(__file__).parent / "README.rst").read_text(),
        author="{{cookiecutter.author}}",
        author_email="{{cookiecutter.email}}",
        license="{{cookiecutter.license}}",
        url="https://{{cookiecutter.project_name}}.readthedocs.io",
        classifiers=[
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Operating System :: OS Independent",
        ],
        packages=[
            "{{cookiecutter.project_name}}.core",
            "{{cookiecutter.project_name}}.plugins.example",
        ],
        setup_requires=["setuptools"],
        install_requires=["importlib_resources"],
        namespace_packages=[
            "{{cookiecutter.project_name}}",
            "{{cookiecutter.project_name}}.plugins",
        ],
        package_data={
            "{{cookiecutter.project_name}}.data": [
                "{{cookiecutter.project_name}}/data",
            ],
        },
    )
