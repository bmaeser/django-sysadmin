#!/usr/bin/env python
# -*- coding: utf-8 -*-

import django_sysadmin
import os
from setuptools import setup, find_packages


## dependencies 
install_requires = [
    'Django>=1.4.1',
]

packages = find_packages()

setup(
    name='django-sysadmin',
    version=django_sysadmin.__version__,
    author='Bernhard Maeser',
    author_email='bernhard.maeser@gmail.com',
    url='https://github.com/bmaeser/django-sysadmin',
    license="MIT",
    description="Django models to make a sysadmins life easier",
    long_description=open('README.rst').read(),
    packages = packages,
    include_package_data=True,
    install_requires = install_requires,
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Installation/Setup',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)