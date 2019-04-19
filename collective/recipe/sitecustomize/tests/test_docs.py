# -*- coding: utf-8 -*-

import doctest
import unittest

import zc.buildout.testing

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)


def setUp(test):
    zc.buildout.testing.buildoutSetUp(test)
    zc.buildout.testing.install_develop('collective.recipe.sitecustomize', test)


def test_suite():
    suite = unittest.TestSuite((
        doctest.DocFileSuite(
            'tests.txt',
            setUp=setUp,
            tearDown=zc.buildout.testing.buildoutTearDown,
            optionflags=optionflags,
        ),
    ))
    return suite
