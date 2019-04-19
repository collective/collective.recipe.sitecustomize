# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

name = "collective.recipe.sitecustomize"
tests_require = ['testfixtures', 'zc.buildout [test]', 'zope.testing']

setup(
    name = name,
    version = "1.0",
    author = "Cleber J Santos",
    author_email = "cleber@cleberjsantos.com.br",
    description = "Add sitecustomize.py to set Python default encoding",
    long_description = open("README.rst").read(),
    license = "GPL",
    keywords = "zc.buildout buildout recipe",
    classifiers = [
        "Framework :: Buildout :: Recipe",
        "Framework :: Buildout",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    url='https://github.com/collective/' + name,
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires = ['zc.buildout', 'setuptools'],
    entry_points = {'zc.buildout':
                    ['default = %s:Recipe' % name]},
    tests_require=tests_require,
    extras_require=dict(test=tests_require),
    test_suite = 'collective.recipe.sitecustomize.tests.test_docs.test_suite',
    )
