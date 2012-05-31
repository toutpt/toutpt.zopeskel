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

toutpt_diazo960
---------------

Create a Plone theme using plone.app.theming.

The theme is pure Diazo theme using 960 css.

The package profile install the theme, activate it, and unactivate column.css
(aka deco). It loads all resources in corresponding registry.

toutpt_diazoboostrap
--------------------

Create a Plone theme using plone.app.theming.

The theme is pure Diazo theme using twitter's boostrap grid (responsive mode).

The package profile install the theme, activate it, and unactivate column.css
(aka deco) and mobile.css. It loads all resources in corresponding registry
and override the 'main_template' to reset the viewport.

toutpt_collectivejs
-------------------

Create a package to provide a javascript library to Plone. Many collective.js.* packages can be found like jqueyrui.

This template has been used to create collective.js.formalize.

toutpt_collective
-----------------

Create a package to be a collective addon. It will provides tests using plone.app.testing, upgrades for genericsetup and a browserlayer. All common needs are their.

Credits
=======

Companies
---------

|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact us <mailto:python@makina-corpus.org>`_

Authors

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

..Contributors

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _ZopeSkel: http://pypi.python.org/pypi/ZopeSkel
.. _modernizr: http://modernizr.com


