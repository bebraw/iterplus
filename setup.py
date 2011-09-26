#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import iterplus


def long_description():
    files = ('README.rst', 'docs/changelog.rst', )
    read_files = map(lambda a: open(a).read(), files)

    return reduce(lambda a, b: a + '\n\n' + b, read_files)

setup(name='iterplus',
    version=iterplus.__version__,
    description='iterplus provides functionality that extends itertools',
    long_description=long_description(),
    author=iterplus.__author__,
    author_email='bebraw@gmail.com',
    url='http://github.com/bebraw/iterplus',
    license='MIT',
    keywords=['functional programming', 'itertools', ],
    packages=['iterplus', ],
    package_dir={'iterplus': 'iterplus', },
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
          'Topic :: Software Development',
          ],
    )

