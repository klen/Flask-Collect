# coding: utf-8

"""Define *Flask* extension."""
from os import path as op

from flask import current_app
from flask._compat import string_types
from werkzeug.local import LocalProxy
from werkzeug.utils import import_string


collect_proxy = LocalProxy(
    lambda: current_app.extensions['collect'].collect
)


class _CollectState(object):

    """Extension state."""

    def __init__(self, app):
        """Build a new state object."""
        self.app = app
        self.static_root = app.config.get(
            'COLLECT_STATIC_ROOT',
            op.join(
                app.root_path,
                'static')).rstrip('/')
        self.static_url = app.static_url_path

        self.storage = app.config.get(
            'COLLECT_STORAGE', 'flask_collect.storage.file')

        filter_ = app.config.get('COLLECT_FILTER')
        if filter_ is not None and isinstance(filter_, string_types):
            filter_ = import_string(filter_)
        self.filter = filter_ if filter_ is not None else list

        # Save link on blueprints
        self.blueprints = app.blueprints

    def collect(self, verbose=False):
        """Collect static files from blueprints.

        :param verbose: Show debug information.
        """
        mod = import_string(self.storage)
        cls = getattr(mod, 'Storage')
        storage = cls(self, verbose=verbose)
        return storage.run()


class Collect(object):
    """Extension object for integration to one or more Flask applications.

    :param app: Flask application

    .. code-block:: python

        app = Flask(__name__)
        collect = Collect(app)

    The second possibility is to create the object once and configure the
    application later to support it:

    .. code-block:: python

        collect = Collect()
        ...
        collect.init_app(app)

    """

    def __init__(self, app=None):
        """Initilize the extension object."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Initialize an application for the use with this collect setup.

        See :ref:`configuration`.

        :param app: Flask application
        """
        if not hasattr(app, 'extensions'):
            app.extensions = dict()
        self._state = app.extensions['collect'] = _CollectState(app)

        if hasattr(app, 'cli'):
            import click

            @app.cli.command()
            @click.option('--verbose', is_flag=True)
            def collect(verbose=True):  # noqa
                """Collect static files."""
                collect_proxy(verbose=verbose)

    def init_script(self, manager):  # noqa
        """Initialize collect scripts with `Flask-Script`_ manager instance.

        :param manager: `Flask-Script`_ manager

        This added manager collect command:

        .. code-block:: console

            $ ./manage.py collect -h
            usage: ./manage.py collect [-h] [-v]

            Collect static from blueprints.

            optional arguments:
            -h, --help     show this help message and exit
            -v, --verbose

        .. _Flask-Script: http://packages.python.org/Flask-Script/
        """
        manager.command(collect_proxy)

    def __getattr__(self, name):
        """Proxy to state object."""
        return getattr(self._state, name, None)
