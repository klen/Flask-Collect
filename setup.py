#!/usr/bin/env python
import os

from setuptools import setup, find_packages

from flask_collect import version, project, license


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


META_DATA = dict(
    name=project,
    version=version,
    license=license,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    platforms=('Any'),

    author='Kirill Klenov',
    author_email='horneds@gmail.com',
    url=' http://github.com/klen/Flask-Collect',

    packages=find_packages(),
    install_requires = ('Flask>=0.8',),
    test_suite = 'tests',
)


if __name__ == "__main__":
    setup(**META_DATA)
