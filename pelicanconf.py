#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fireforce Technology'
SITENAME = 'Fireforce Technology'
SITEURL = ''  # https://www.fireforce-technology.ch

PATH = 'content'

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = 'fr'

THEME = 'themes/bootstrap2'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Ordonnance sur la protection de l’air (OPair)',
          'https://www.admin.ch/opc/fr/classified-compilation/19850321/index.html'),
         ('Directive de protection incendie - Installations thermiques',
          'https://services.vkg.ch/rest/public/georg/bs/publikation/documents/BSPUB-1394520214-115.pdf/content'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True