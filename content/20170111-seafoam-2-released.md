Title: Seafoam 2.0.4 Pelican Theme Released
Date: 2017-01-11 13:33T+0700
Author: Wm. Minchin
Tags: Seafoam, Python, Releases, Pelican Themes
Category: Seafoam

Version 2.0.4 of *Seafoam* has been released.

Seafoam is the Pelican theme I use for this site, but published to PyPI in the
hope that it will be useful to others.

This release changes the name of the project to *seafoam* from the unwieldy
*[minchin.pelican.themes.minchindotca]({filename}20160912-minchin-dot-ca-pelican-theme-version-110-released.md)*.
It also add support for the [Pelican Comment
System](https://bernhard.scheirle.de/posts/2014/March/29/static-comments-via-email/),
removes the need to define Jinja2 filters in your configuration file, updates
to Font Awesome v4.7, and several design fixes as well. Code is updated to
work with Pelican v3.7 and Jinja v2.9.

<!-- read more -->

## Quickstart

To use this theme, first install it via `pip`: (as a side, this is the only
Pelican theme I know of that is installable from PyPI.)

    pip install seafoam

Next, update your `pelicanconf.py` to use the theme, with its default settings:

    import seafoam

    THEME = seafoam.get_path()
    BOOTSTRAP_THEME = 'seafoam'

    PLUGINS = ['minchin.pelican.jinja_filters',
               'minchin.pelican.plugins.image_process',
               # others, as desired...
               ]

    IMAGE_PROCESS = {
      'article-feature': ["scale_in 848 848 True"],
      'index-feature': ["scale_in 263 263 True"],
    }

And then regenerate your site.

The theme depends on the pathlib library, that was introduced in Python 3.4, so
the theme won't work on earlier versions of Python. Installing the pathlib2
library should provide the necessary functionality for the theme to work, but
this is currently untested by me.

## Settings

The full settings are not particularly well documented (by me anyway), although
the the
[ReadMe](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3)
for the base theme goes over most of the settings.

## Changelog {#changelog}

I've built a release script that automates pushing releases to PyPI, and so it
makes it very easy to make a release. In fact, writing these release blog posts
is probably the most involved part of cutting a release! Therefore, this blog
post is to serve for five releases: 2.0.0, 2.0.1, 2.0.2, 2.0.3, and 2.0.4:

### Version 2.0.0 -- January 9, 2017

- *BREAKING*: rename from `minchin.pelican.themes.minchindotca`
  to `seafoam`
- *feature*: add support for Pelican Blog System
- *feature*: add Seafoam logo
- *feature*: switch to `minchin.pelican.jinja_filters` to provide
  the required Jinja filters, rather than requiring them to be manually
  added to the user's configuration file
- *feature*: upgrade to FontAwesome 4.7.0
- *feature*: upgrade to jQuery 3.1.0
- *feature*: add support for reading time via
  [post stats](https://github.com/getpelican/pelican-plugins/tree/master/post_stats)
  plugin
- *feature*: add support for [pelican comment
  system](https://github.com/getpelican/pelican-plugins/tree/master/pelican_comment_system)
- *bug*: restyle comments with bootstrap's `media` class (much cleaner template
  code) (see [issue 6](https://github.com/MinchinWeb/seafoam/issues/6))
- *bug*: switch template variable from `PAGES` to `pages` to support Pelican
  v3.7 (see [issue 5](https://github.com/MinchinWeb/seafoam/issues/5))
- *bug*: don't print section for next and previous posts in a category if the
  article is the only one in that category

### Version 2.0.1 -- January 10, 2017

- *bug*: pluralization of "1 comment" now correct (see [issue
  8](https://github.com/MinchinWeb/seafoam/issues/8))
- *bug*: fix pagination code to work with Jinja2 v2.9.0 (see [issue
  9](https://github.com/MinchinWeb/seafoam/issues/9))

### Version 2.0.2 -- January 11, 2017

- *bug*: fix link color on panel-primary
- *bug*: improve layout of generated HTML

### Version 2.0.3 -- January 11, 2017

- *bug*: fix link color in body area of panel-primary (fixes regression
  from version 2.0.2)

### Version 2.0.4 -- January 11, 2017

- *bug*: fix archive page template code to work with Jinja2 v2.9.0 (see [issue
  10](https://github.com/MinchinWeb/seafoam/issues/10))
