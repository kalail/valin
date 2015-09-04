#!/usr/bin/env python
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""


from codecs import open  # To use a consistent encoding
from os import path
from setuptools import setup

import valin

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='valin',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=valin.VERSION,

    description='Library to help with data modeling',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/kalail/valin',

    # Author details
    author='Kashif Malik',
    author_email='kashif610@gmail.com',
)
