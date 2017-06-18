#!/usr/bin/env python
import os

from distutils.core import setup
from commands import getoutput

version = getoutput('git describe --always') or '1.0'

setup(name='gtalkbot',
      version=version,
      description='XMpp client to Gtalk, and integration with raspberry based on mitchtech version',
      author='mitchtech, Marlon Olaya',
      author_email='marlon.olaya.ac@gmail.com',
      url='https://github.com/mitchtech/raspi_gtalk_robot',
      packages=['gtalkbot'],
      scripts=['gtalk-bot'],
      classifiers=['Development Status :: 1 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries',
          'Topic :: System :: Networking']
     )
