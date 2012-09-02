# -*- coding: utf-8 -*-
import os
import sys

from flask_collect import __version__ as release

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Flask-Collect'
copyright = u'2012, Kirill Klenov'
version = '.'.join(release.split('.')[:2])
exclude_patterns = ['_build']
html_use_modindex = False
html_show_sphinx = False
htmlhelp_basename = 'Flask-Collectdoc'
latex_documents = [
    ('index', 'Flask-Collect.tex', u'Flask-Collect Documentation',
        u'Kirill Klenov', 'manual'),
]
latex_use_modindex = False
latex_elements = {
    'fontpkg':      r'\usepackage{mathpazo}',
    'papersize':    'a4paper',
    'pointsize':    '12pt',
    'preamble':     r'\usepackage{flaskstyle}'
}
latex_use_parts = True
latex_additional_files = ['flaskstyle.sty', 'logo.pdf']
man_pages = [
    ('index', 'flask-mixer', u'Flask-Collect Documentation',
     [u'Kirill Klenov'], 1)
]
pygments_style = 'tango'
html_theme = 'default'
html_theme_options = {}

sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']
html_theme = 'flask'
