MODULE=flask_collect
SPHINXBUILD=sphinx-build
ALLSPHINXOPTS= -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
BUILDDIR=_build


.PHONY: clean
clean:
	sudo rm -rf build dist
	find . -name "*.pyc" -delete
	find . -name "*.orig" -delete

.PHONY: install
install: remove _install clean

.PHONY: register
register: _register clean

.PHONY: upload
upload: _upload install

.PHONY: _upload
_upload:
	python setup.py sdist upload || echo 'Upload already'

.PHONY: _register
_register:
	python setup.py register

.PHONY: remove
remove:
	sudo pip uninstall -y $(MODULE) || echo "not installed"

.PHONY: _install
_install:
	sudo pip install -U .

.PHONY: test
test:
	python setup.py test
