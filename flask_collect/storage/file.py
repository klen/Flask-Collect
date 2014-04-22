from os import path as op, makedirs
from shutil import copy2

from .base import BaseStorage


class Storage(BaseStorage):

    def run(self):
        self.log("Collect static from blueprints.")
        for bp, f, o in self:
            destination = op.join(self.collect.static_root, o)
            destination_dir = op.dirname(destination)
            if not op.exists(destination_dir):
                makedirs(destination_dir)

            if (
                not op.exists(destination)
                    or op.getmtime(destination) < op.getmtime(f)):
                copy2(f, destination)
                self.log(
                    "Copied: [%s] '%s'" %
                    (bp.name,
                     op.join(
                         self.collect.static_url,
                         destination)))
