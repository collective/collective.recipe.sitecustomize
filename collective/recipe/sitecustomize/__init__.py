# -*- coding: utf-8 -*-
import logging
import os
import sys
import zc.buildout

class Recipe:
    def __init__(self, buildout, name, options):
        self.buildout, self.options, self.name = buildout, options, name
        self.logger = logging.getLogger(name)
        self.python = os.environ.get('PYTHON', sys.prefix)

        options['python-dir'] = os.path.join(
           self.python,
           'lib/python{}.{}'.format(
               sys.version_info.major,
               sys.version_info.minor
           )
        )

    def install(self):
        logger = logging.getLogger(self.name)
        encoding = self.options.get('encoding',
            os.environ.get('PYTHONIOENCODING', 'ascii') )
        dest = os.path.join(self.options.get('python-dir'),
            'sitecustomize.py'
        )
        self.logger.info("Setting '%s' encoding as default" % encoding)

        sitecustomize = """import sys\nsys.setdefaultencoding('%s')""" %encoding

        with open(dest, 'w') as f:
            f.write(sitecustomize)
        os.chmod(dest, 0600)
