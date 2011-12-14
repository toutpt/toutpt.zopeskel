Introduction
============

This package provide new templates for ZopeSkel_ 2.X.

It contains at the moment only one template for Plone.

How to install
==============

This can be installed by using easy_install, pip or buildout. 
An example of buildout can be found at https://github.com/toutpt/mypythontools

Templates
=========

toutpt_diazotheme
-----------------

Create a Plone theme using plone.app.theming.

The theme is a copy of sunburst theme but using 960 css.

The package profile install the theme, activate it, and reset public.css and
column.css (aka deco).  It loads all resources in corresponding registry plus
modernizr_ in the jsregistry.

toutpt_collectivejs
-------------------

Create a package to provide a javascript library to Plone. Many collective.js.* packages can be found like jqueyrui.

This template has been used to create collective.js.formalize.

Credits
=======

Companies
---------

|makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact us <mailto:python@makina-corpus.org>`_

Authors

  - JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

Contributors

  - 

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _ZopeSkel: http://pypi.python.org/pypi/ZopeSkel
.. _modernizr: http://modernizr.com
