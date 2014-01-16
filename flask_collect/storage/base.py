""" Abstract Storage. """
from __future__ import print_function

from os import path as op, walk


class BaseStorage():

    """ Base class for storages. """

    def __init__(self, collect, verbose=False):
        self.verbose = verbose
        self.collect = collect

    def __iter__(self):
        """ Seek static files and result full and relative paths.

        :return generator: Walk files

        """
        for bp in [self.collect.app] + list(self.collect.blueprints.values()):
            if bp.has_static_folder and op.isdir(bp.static_folder):
                for root, _, files in walk(bp.static_folder):
                    for f in files:
                        fpath = op.join(root, f)
                        opath = op.relpath(fpath, bp.static_folder.rstrip('/'))
                        if bp.static_url_path and self.collect.static_url and \
                                bp.static_url_path.startswith(
                                    op.join(self.collect.static_url, '')): # noqa
                            opath = op.join(
                                op.relpath(
                                    bp.static_url_path,
                                    self.collect.static_url), opath)
                        yield bp, fpath, opath

    def log(self, msg):
        """ Log message. """
        if self.verbose:
            print(msg)
