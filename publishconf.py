#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


SITEURL = 'http://blog.minchin.ca'
SITE_ROOT_URL = 'http://minchin.ca'
RELATIVE_URLS = False
LOAD_CONTENT_CACHE = False

FEED_DOMAIN = SITEURL

# DELETE_OUTPUT_DIRECTORY = True

PLUGINS = PLUGINS + [
            'minchin.pelican.plugins.image_process',
            'minchin.pelican.plugins.cname',
            'minchin.pelican.plugins.nojekyll',
            'minify',  # pelican-minify
            'extended_sitemap',  # pelican-extended-sitemap
            'minchin.pelican.plugins.optimize_images',  # need executables for Linux to do this on Travis-CI
          ]

OUTPUT_PATH = '../blog.minchin.ca-master/'

GOOGLE_ANALYTICS_UNIVERSAL = 'UA-384291-1'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'Minchin.ca Blog'
