#!/usr/bin/env python

from distutils.core import setup

VERSION = 1

licenses = ( 'Python Software Foundation License'
           , 'GNU Library or Lesser General Public License (LGPL)'
           )

setup \
    ( name = 'hooks'
    , version = VERSION
    , description = ''
    , long_description = ''
    , author = 'Andrew Kornilov'
    , author_email = 'frutik@gmail.com'
    , maintainer = 'Andrew Kornilov'
    , maintainer_email = 'frutik@gmail.com'
    , url = 'https://github.com/frutik/hooks'
    , packages = ['hooks']
    , license = ', '.join (licenses)
    , platforms = 'Any'
    , classifiers =
        [ 'Development Status :: 5 - Production/Stable'
        , 'Environment :: Other Environment'
        , 'Intended Audience :: Developers'
        , 'Intended Audience :: Telecommunications Industry'
        , 'Operating System :: OS Independent'
        , 'Programming Language :: Python'
        , 'Programming Language :: Python :: 2.4'
        , 'Programming Language :: Python :: 2.5'
        , 'Programming Language :: Python :: 2.6'
        , 'Programming Language :: Python :: 2.7'
        , 'Topic :: Communications :: Internet Phone'
        , 'Topic :: Communications :: Telephony'
        , 'Topic :: Software Development :: Libraries :: Python Modules'
        ] + ['License :: OSI Approved :: ' + l for l in licenses]
    )
