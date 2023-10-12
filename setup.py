#!/usr/bin/env python
from pathlib import Path

from setuptools import setup

with open("TemplateExample/core/__init__.py") as file:
    for line in file.readlines():
        if "version" in line:
            version = line.split("=")[1].strip().replace('"', "")
            break

extra_requires = {"plugins": ["importlib_resources"]}
extra_requires["all"] = sorted(set(sum(extra_requires.values(), [])))

if __name__ == "__main__":
    setup(
        name="TemplateExample",
        version=version,
        extras_require=extra_requires,
        description="TemplateDescription",
        long_description=(Path(__file__).parent / "README.rst").read_text(),
        author="TemplateAuthor",
        author_email="TemplateEmail",
        license="TemplateLicense",
        url="https://TemplateExample.readthedocs.io",
        classifiers=[
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Operating System :: OS Independent",
        ],
        packages=[
            "TemplateExample.core",
            "TemplateExample.plugins.example",
        ],
        setup_requires=["setuptools"],
        install_requires=["importlib_resources"],
        package_data={
            "TemplateExample.data": [
                "TemplateExample/data",
            ],
        },
    )
