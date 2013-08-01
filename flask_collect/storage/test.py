from .base import BaseStorage


class Storage(BaseStorage):

    def run(self):
        return [f for f in self]
