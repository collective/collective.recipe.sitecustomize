
.. contents::

Supported options
=================

This recipe supports the following options:

encoding
    Set default encoding, e.g. UTF-8. Defaults to ``ascii`` 


Example usage
=============

To use this recipe, just create a part for it and define the ``recipe``
parameter::

    [buildout]
    parts =
        ...
        unicode

    [unicode]
    recipe = collective.recipe.sitecustomize

This will configure the default option for ``encoding``. If you like
or need to you can override the parameter, e.g.::

    [unicode]
    recipe = collective.recipe.sitecustomize
    encoding = UTF-8


Code repository
===============

https://github.com/collective/collective.recipe.sitecustomize
