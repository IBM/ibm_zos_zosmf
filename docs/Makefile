##############################################################################
# Copyright (c) IBM Corporation 2020                                         #
##############################################################################

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

view:
	open build/html/index.html

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

clean: 
	rm -rf build
	echo "Deleted directory build/"

	rm -rf source/_build
	echo "Deleted directory source/_build/"

	rm -rf source/modules
	echo "Deleted directory source/modules"
	echo "Completed HTML text generation, run 'make ibm_zos_zosmf'"

ibm_zos_zosmf: 
	mkdir build
	mkdir -p source/modules
	ansible-doc-extractor --template templates/module.rst.j2 source/modules ../plugins/modules/*.py
	echo "Completed restructured text generation, run 'make html'"

html:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "Completed HTML generation, run 'make html-all'"

html-all:
	@sphinx-versioning -l "$(ROOT_DIR)"/source/conf.py build  "$(ROOT_DIR)"/source/ "$(ROOT_DIR)"/build/html
	@echo "Completed HTML generation for git repository branches and/or tags, run 'make view'"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	echo "Completed HTML text generation, run 'make view'"