from os import path as op, walk


class BaseStorage():

    def __init__(self, collect, verbose=False):
        self.verbose = verbose
        self.collect = collect

    def __iter__(self):
        " Seek static files and result full and relative paths. "
        app = self.collect.app
        for bp in app.blueprints.values():
            if bp.static_folder and op.isdir(bp.static_folder):
                for root, _, files in walk(bp.static_folder):
                    for f in files:
                        fpath = op.join(root, f)
                        opath = op.relpath(fpath, bp.static_folder.rstrip('/'))
                        if bp.static_url_path and bp.static_url_path.startswith(op.join(app.static_url_path, '')):
                            opath = op.join(op.relpath(bp.
                                                       static_url_path, app.static_url_path), opath)
                        yield bp, fpath, opath

    def log(self, msg):
        if self.verbose:
            print msg
