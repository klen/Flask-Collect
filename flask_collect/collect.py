# coding: utf-8

from importlib import import_module
from os import path as op


class Collect():
    """This class is used for integration to one or more Flask
    applications.

    :param app: Flask application

    ::

        app = Flask(__name__)
        collect = Collect(app)

    The second possibility is to create the object once and configure the
    application later to support it::

        collect = Collect()
        ...
        collect.init_app(app)

    """

    def __init__(self, app=None):
        self.static_root = None
        self.storage = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        """This callback can be used to initialize an application for the
        use with this collect setup.

        See :ref:`configuration`.

        :param app: Flask application

        """
        if not hasattr(app, 'extensions'):
            app.extensions = dict()
        app.extensions['collect'] = self

        self.static_root = app.config.get('COLLECT_STATIC_ROOT',
                                          op.join(app.root_path, 'static')).rstrip('/')
        self.storage = app.config.get(
            'COLLECT_STORAGE', 'flask.ext.collect.storage.file')

    def init_script(self, manager):
        """This callback can be used to initialize collect scripts with
        `Flask-Script`_ manager instance.

        :param manager: `Flask-Script`_ manager

        This added manager collect command: ::

            $ ./manage.py collect -h
            usage: ./manage.py collect [-h] [-v]

            Collect static from blueprints.

            optional arguments:
            -h, --help     show this help message and exit
            -v, --verbose

        .. _Flask-Script: http://packages.python.org/Flask-Script/

        """
        @manager.command
        def collect(verbose=True):
            " Collect static from blueprints. "
            self.collect(verbose=verbose)
        assert collect

    def collect(self, verbose=False):
        """Collect static files from blueprints.

        :param verbose: Show debug information.

        """
        mod = import_module(self.storage)
        cls = getattr(mod, 'Storage')
        storage = cls(self, verbose=verbose)
        storage.run()
