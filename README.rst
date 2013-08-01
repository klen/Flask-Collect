Flask-Collect
#############

.. _description:

Flack-Collect is simply application for collect static files in Flask project.
Serve static files with Flask -- bad idea for production, with this you will can
collect them in one command.

This extension checks application blueprints for static files and copy it
to specific folder (saves related paths).

.. _badges:

.. image:: https://secure.travis-ci.org/klen/Flask-Collect.png?branch=develop
    :target: http://travis-ci.org/klen/Flask-Collect
    :alt: Build Status

.. image:: https://coveralls.io/repos/klen/Flask-Collect/badge.png?branch=develop
    :target: https://coveralls.io/r/klen/Flask-Collect
    :alt: Coverals

.. image:: https://pypip.in/v/Flask-Collect/badge.png
    :target: https://crate.io/packages/Flask-Collect
    :alt: Version

.. image:: https://pypip.in/d/Flask-Collect/badge.png
    :target: https://crate.io/packages/Flask-Collect
    :alt: Downloads

.. image:: https://dl.dropboxusercontent.com/u/487440/reformal/donate.png
    :target: https://www.gittip.com/klen/
    :alt: Donate


.. _documentation:


**Docs are available at https://flask-collect.readthedocs.org/. Pull requests with documentation enhancements and/or fixes are awesome and most welcome.**


.. _contents:

.. contents::


.. _requirements:

Requirements
=============

- python (2.6, 2.7, 3.3)
- Flask_ >= 0.10.1


.. _installation:

Installation
=============

**Flask-Collect** should be installed using pip: ::

    pip install Flask-Collect


.. _setup:

Setup
=====

Flask-Collect settings (default values): ::

    # Target static dir
    COLLECT_STATIC_ROOT = <APP.ROOT_PATH>/static
    COLLECT_STORAGE = 'flask.ext.collect.storage.file'

Initialize Flask-Collect extenstion: ::

    from flask.ext.collect import Collect
    
    ...

    collect = Collect()
    collect.init_app(app)

If you use `Flask-Script <http://github.com/rduplain/flask-script>`_, activate Flask-Collect commands: ::

    from flask.ext.collect import Collect

    ...
    manager = Manager()
    ...

    collect = Collect()
    collect.init_app(app)
    collect.init_script(manager)


.. _usage:

Use Flask-Collect
=================

You can run: ::

    collect.collect(verbose=True)

or with command:

    $ ./manage.py collect


.. _bagtracker:

Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/klen/Flask-Collect/issues


.. _contributing:

Contributing
============

Development of flask-collect happens at github: https://github.com/klen/Flask-Collect


.. _license:

License
=======

Licensed under a `BSD license`_.


.. _links:

.. _BSD license: http://www.linfo.org/bsdlicense.html
.. _klen: http://klen.github.com/
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _Flask: http://flask.pocoo.org/
