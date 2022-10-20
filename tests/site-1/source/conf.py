# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test 1'
copyright = '2022, test author'
author = 'test author'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_plausible"]
plausible_domain="domain-test-1"

# For tests
import os
if 'SPHINX_PLAUSIBLE_DEACTIVATE' in os.environ:
    plausible_enabled = False

templates_path = ['_templates']
exclude_patterns = []
master_doc = 'index' # for old sphinx, new name is root_doc but default is OK


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
