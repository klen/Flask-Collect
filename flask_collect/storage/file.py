# -*- coding: utf-8 -*-
#
# This file is part of Flask-Collect.
# Copyright (C) 2012, 2014 Kirill Klenov.
# Copyright (C) 2014 CERN.
#
# Flask-Collect is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Copy files from all static folders to root folder."""

from os import path as op, makedirs
from shutil import copy

from .base import BaseStorage


class Storage(BaseStorage):

    """Storage that copies static files."""

    def run(self):
        """Collect static files from blueprints."""
        self.log("Collect static from blueprints.")
        destination_list = set()
        for bp, f, o in self:
            destination = op.join(self.collect.static_root, o)
            destination_dir = op.dirname(destination)
            if not op.exists(destination_dir):
                makedirs(destination_dir)
            if destination in destination_list:
                self.log("{0} already copied".format(destination))
            elif not op.exists(destination) or \
                    op.getmtime(destination) < op.getmtime(f):
                copy(f, destination)
                self.log(
                    "Copied: [%s] '%s'" % (
                        bp.name,
                        op.join(self.collect.static_url, destination)))
            # Always add destination to avoid overwrites by newer version
            # from next blueprint with same file.
            destination_list.add(destination)
