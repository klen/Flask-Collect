from unittest import TestCase


class BaseTest(TestCase):

    def test_collect(self):
        from tempfile import mkdtemp
        from flask import Flask, Blueprint
        from flask_collect import Collect
        from os import path as op

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
        self.assertTrue(len(test), 2)
