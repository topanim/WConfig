#!/usr/bin/env python

from io import open
from setuptools import setup, find_packages

"""
:authors: WHAOX
:license: MIT License, see LICENSE file
:copyright: (c) 2024 WHAOX
"""

version = '1.0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='whaox-wconfig',
    version=version,

    author='WHAOX',
    author_email='gorogannisan641@gmail.com',

    description="Library to simplify working with the environment",
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/topanim/WApi',

    license='MIT LICENSE, see LICENSE file',

    packages=find_packages(),
    install_requires=[],

    keywords=['python', 'env', 'environment', 'config']
)
