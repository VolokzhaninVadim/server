# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'server'
copyright = '2025, Volokzhanin Vadim'
author = 'Volokzhanin Vadim'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx_markdown_builder',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_togglebutton',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = [
    'build/*'
]

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_sidebars = {
    '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
    'using/windows': ['windowssidebar.html', 'searchbox.html'],
}
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
markdown_uri_doc_suffix = ".html"
pygments_style = 'sphinx'
source_suffix = ['.rst', '.md']
myst_heading_anchors = 4