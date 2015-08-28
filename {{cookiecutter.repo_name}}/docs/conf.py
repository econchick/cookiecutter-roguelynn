# -*- coding: utf-8 -*-

# for explaination of what each config option is,
# take a look at http://sphinx-doc.org/config.html

import codecs
import datetime
import os
import re
import sys

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), "rb", "utf-8") as f:
        return f.read()


def find_version(*file_paths):
    """
    Build a path from *file_paths* and search for a ``__version__``
    string inside.
    """
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def find_latest_release_date():
    """
    Build a date string from the latest release logged in ``changelog.rst``
    """
    changelog = read("changelog.rst")
    # format of either YYYY-MM-DD or YYYY/MM/DD
    date_regex = re.compile("(\d{4}[-/]\d{2}[-/]\d{2})")
    date_match = date_regex.findall(changelog)[0]
    if date_match:
        release_date = datetime.datetime.strptime(date_match, "%Y-%m-%d")
        fmt_release_date = release_date.strftime("%b %-d, %Y")
        return fmt_release_date
    raise RuntimeError("Unable to find latest release date in changelog.rst")


sys.path.append(os.path.abspath(os.path.pardir))

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.autosummary',
]
autodoc_member_order = 'bysource'
autoclass_content = 'class'

templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'

project = u'{{ cookiecutter.project_name }}'
year = datetime.date.today().year
copyright = u'{{ cookiecutter.year }}{0}, {{ cookiecutter.full_name}}'.format(
    u'-{0}'.format(year) if year != {{ cookiecutter.year }} else u""
)

release = find_version("../{{ cookiecutter.project_name }}/__init__.py")
version = release.rsplit(u".", 1)[0]
today = find_latest_release_date()

exclude_patterns = ['_build']

pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

if sphinx_rtd_theme:
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = "default"

# html_theme_options = {}
# html_theme_path = []
# html_title = None
# html_short_title = None
# html_logo = None
# html_favicon = "_static/favicon.ico"
html_static_path = ['_static']
# html_extra_path = []
# html_last_updated_fmt = '%b %d, %Y'
html_use_smartypants = True
# html_sidebars = {}
# html_additional_pages = {}
# html_domain_indices = True
# html_use_index = True
# html_split_index = False
# html_show_sourcelink = True
# html_show_sphinx = True
html_show_copyright = True
# html_use_opensearch = ''
# html_file_suffix = None
htmlhelp_basename = '{{ cookiecutter.project_name }}doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # 'papersize': 'letterpaper',
    # 'pointsize': '10pt',
    # 'preamble': '',
}
latex_documents = [
    ('index', '{{ cookiecutter.project_name }}.tex',
     u'{{ cookiecutter.project_name }} Documentation',
     u'{{ cookiecutter.full_name }}', 'manual'),
]
# latex_logo = None
# latex_use_parts = False
# latex_show_pagerefs = False
# latex_show_urls = False
# latex_appendices = []
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

man_pages = [
    ('index', '{{ cookiecutter.project_name }}',
     u'{{ cookiecutter.project_name }} Documentation',
     [u'{{ cookiecutter.full_name }}'], 1)
]

# man_show_urls = False

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    ('index', '{{ cookiecutter.project_name }}',
     u'{{ cookiecutter.project_name }} Documentation',
     u'{{ cookiecutter.full_name }}',
     '{{ cookiecutter.project_name }}',
     '{{ cookiecutter.short_desc }}',
     'Miscellaneous'),
]

# texinfo_appendices = []
# texinfo_domain_indices = True
# texinfo_show_urls = 'footnote'
# texinfo_no_detailmenu = False
