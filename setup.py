import sys
import os
from distutils.core import setup, Extension


marsharelax = Extension('marsharelax',
                        sources = ['marsharelax.c'])


setup(name = 'marsharelax',
      version = '0.1',
      description = 'marsharelax',
      ext_modules = [marsharelax])

