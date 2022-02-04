# Configuration file for the Sphinx documentation builder.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import sys
sys.path.append('../../')


# -- Project information
exec(open("../../lumispy/release_info.py").read())  # grab version info

project = 'LumiSpy'
copyright = copyright
author = author

release = version
version = version

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '../media/logo_sq_april21.svg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '../media/lumispy.ico'

# -- Options for EPUB output
epub_show_urls = 'footnote'
