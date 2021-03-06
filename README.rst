Flask-Collect
#############

.. _description:

**Flask-Collect** is an extension for Flask that helps collecting static files.

Serving static files with *Flask* -- bad idea for production, this tool will
help you collect them in one command. It checks application and blueprints for
static files and copy them to specific folder (saves related paths).

.. _badges:

.. image:: http://img.shields.io/travis/klen/Flask-Collect.svg?style=flat-square
    :target: http://travis-ci.org/klen/Flask-Collect
    :alt: Build Status

.. image:: http://img.shields.io/coveralls/klen/Flask-Collect.svg?style=flat-square
    :target: https://coveralls.io/r/klen/Flask-Collect
    :alt: Coverals

.. image:: http://img.shields.io/pypi/v/flask-collect.svg?style=flat-square
    :target: https://pypi.python.org/pypi/flask-collect
    :alt: Version

.. image:: http://img.shields.io/pypi/dm/flask-collect.svg?style=flat-square
    :target: https://pypi.python.org/pypi/flask-collect
    :alt: Downloads


.. _documentation:

**Docs are available at** http://flask-collect.readthedocs.org/. **Pull
requests with documentation enhancements and/or fixes are awesome and most
welcome.**

.. _contents:

.. contents::


.. _requirements:

Requirements
=============

- python (2.6, 2.7, 3.3)
- Flask_ >= 0.10.1


.. _installation:

Installation
============

**Flask-Collect** should be installed using pip: ::

    pip install Flask-Collect


.. _setup:

Setup
=====

Flask-Collect settings (default values): ::

    # Target static dir
    COLLECT_STATIC_ROOT = <APP.ROOT_PATH>/static
    COLLECT_STORAGE = 'flask_collect.storage.file'

Initialize Flask-Collect extension: ::

    from flask_collect import Collect

    ...

    collect = Collect()
    collect.init_app(app)

If you use Flask-Script_, activate Flask-Collect commands: ::

    from flask_collect import Collect

    ...
    manager = Manager()
    ...

    collect = Collect()
    collect.init_app(app)
    collect.init_script(manager)

If you configure Flask via a factory function::

    from flask_collect import Collect

    ...

    def create_app():
        app = Flask()
        ...
        collect = Collect()
        collect.init_app(app)

        return app


.. _usage:

Use Flask-Collect
=================

From any python script: ::

    collect.collect(verbose=True)

with Flask-Script_: ::

    $ ./manage.py collect

with Flask>=0.11: ::

    $ flask collect


.. _bugtracker:

Bug tracker
===========

If you have any suggestions, bug reports or annoyances please report them
to the issue tracker at https://github.com/klen/Flask-Collect/issues


.. _contributing:

Contributors
============

Maintainer: Kirill Klenov (horneds@gmail.com)

Also see the `CONTRIBUTORS.rst
<https://github.com/klen/Flask-Collect/blob/develop/CONTRIBUTORS.rst>`_
file.

Contributing
============

Development of flask-collect happens at github:
https://github.com/klen/Flask-Collect


.. _license:

License
=======

Licensed under a `BSD license`_.


.. _links:

.. _BSD license: http://www.linfo.org/bsdlicense.html
.. _klen: http://klen.github.com/
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _Flask: http://flask.pocoo.org/
.. _Flask-Script: http://github.com/rduplain/flask-script
