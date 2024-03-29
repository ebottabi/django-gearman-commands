# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import django_gearman_commands

# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-gearman-commands',
    version=django_gearman_commands.__version__,
    description='Django management commands for working with Gearman job server from Django framework',
    long_description=read('README.rst'),
    author=u'Jozef Ševčík',
    author_email='sevcik@codescale.net',
    url='http://www.codescale.net/en/community#django-gearman-commands',
    download_url='http://github.com/jsk/django-gearman-commands/tarball/master',
    license='BSD',
    keywords = 'django gearman gearmand jobs queue',
    packages=['django_gearman_commands'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Framework :: Django',
    ],
)
