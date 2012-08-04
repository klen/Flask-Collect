from importlib import import_module
from os import path as op


class Collect():

    def __init__(self, app=None):
        self.app = app
        self.static_root = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

        if not hasattr(self.app, 'extensions'):
            self.app.extensions = dict()

        if 'static' in self.app.extensions:
            raise Exception('Can not have more than one instance of the Static class associated with Flask application')

        self.app.extensions['static'] = self

        self.static_root = self.app.config.get('COLLECT_STATIC_ROOT', op.join(self.app.root_path, 'static')).rstrip('/')
        self.storage = self.app.config.get('COLLECT_STORAGE', 'flask.ext.collect.storage.file')

    def init_script(self, manager):
        @manager.command
        def collect(verbose=True):
            " Collect static from blueprints. "
            self.collect(verbose=verbose)
        assert collect

    def collect(self, verbose=False):

        mod = import_module(self.storage)
        cls = getattr(mod, 'Storage')
        storage = cls(self, verbose=verbose)
        storage.run()
