#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import date

import seafoam

AUTHOR = 'Wm. Minchin'
SITENAME = 'Minchin.ca'
SITEURL = ''
SITE_ROOT_URL = 'http://minchin.ca'

TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = 'en'


# Caching
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True


# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
# USE_PAGER = False
PAGINATOR_LIMIT = 6

# static paths will be copied under the same name
# these are relative to the base CONTENT folder
STATIC_PATHS = ['images',
                '../extras',
                'css',
                'design',
                'js',
                'pages/img',
                '../.gitattributes',
                '../.gitignore',
                '../README.txt',
                ]
#STATIC_EXCLUDE = ['theme/less']

# A list of files to copy from the source to the destination
EXTRA_PATH_METADATA = {
    '../.gitattributes':            {'path': '.gitattributes'},
    '../.gitignore':                {'path': '.gitignore'},
    '../README.txt':                {'path': 'README.txt'},
    '../extras/minchin.ico':        {'path': 'favicon.ico'},
    }


# Custom settings
#FILENAME_METADATA = ('(?P<date>\d{4}-\d{2}-\d{2}).*')  # default?
#FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'  # extract date and slug
#FILENAME_METADATA = '(?P<slug>[\w-]*)'      # so anything before the file extension becomes the slug
FILENAME_METADATA = '(?P<date>\d{4}\d{2}\d{2})-(?P<slug>.*)'
## Please note that the metadata available inside your files takes precedence
#  over the metadata extracted from the filename.

MARKUP = (('rst',
           'md',
           'markdown',
           'mkd',
           'mdown',
           'html',
           'htm'))
PATH = 'content'
# OUTPUT_PATH = '../blog.minchin.ca-temp/'  # default is 'output/'

#FORMATTED_FIELDS = ['summary', 'title', ]


