#!/usr/bin/env python

"""
Flask-Collect
-------------

Setup module.

"""
from os import path
from sys import version_info

from setuptools import setup, find_packages

from flask_collect import __version__, __license__


def read(fname):
    try:
        return open(path.join(path.dirname(__file__), fname)).read()
    except IOError:
        return ''


install_requires = [
    l for l in read('requirements.txt').split('\n')
    if l and not l.startswith('#')]

if version_info < (2, 7):
    install_requires.append('importlib')


META_DATA = dict(
    name='Flask-Collect',
    version=__version__,
    license=__license__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    platforms=('Any'),
    keywords = "flask static deploy".split(),

    author='Kirill Klenov',
    author_email='horneds@gmail.com',
    url=' http://github.com/klen/Flask-Collect',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],

    packages=find_packages(),
    include_package_data=True,
    install_requires = install_requires,
    test_suite = 'tests',
)


if __name__ == "__main__":
    setup(**META_DATA)
