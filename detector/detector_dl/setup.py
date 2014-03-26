#!/usr/bin/env python
# This is Yangqing's extremely hacky code to install decaf on your machine
# assuming that you are using a Unix-like system. To install, do:
#   python setup.py build
#   python setup.py install
# You should be able to then use decaf in your python environment.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from distutils.util import convert_path
from fnmatch import fnmatchcase
import os
import sys

def find_packages(where='.'):
    out = []
    stack=[(convert_path(where), '')]
    while stack:
        where, prefix = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where,name)
            if ('.' not in name and os.path.isdir(fn) and
                os.path.isfile(os.path.join(fn, '__init__.py'))
               ):
                out.append(prefix+name)
                stack.append((fn, prefix+name+'.'))
    for pat in ['ez_setup', 'distribute_setup']:
        out = [item for item in out if not fnmatchcase(item, pat)]
    return out

def run_setup():
    if sys.version_info < (2, 7):
        sys.stderr.write("Decaf requires Python >= 2.7\n")
        exit(-1)
    # Before running setup, let's do a make since we have C shared libraries
    # to be build (note that they are not python extensions...)
    # It's kind of ugly, but let's just keep it this way for simplicity
    retval = os.system('cd decaf; make')
    if retval != 0:
        sys.stderr.write("Failed to build the C libraries; exiting.\n")
        exit(retval)
    setup(name='decaf',
          version='0.9',
          description='Deep convolutional neural network framework',
          author='Yangqing Jia',
          author_email='jiayq84@gmail.com',
          packages=find_packages(),
          package_data={'decaf': ['util/_data/*'],
                        'decaf.demos.jeffnet': ['static/*', 'templates/*'],
                        'decaf.demos.notebooks': ['*.ipynb'],
                        'decaf.layers.cpp': ['libcpputil.so'],
                       },
          install_requires=[
              'matplotlib',
              'networkx',
              'numexpr',
              'numpy',
              'pydot',
              'scipy',
              'scikit-image',
          ],
          extras_require={
              'benchmarks': ['theano'],
              'mpi': ['mpi4py'],
              'demo': [
                  'python-gflags',
                  'flask',
                  'tornado',
                  'PIL',
              ],
          }
    )

if __name__ == '__main__':
    run_setup()
