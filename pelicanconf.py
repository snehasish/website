#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'snehasish'
SITENAME = u'Snehasish'
SITEURL = 'http://www.snehasish.net'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# My settings
MARKUP=(('rst', 'md'))
STATIC_PATHS=['robots.txt', 'docs', 'CNAME']
EXTRA_PATH_METADATA = {'CNAME': {'path': 'CNAME'},}
THEME="single-page"
SITESUBTITLE=''
READERS = {'html': None}

# ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
