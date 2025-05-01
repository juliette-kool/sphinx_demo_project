# Configuration file for the Sphinx documentation builder.

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx Demo Project'
copyright = '2025, Juliette Kool'
author = 'Juliette Kool'
release = '0.1'

html_title = f"{project} v{release}"
html_short_title = f"{project} v{release}"
html_context = {
    "display_github": True,
    "display_version": True,
    "version": release,
}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'special-members': '__init__',
    'show-inheritance': True,
}
templates_path = ['_templates']
exclude_patterns = []

language = 'english'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
master_doc = 'index'
html_theme = 'furo'
html_baseurl = "https://juliette-kool.github.io/sphinx_demo_project/"
html_static_path = ['_static']  # if not already defined


# Inject project version manually
html_context = {
    "project_version": release,  # custom field
}

html_theme_options = {
    "sidebar_hide_name": False,  # sidebar shows the project name
    "light_logo": "systemiq_logo.png",
    "dark_logo": "systemiq_logo_dark.jpg",
}