.. _configuration:

Configuration
=============

The following configuration values exist for Flask-SQLAlchemy.
Flask-SQLAlchemy loads these values from your main Flask config which can
be populated in various ways.  Note that some of those cannot be modified
after the engine was created so make sure to configure as early as
possible and to not modify them at runtime.

Configuration Keys
------------------

A list of configuration keys currently understood by the extension:

=============================== =========================================
``COLLECT_STATIC_ROOT``         Path to folder for collect static files.
                                By default: *<APP_ROOT>/static*.

``COLLECT_STORAGE``             Import path to storage backend.
                                By default: *flask.ext.collect.storage.file*.

``COLLECT_FILTER``              Import path to filter function that can
                                manipulate blueprints before iterating in
                                :meth:`~flask_collect.storage.base.StorageBase`.
                                By default: *flask.ext.collect.storage.file*.
=============================== =========================================
