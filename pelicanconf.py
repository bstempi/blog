#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brian Stempin'
SITENAME = u"BMS's Blog"
SITEURL = 'http://brianstempin.com'
SITESUBTITLE = 'Because my crap has to live somewhere'

PATH = 'content'

THEME = 'theme/'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('GitHub', 'https://github.com/bstempi'),
          ('LinkedIn', 'https://www.linkedin.com/in/brianstempin'),
          ('Facebook', 'https://www.facebook.com/brian.stempin'),
          ('Twitter', 'https://twitter.com/bstempi'),
         )

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

# For when I have one
# SITELOGO = 'images/my_site_logo.png'

# For when I have one
# FAVICON = 'images/favicon.png'

# Currently doesn't work; Put in PR to fix this.
CUSTOM_CSS = 'static/custom.css'

HIDE_SITENAME = True

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/custom.css', 'extra/CNAME', 'notebooks']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/CNAME': {'path': 'CNAME'},
}

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

ARTICLE_EXCLUDES = ['notebooks']
PAGE_EXCLUDES = ['notebooks']

# Share
SHARE = True