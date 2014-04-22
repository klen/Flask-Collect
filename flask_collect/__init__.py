# -*- coding: utf-8 -*-
"""
    Flask-Collect
    =============

    Flack-Collect is simply application for collect static files in Flask_
    project.
    Serve static files with Flask_ -- bad idea for production, with this you
    will can collect them in one command.

    This extension checks application blueprints for static files and copy it
    to specific folder (saves related paths).

"""

from .collect import Collect

__author__ = "Kirill Klenov <horneds@gmail.com>"
__license__ = "BSD"
__project__ = __name__
__version__ = "0.2.3"
