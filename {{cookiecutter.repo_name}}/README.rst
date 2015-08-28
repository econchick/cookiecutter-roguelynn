{{ cookiecutter.project_name }}
===============================


.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg?style=flat-square
   :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
   :alt: CI status

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg?style=flat-square
   :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/{{ cookiecutter.repo_name }}.svg?style=flat-square
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
    :alt: Development Status

.. image:: https://img.shields.io/pypi/l/{{ cookiecutter.repo_name }}.svg?style=flat-square
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/blob/master/LICENSE
   :alt: License

.. image:: https://img.shields.io/coveralls/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master.svg?style=flat-square
   :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master
   :alt: Current coverage

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}.svg?style=flat-square
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
    :alt: Supported Python versions


.. begin

Requirements and Installation
=============================

User Setup
----------

The latest stable version can be found on PyPI_, and you can install via pip_::

   $ pip install {{ cookiecutter.repo_name }}

``{{ cookiecutter.project_name }}`` runs on Python 2.7, and 3.3+, and PyPy. Both Linux and OS X are supported.

Continue onto `usage`_ to get started on using ``{{ cookiecutter.project_name }}``.


Developer Setup
---------------

If you'd like to contribute or develop upon ``{{ cookiecutter.project_name }}``, be sure to read `How to Contribute`_
first.


System requirements:
^^^^^^^^^^^^^^^^^^^^

- 2.7, 3.3+, or PyPy
- virtualenv_

Here's how to set your machine up::

    $ git clone git@github.com:{{ cookiecutter.github_username}}/{{ cookiecutter.repo_name}}
    $ cd {{ cookiecutter.repo_name}}
    $ virtualenv env
    $ source env/bin/activate
    (env) $ pip install -r dev-requirements.txt


Run Tests
^^^^^^^^^

If you'd like to run tests for all supported Python versions, you must have all Python versions
installed on your system.  I suggest pyenv_ to help with that.

To run all tests::

    (env) $ tox

To run a specific test setup (options include: `py27``, ``py33``, ``py34``, ``pypy``,
``flake8``, ``verbose``, ``manifest``, ``docs``, ``setup``, ``setupcov``)::

    (env) $ tox -e py27

To run tests without tox::

    (env) $ py.test
    (env) $ py.test --cov {{ cookiecutter.project_name }} --cov-report term-missing


Build Docs
^^^^^^^^^^

Documentation is build with Sphinx_, written in rST, uses the `Read the Docs`_ theme with
a slightly customized CSS, and is hosted on `Read the Docs site`_.

To rebuild docs locally, within the parent ``{{ cookiecutter.project_name }}`` directory::

    (env) $ tox -e docs

or::

    (env) $ sphinx-build -b docs/ docs/_build

Then within ``{{ cookiecutter.project_name }}/docs/_build`` you can open the index.html page in your browser.


.. _pip: https://pip.pypa.io/en/latest/installing.html#install-pip
.. _PyPI: https://pypi.python.org/project/{{ cookiecutter.repo_name }}/
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
.. _pyenv: https://github.com/yyuu/pyenv
.. _Sphinx: http://sphinx-doc.org/
.. _`Read the Docs`: https://github.com/snide/sphinx_rtd_theme
.. _`Read the Docs site`: https://{{ cookiecutter.repo_name }}.readthedocs.org
.. _`usage`: http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/usage.html
.. _`How to Contribute`: http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/contributing.html
