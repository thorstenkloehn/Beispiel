# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Beispiel Dokument'
copyright = '2023, Thorsten Klöhn'
author = 'Thorsten Klöhn'
from recommonmark.parser import CommonMarkParser
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
