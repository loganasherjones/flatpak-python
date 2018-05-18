# -*- coding: utf-8 -*-
#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages
import sys
import os


current_dir = os.path.abspath(os.path.dirname(__file__))
version_file = os.path.join(current_dir, 'hello', '__init__.py')

with io.open(version_file, encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='hello',
    version=version,
    description='A package that hits google',
    author='Logan Asher Jones',
    author_email='loganasherjones@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    install_requires=[
        'requests',
    ],
)
