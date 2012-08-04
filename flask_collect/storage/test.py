from .base import BaseStorage


class Storage(BaseStorage):

    def run(self, app, verbose=False):
        self.verbose = verbose
        return [f for f in self]
