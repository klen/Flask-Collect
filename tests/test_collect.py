# -*- coding: utf-8 -*-
#
# This file is part of Flask-Collect.
# Copyright (C) 2012, 2013, 2014 Kirill Klenov.
# Copyright (C) 2014 CERN.
#
# Flask-Collect is free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.
import time
from os import path as op, remove

import subprocess
from flask import Flask, Blueprint
from functools import partial
from shutil import rmtree
from tempfile import mkdtemp
from unittest import TestCase

from flask_collect import Collect


def filter_(order, items):
    """Filter application blueprints."""
    def _key(item):
        if item.name in order:
            return order.index(item.name)
        return -1
    return sorted(items, key=_key)


class BaseTest(TestCase):

    def test_collect(self):
        app = Flask(__name__)

        blueprint = Blueprint(
            'test1', __name__, static_folder='static1',
            static_url_path='/static/test1')
        app.register_blueprint(blueprint)

        blueprint = Blueprint('test2', __name__, static_folder='static2')
        app.register_blueprint(blueprint)

        static_root = mkdtemp()

        app.config['COLLECT_STATIC_ROOT'] = static_root

        collect = Collect(app)
        collect.collect(verbose=True)

        self.assertTrue(op.exists(op.join(static_root, 'test1', 'test.css')))
        self.assertTrue(op.exists(op.join(static_root, 'js', 'test.js')))
        self.assertTrue(op.exists(op.join(static_root, 'app.css')))

        app.config['COLLECT_STORAGE'] = 'flask_collect.storage.test'
        collect = Collect(app)
        test = collect.collect(verbose=True)
        self.assertEqual(len(test), 3)

        rmtree(static_root)

    def test_filter(self):
        """Test blueprint filter."""
        app = Flask(__name__)

        blueprint = Blueprint('test1', __name__, static_folder='static1')
        app.register_blueprint(blueprint)

        blueprint = Blueprint('test3', __name__, static_folder='static3')
        app.register_blueprint(blueprint)

        static_root = mkdtemp()

        app.config['COLLECT_STATIC_ROOT'] = static_root
        app.config['COLLECT_FILTER'] = partial(filter_, ['test3', 'test1'])
        app.config['COLLECT_STORAGE'] = 'flask_collect.storage.test'

        collect = Collect(app)
        test = list(collect.collect(verbose=True))
        self.assertEqual(len(test), 2)
        self.assertTrue('static3' in test[1][1])

        app.config['COLLECT_FILTER'] = partial(filter_, ['test1', 'test3'])
        collect = Collect(app)
        test = list(collect.collect(verbose=True))
        self.assertTrue('static1' in test[1][1])

        rmtree(static_root)

    def test_file_storage(self):
        """Test file storage."""
        app = Flask(__name__)

        blueprint = Blueprint('test1', __name__, static_folder='static1')
        app.register_blueprint(blueprint)

        blueprint = Blueprint('test3', __name__, static_folder='static3')
        app.register_blueprint(blueprint)

        static_root = mkdtemp()

        app.config['COLLECT_STATIC_ROOT'] = static_root
        app.config['COLLECT_FILTER'] = partial(filter_, ['test3', 'test1'])
        app.config['COLLECT_STORAGE'] = 'flask_collect.storage.file'

        collect = Collect(app)
        collect.collect()

        with open(op.join(static_root, 'test.css'), 'r') as file_:
            self.assertTrue('body { color: red; }' in file_.read())

        rmtree(static_root)

    def test_file_storage_update(self):
        """Test file storage."""
        dummy_app = Flask(__name__)

        test_static3 = mkdtemp()
        dummy_bp = Blueprint('dummy', __name__, static_folder='static3')
        dummy_app.register_blueprint(dummy_bp)

        dummy_app.config['COLLECT_STATIC_ROOT'] = test_static3
        dummy_app.config['COLLECT_STORAGE'] = 'flask_collect.storage.file'

        dummy_collect = Collect(dummy_app)
        dummy_collect.collect()

        app = Flask(__name__)

        blueprint = Blueprint('test1', __name__, static_folder='static1')
        app.register_blueprint(blueprint)

        blueprint = Blueprint('test3', __name__, static_folder=test_static3)
        app.register_blueprint(blueprint)

        static_root = mkdtemp()

        app.config['COLLECT_STATIC_ROOT'] = static_root
        app.config['COLLECT_FILTER'] = partial(filter_, ['test1', 'test3'])
        app.config['COLLECT_STORAGE'] = 'flask_collect.storage.file'

        collect = Collect(app)
        collect.collect()

        with open(op.join(static_root, 'test.css'), 'r') as file_:
            self.assertTrue('body { color: blue; }' in file_.read())

        time.sleep(1)
        subprocess.call(['touch', op.join(test_static3, 'test.css')])

        # re-collect files
        collect.collect()

        # check that test3 was not added because it's newer
        with open(op.join(static_root, 'test.css'), 'r') as file_:
            self.assertTrue('body { color: blue; }' in file_.read())

        rmtree(test_static3)
        rmtree(static_root)

    def test_link_storage(self):
        """Test file storage."""
        dummy_app = Flask(__name__)

        test_static3 = mkdtemp()
        dummy_bp = Blueprint('dummy', __name__, static_folder='static3')
        dummy_app.register_blueprint(dummy_bp)

        dummy_app.config['COLLECT_STATIC_ROOT'] = test_static3
        dummy_app.config['COLLECT_STORAGE'] = 'flask_collect.storage.file'

        dummy_collect = Collect(dummy_app)
        dummy_collect.collect()

        with open(op.join(test_static3, 'test.css'), 'r') as file_:
            self.assertTrue('body { color: red; }' in file_.read())

        app = Flask(__name__)

        blueprint = Blueprint('test1', __name__, static_folder='static1')
        app.register_blueprint(blueprint)

        blueprint = Blueprint('test2', __name__, static_folder='static2')
        app.register_blueprint(blueprint)

        blueprint = Blueprint('test3', __name__, static_folder=test_static3)
        app.register_blueprint(blueprint)

        static_root = mkdtemp()

        app.config['COLLECT_STATIC_ROOT'] = static_root
        app.config['COLLECT_FILTER'] = partial(filter_, ['test3', 'test1'])
        app.config['COLLECT_STORAGE'] = 'flask_collect.storage.link'

        collect = Collect(app)
        collect.collect()

        with open(op.join(static_root, 'test.css'), 'r') as file_:
            self.assertTrue('body { color: red; }' in file_.read())

        with open(op.join(test_static3, 'test.css'), 'w') as file_:
            file_.write('body { color: green; }')

        with open(op.join(static_root, 'test.css'), 'r') as file_:
            self.assertTrue('body { color: green; }' in file_.read())

        # remove custom test.css and re-collect files
        remove(op.join(test_static3, 'test.css'))
        collect.collect()

        with open(op.join(static_root, 'test.css'), 'r') as file_:
            # we get the file content from test1
            self.assertTrue('body { color: blue; }' in file_.read())

        rmtree(test_static3)
        rmtree(static_root)

    def test_link_storage_update(self):
        """Test link storage update."""
        app = Flask(__name__)

        blueprint = Blueprint('test1', __name__, static_folder='static1')
        app.register_blueprint(blueprint)

        static_root = mkdtemp()

        app.config['COLLECT_STATIC_ROOT'] = static_root
        app.config['COLLECT_FILTER'] = partial(filter_, ['test1'])
        app.config['COLLECT_STORAGE'] = 'flask_collect.storage.link'

        collect = Collect(app)
        collect.collect()

        # Make sure a new link has been created pointing to test1
        with open(op.join(static_root, 'test.css'), 'r') as file_:
            self.assertTrue('body { color: blue; }' in file_.read())

        blueprint = Blueprint('test3', __name__, static_folder='static3')
        app.register_blueprint(blueprint)

        app.config['COLLECT_FILTER'] = partial(filter_, ['test3', 'test1'])
        collect = Collect(app)
        collect.collect()

        # Make sure a new link has been created pointing to test3
        with open(op.join(static_root, 'test.css'), 'r') as file_:
            self.assertTrue('body { color: red; }' in file_.read())

        rmtree(static_root)
