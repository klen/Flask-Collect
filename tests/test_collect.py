from flask import Flask, Blueprint
from flask_collect import Collect
from functools import partial
from os import path as op
from tempfile import mkdtemp
from unittest import TestCase


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

        app.config['COLLECT_STORAGE'] = 'flask.ext.collect.storage.test'
        collect = Collect(app)
        test = collect.collect(verbose=True)
        self.assertEqual(len(test), 3)

    def test_filter(self):
        app = Flask(__name__)

        blueprint = Blueprint('test1', __name__, static_folder='static1')
        app.register_blueprint(blueprint)

        blueprint = Blueprint('test3', __name__, static_folder='static3')
        app.register_blueprint(blueprint)

        static_root = mkdtemp()

        def filter_(order, items):
            def _key(item):
                if item.name in order:
                    return order.index(item.name)
                return -1
            return sorted(items, key=_key)

        app.config['COLLECT_STATIC_ROOT'] = static_root
        app.config['COLLECT_FILTER'] = partial(filter_, ['test3', 'test1'])
        app.config['COLLECT_STORAGE'] = 'flask.ext.collect.storage.test'

        collect = Collect(app)
        test = list(collect.collect(verbose=True))
        self.assertEqual(len(test), 3)
        self.assertTrue('static3' in test[1][1])

        app.config['COLLECT_FILTER'] = partial(filter_, ['test1', 'test3'])
        collect = Collect(app)
        test = list(collect.collect(verbose=True))
        self.assertTrue('static1' in test[1][1])
