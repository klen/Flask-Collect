from os import path as op, makedirs
from shutil import copy

from .base import BaseStorage


class Storage(BaseStorage):

    def run(self):
        self.log("Collect static from blueprints.")
        destination_list = set()
        for bp, f, o in self:
            destination = op.join(self.collect.static_root, o)
            destination_dir = op.dirname(destination)
            if not op.exists(destination_dir):
                makedirs(destination_dir)
            if destination in destination_list:
                self.log("{0} already copied".format(destination))
            if not op.exists(destination) or op.getmtime(destination) < op.getmtime(f):
                copy(f, destination)
                self.log(
                    "Copied: [%s] '%s'" % (bp.name, op.join(self.collect.static_url, destination)))
            destination_list.add(destination)
