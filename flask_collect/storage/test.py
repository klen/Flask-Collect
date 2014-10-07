# -*- coding: utf-8 -*-
#
# This file is part of Flask-Collect.
# Copyright (C) 2012, 2013 Kirill Klenov.
# Copyright (C) 2014 CERN.
#
# Flask-Collect is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""List files from all static folders."""

from .base import BaseStorage


class Storage(BaseStorage):

    """Dummy storage engine."""

    def run(self):
        """List all file paths."""
        return [f for f in self]
