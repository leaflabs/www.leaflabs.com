#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Staff'
SITENAME = u'LeafLabs'
SITEURL = 'http://leaflabs.com'

TIMEZONE = 'UTC'
DATE_FORMATS = { 'en': '%A, %B %d, %Y', }

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 6

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_LANG_URL = '{lang}/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_LANG_SAVE_AS = '{lang}/{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{lang}/{slug}/'
PAGE_LANG_SAVE_AS = '{lang}/{slug}/index.html'
INDEX_SAVE_AS = 'blog/index.html'
ARCHIVES_SAVE_AS = 'blog/archives/index.html'

#AUTHOR_SAVE_AS = False
#CATEGORY_SAVE_AS = False
#TAG_SAVE_AS = False

PATH = '.'
ARTICLE_DIR = ('posts')
PAGE_DIR = ('pages')
#FILES_TO_COPY = (('style', 'style'), )
STATIC_PATHS = ['style']
TEMPLATE_PAGES = {'home.html': 'index.html'}

DIRECT_TEMPLATES = ('index', 'archives')

FEED_ALL_RSS = 'main.xml'
FEED_MAX_ITEMS = '20'

THEME = "leaflabs_theme"
THEME_STATIC_PATHS = ['style', ]

MARKUP = ('rst', 'md', 'html')
