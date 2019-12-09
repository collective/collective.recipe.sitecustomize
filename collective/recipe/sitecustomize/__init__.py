# -*- coding: utf-8 -*-

import logging
import os
import sys


class Recipe:
    def __init__(self, buildout, name, options):
        self.buildout, self.options, self.name = buildout, options, name
        self.logger = logging.getLogger(name)
        self.python = os.environ.get('PYTHON', sys.prefix)

        options['python-dir'] = os.path.join(
            self.python,
            'lib/python{0}.{1}'.format(
                sys.version_info.major,
                sys.version_info.minor,
            ),
        )

    def install(self):
        encoding = self.options.get(
            'encoding',
            os.environ.get('PYTHONIOENCODING', 'ascii'),
        )
        dest = os.path.join(
            self.options.get('python-dir'),
            'sitecustomize.py',
        )
        self.logger.info("Setting '{0}' encoding as default".format(encoding))

        sitecustomize = """import sys\nsys.setdefaultencoding('{0}')""".format(encoding)

        if os.path.isfile(dest):
            os.chmod(dest, 0o600)

        with open(dest, 'w') as f:
            f.write(sitecustomize)
