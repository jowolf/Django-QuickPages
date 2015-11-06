#!/usr/bin/env python

from distutils.core import setup

setup (
    name         = 'Django-QuickPages',
    packages     = ['quickpages'],
    version      = '1.0.1',
    description  = 'Simliar to django-flatpages, but better & more flexible - also does snippets.',
    author       = 'Joseph Wolff',
    author_email = 'joe@eracks.com',
    url          = 'https://github.com/jowolf/Django-QuickPages',
    download_url = 'https://github.com/jowolf/Django-QuickPages/archive/master.zip',
    license      = "BSD",
    install_requires = ['django-wysiwyg'],
)
