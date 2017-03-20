# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('csv2keychain/__main__.py').read(),
    re.M
).group(1)

setup(
    name="cmdline-csv2keychain",
    packages=["csv2keychain"],
    entry_points={
        "console_scripts": ['csv2keychain = csv2keychain.__main__:main']
    },
    version=version,
    description="Tool for adding exported credentials from Chrome to the macOS keychain.",
    author="Nikita Tarasov",
    author_email="mail@ntarasov.ru",
    url="https://github.com/nntarasov/csv2keychain",
)