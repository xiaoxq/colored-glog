#!/usr/bin/env python

import os
import setuptools

VERSION = '1.1.0'

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setuptools.setup(
    name='colored-glog',
    author='Xiangquan Xiao',
    author_email='xiaoxiangquan@gmail.com',
    url='https://github.com/xiaoxq/colored-glog',
    install_requires=[
        'python-gflags>=3.1',
        'six',  # glog doesn't need six, but gflags 3.1 does and its distutils
                # "requires" line apparently accomplishes nothing, so ...
        'termcolor',
    ],
    description='Colored Google-style logging wrapper for Python.',
    long_description=README,
    py_modules=['colored_glog'],
    license='BSD',
    test_suite='tests',
    version=VERSION,
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: System :: Logging',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
)