# Set URL's
TAG_URL = 'label/{slug}/'
TAG_SAVE_AS = 'label/{slug}/index.html'
TAGS_URL = 'label/'
TAGS_SAVE_AS = 'label/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'category/'
CATEGORIES_SAVE_AS = 'category/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_URL = '{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_URL = '{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL


# Add Blog to sidebar
MENUITEMS = (('Blog',        SITEURL + '/',                  'fa fa-fw fa-pencil'),
             ('Genealogy',   'http://minchin.ca/genealogy',  'glyphicon glyphicon-tree-deciduous'),
             ('My Projects', 'http://minchin.ca/projects/',  'fa fa-fw fa-flask'),
             ('Search',      'http://minchin.ca/search/',    'fa fa-fw fa-search'),
             ('About',       'http://minchin.ca/about/',     'fa fa-fw fa-info-circle'),
             ('Contact Me',  'http://minchin.ca/contact/',   'fa fa-fw fa-envelope'),
            )

MENUITEMS_2_AT = 'Blog'
MENUITEMS_2_AT_LINK = ''  # this is added to SITEURL

MENUITEMS_2 = (#('Archives',  SITEURL + '/' + ARCHIVES_URL,  'fa fa-fw fa-archive'),
               ('Labels',    SITEURL + '/' + TAGS_URL,      'fa fa-fw fa-tags'),
              )


DISPLAY_PAGES_ON_MENU = False


# Theme Related
# TYPOGRIFY = False  # breaks the pelican_comment_system, may be fixed in Pelican 3.7
TYPOGRIFY = True
THEME = seafoam.get_path()
SITELOGO = 'images/MinchindotCA-200.png'
SITELOGO_SIZE = '100%'
PYGMENTS_STYLE = 'friendly'
DISPLAY_BREADCRUMBS = True
FAVICON = 'favicon.ico'
BOOTSTRAP_THEME = 'seafoam'
USE_OPEN_GRAPH = True
#CUSTOM_CSS = 'css/minchin-ca.css'
DOCUTIL_CSS = False
CUSTOM_JS_LIST = [
                 ]
# update copyright date automatically
INDEX_COPY_DATE = '2006-{}'.format(str(date.today().year)[-2:])

# list categories here in lowercase
CATEGORY_IMAGES = {'colourettu':            'images/2015/colourettu-logo-4x.png',
                   'seafoam':               'images/2017/seafoam-logo-4x.png',
                   'Minchin dot CA theme':  'images/2016/minchindotca-theme-article.png',
                  }


# Plugins
PLUGIN_PATHS = ('../pelican-plugins',)
PLUGINS = [
            # 'assets',  # unused
            'neighbors',
            'pelican_alias',
            'pelican_comment_system',
            # 'minchin.pelican.plugins.image_process',  # publish only
            # 'minchin.pelican.plugins.cname',  # publish only
            # 'minchin.pelican.plugins.nojekyll',  # publish only
            'minchin.pelican.jinja_filters',
            'minchin.pelican.plugins.summary',
            'minify',  # publish only
            # 'extended_sitemap'  # publish only
            # 'optimize_images',  # publish only
            'minchin.pelican.plugins.post_stats',
          ]

ASSET_CSS = False
ASSET_JS = False
NEIGHBORS = True
PELICAN_COMMENT_SYSTEM = True
PELICAN_COMMENT_SYSTEM_IDENTICON_DATA = ('author', 'email')
PELICAN_COMMENT_SYSTEM_EMAIL_USER = 'minchinweb'
PELICAN_COMMENT_SYSTEM_EMAIL_DOMAIN = 'gmail.com'
PELICAN_COMMENT_SYSTEM_AUTHORS = {
    ('PROTIK KHAN', 'noreply@blogger.com'): "images/authors/rabiul_karim.webp",
    ('Matthew Hartzell', 'noreply@blogger.com'): "images/authors/matthew_hartzell.webp",
    ('Jens-Peter Labus', 'noreply@blogger.com'): "images/authors/jens-peter_labus.png",
    ('Bridget', 'noreply@blogger.com'): "images/authors/bridget.jpg",
    ('melissaclee', 'noreply@blogger.com'): "images/authors/melissa_lee.jpg",
    ('Melissa', 'noreply@blogger.com'): "images/authors/melissa_lee.jpg"
}

IMAGE_PROCESS = {
  'article-feature': ["scale_in 848 848 True"],
  'index-feature': ["scale_in 263 263 True"],
  'example-pict': {'type': 'picture',
                   'sources': [{'name': 'default',
                                'media': '(min-width: 640px)',
                                'srcset': [('640w', ["scale_in 640 480 True"]),
                                           ('1024w', ["scale_in 1024 683 True"]),
                                           ('1600w', ["scale_in 1600 1200 True"]),
                                           ],
                                'sizes': '100vw',
                                },
                               {'name': 'source-1',
                                'srcset': [('1x', ["crop 100 100 200 200"]),
                                           ('2x', ["crop 100 100 300 300"]),
                                           ]
                                }
                               ],
                   'default': ('default', '640w'),
                   },
  '9-col':  {'type': 'picture',
             'sources': [{'name': 'default',
                          'srcset': [('768w', ["scale_in 750 562.5 True"]),    # actually 12 cols (full width) on smallest screens
                                     ('992w', ["scale_in 727.5 545.5 True"]),
                                     ('1200w', ["scale_in 877.5 658 True"]),
                                     ],
                          'sizes': '100vw',
                          },
                         ],
             'default': ('default', '1200w'),
             },
  'index-thumbnail':
            {'type': 'picture',
             'sources': [{'name': 'default',
                          'srcset': [('768w', ["scale_in 187.5 140.5 True"]),  # actually 12 cols (full width) on smallest screens
                          # 157.5
                                     ('992w', ["scale_in 212.5 182 True"]),
                                     ('1200w', ["scale_in 262.5 219.5 True"]),
                                     ],
                          'sizes': '100vw',
                          },
                         ],
             'default': ('default', '1200w'),
             },
}
IMAGE_PROCESS_PARSER = "html5lib"
#IMAGE_PROCESS_FORCE = True  # force reproduction of all images

#SUMMARY_BEGIN_MARKER = '<!-- PELICAN_BEGIN_SUMMARY -->'
#SUMMARY_END_MARKER = '<!-- PELICAN_END_SUMMARY -->'
SUMMARY_USE_FIRST_PARAGRAPH = True
SUMMARY_END_MARKER = '<!-- read more -->'


# `assets` sounds good, but I can't figure out how to get it to work for my CSS
# `better_figures_and_images` didn't seem to do what I wanted (see Projects)
# `gallery` looks good, but don't have a use here yet
# `liquid_tags` & `pelican_comment_system` might be useful...
# `optimize_images` works, but I don't have many images yet
#       - requires `jpegtran.exe` <http://jpegclub.org/jpegtran/> and
#           `optinpng.exe` <http://sourceforge.net/projects/optipng/>
# look into 'neighbors' plugin for profiles


# # Make things disappear
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_SITENAME = True
HIDE_SIDEBAR = True
GITHUB_USER = False
ADDTHIS_PROFILE = False
DISQUS_SITENAME = False
PDF_PROCESSOR = False
# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
#FEED_ATOM = None
#FEED_ALL_ATOM = None
FEED_RSS = None
FEED_ALL_RSS = None
#CATEGORY_FEED_ATOM = None
# CATEGORY_FEED_RSS = None
#AUTHOR_FEED_ATOM = None
AUTHOR_FEED_ATOM = 'feeds/author.%s.atom.xml'
# AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = 'feeds/label.%s.atom.xml'  # not automatically generated
# TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
#FEED_MAX_ITEMS = 0


## Testing
# PATH = 'content-2'
#PLUGINS.append("minification")  # currently eats too many spaces
#                                 try pelican-diminuendo
#                                 try pelican-minify / minify
#PLUGINS.append('pelican_diminuendo')
#DISPLAY_PAGES_ON_MENU = True


# add markdown extras, smart symbols -- https://facelessuser.github.io/pymdown-extensions/extensions/smartsymbols/
