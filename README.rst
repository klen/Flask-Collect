Flask-Collect
#############

Flack-Collect is simply application for collect static files in Flask project.
Serve static files with Flask -- bad idea for production, with this you will can
collect them in one command.

This extension checks application blueprints for static files and copy it
to specific folder (saves related paths).

.. image:: https://secure.travis-ci.org/klen/Flask-Collect.png?branch=develop
    :target: http://travis-ci.org/klen/Flask-Collect
    :alt: Build Status

.. contents::


Requirements
=============

- python 2.5 (importlib)
- python 2.6
- Flask >= 0.8


Installation
=============

**Flask-Collect** should be installed using pip: ::

    pip install Flask-Collect


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


Use Flask-Collect
=================

You can run: ::

    collect.collect(verbose=True)

or with command:

    $ ./manage.py collect


Bug tracker
===========

If you have any suggestions, bug reports or
annoyances please report them to the issue tracker
at https://github.com/klen/Flask-Collect/issues


Contributing
============

Development of adrest happens at github: https://github.com/klen/Flask-Collect


Contributors
=============

* klen_ (Kirill Klenov)


License
=======

Licensed under a `GNU lesser general public license`_.


.. _GNU lesser general public license: http://www.gnu.org/copyleft/lesser.html
.. _klen: http://klen.github.com/
