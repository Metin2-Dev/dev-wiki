# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Standard Imports
import sys
import os
from datetime import datetime
from pathlib import Path

# Application Imports

# External Imports
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'Wiki'
copyright = f'2019-{datetime.now().year}'
author = 'test'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
needs_sphinx = "4.4"

sys.path.append(os.path.abspath("_extensions"))
extensions = [
    'myst_parser',
    'sphinx_design',
    "notfound.extension",
]

templates_path = ['_templates']
exclude_patterns = ["_build"]

notfound_context = {
    "title": "Page not found",
    "body": Path("_templates/404.html").read_text()
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_title = "Metin2Dev Wiki"
html_logo = "https://raw.githubusercontent.com/Metin2-Dev/Assets/main/128_round_black.png"

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "logo_only": True,
    "collapse_navigation": False,
}

html_static_path = ['_static']

html_css_files = [
    "css/custom.css",
]

html_js_files = [
]


# HTML Context options https://docs.readthedocs.io/en/latest/integrations.html
html_context = {
    "display_github": True,
    "github_user": "Metin2-Dev",
    "github_repo": "Wiki",
    "github_version": "main",
    "conf_py_path": "/",
}


# MyST configuration
myst_enable_extensions = ["colon_fence"]
