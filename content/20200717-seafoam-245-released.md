title: Seafoam 2.4.5 Released
date: 2020-07-17 20:54
Modified: 2020-07-18 11:41
Author: Wm. Minchin
Tags: Seafoam, Python, Releases
Category: Seafoam

It's time for a new update to *Seafoam*, the website theme currently in use
here (on my Blog) and by my wider site.

In reviewing my blog, I realized it's been many versions and a couple of years
since I did a post about a *Seafoam* release. In the background, I've continued
to make small improvements. I also use the project for private, personal
projects, so some of the improvements are centered on those. What drove this
particular release was that something has happened that broke my fonts.
Previously, they were hosted directly on Google Fonts, but they seem to have
stopped loading, so with this release they are "internal" to the theme.

As well, [minchin.releaser](https://github.com/MinchinWeb/minchin.releaser/)
has made putting out a release very simple, to the point where a blog post
about the release in question can be the hardest part of the whole process (and
so they often just never happen...). You'll notice in the changelog below it's
not uncommon to see multiple releases the same day.

A final thing I noticed was lacking from the project readme was any sort of
sample images. This is hope will prove simple and easy to fix.

## Fallback fonts (i.e. "broken")

![fallback fonts]({filename}images/2020/broken_fonts.png)

## Working fonts

![workingfonts]({filename}images/2020/working_fonts.png)

## Future Plans {#future-plans}

This theme is based on [Bootstrap 3](https://getbootstrap.com/docs/3.3/). About
a year ago, I'd started an effort to move to Bootstrap 4. Turns out that
transition is a bit of a pain, and I never did finish it to my liking. Now
Bootstrap 5 (at least [the first alphas
build](https://blog.getbootstrap.com/2020/06/16/bootstrap-5-alpha/)) have been
released, so I'll probably just skip 4 if I ever do that update. A big issue on
updating Bootstrap, at least for me, is that they changed their preferred CSS
processor from LESS to SASS: Bootstrap 3 supported both, while version 4 is
SASS only. All my modifications had been done in LESS, so that provided a large
effort to "translate".

## Upgrading

Upgrading *should* is straight forward. I haven't broken anything on purpose
since v2.0.0 came out.

To install or to upgrade, you can use pip:

```sh
pip install seafoam --upgrade
```

## Update: July 18, 2020

New day, new update! Version 2.4.6 adds a few non-breaking spaces to improve
the flow of the acticle details on the article index page.

## Changelog {#changelog}

See my [previous post]({filename}20170111-seafoam-2-released.md#changelog) for earlier
changelog entries.

### Version 2.1.0 -- February 20, 2017

- *feature*: add support for the
  [readtime](https://pypi.python.org/pypi/pelican-readtime) plugin in
  preference to the *post-stats* plugin to get article reading time. The
  former is available on PyPI (as *pelican-readtime*), while the latter is
  not.
- *support*: document optionally supported plugins (see [issue
  2](https://github.com/MinchinWeb/seafoam/issues/2).)

### Version 2.1.1 -- March 8, 2017

- *bug*: fix pagination links on category and tag pages. See [issue
  6](https://github.com/MinchinWeb/seafoam/issues/6).
- *bug*: remove unused code in pagination template. Thanks
  [@jorgesumle](https://github.com/jorgesumle)! (see [issue
  13](https://github.com/MinchinWeb/seafoam/issues/13).)

### Version 2.1.2 -- March 8, 2017

- *bug*: provide universal wheels. On versions of Python before 3.4 (when the
  *pathlib* module was added to the standard library), we now depend on
  [pathlib2](https://pypi.python.org/pypi/pathlib2).
- *bug*: provide an absolute path.

### Version 2.1.3 -- April 19, 2017

- *support*: document most theme options (see [issue
  2](https://github.com/MinchinWeb/seafoam/issues/2)).

### Version 2.1.4 -- April 9, 2017

- *suupport*: [Framework :: Pelican ::
  Themes](https://pypi.org/search/?c=Framework+%3A%3A+Pelican+%3A%3A+Themes)
  trove classifier on PyPI now available.

### Version 2.1.5 -- May 31, 2017

- *bug*: indent definition list items (see [issue
  11](https://github.com/MinchinWeb/seafoam/issues/11)).
- *bug*: note that *Image Processing* v1.1.2 is broken (see their
  [issue
  2](https://github.com/MinchinWeb/minchin.pelican.plugins.image_process/issues/2)).
  Use a different version of that plugin.

### Version 2.2.0 -- November 13, 2017

- *feature*: include [prjct](https://github.com/MinchinWeb/prjct) template.
- *feature*: include 404 template (see [issue
  15](https://github.com/MinchinWeb/seafoam/issues/15)).
- *feature*: use `NAVBAR_ON_TOP` to move the menu from the left side of the
  page to the top (the Bootstrap default).
- *bug*: respect Pelican's `THEME_STATIC_DIR` setting.
- *support*: use
  [minchin.releaser](https://github.com/MinchinWeb/minchin.releaser/) to put
  out releases.

### Version 2.2.1 -- November 13, 2017

- *bug*: fix reference to *python-dateutil* in project metadata.

### Version 2.3.0 -- November 29, 2017

- *feature*: add basic support for Tuque Search plugin.
- *feature*: added support for [prjct](https://github.com/MinchinWeb/prjct).
- *bug*: fix issues with navbar coloring, navbar brand text + logo
  layout, and sidebar alinement.

### Version 2.3.1 -- November 30, 2017

- *bug*: fix styling of breadcrumbs on article pages.
- *bug*: fix styling of pager on search results.

### Version 2.3.2 -- December 8, 2017

- *bug*: fix styling of main text body when using vertical menu.

### Version 2.3.3 -- January 18, 2018

- *bug*: make *Archives* link work better with vertical menu and with
  sub-sites.

### Version 2.3.4 -- January 18, 2018

- *bug*: Add instructions on how to use the *404 Error* page.

### Version 2.4.0 -- February 3, 2018

- *feature*: various CSS additions to support
  [Gigatrees](https://gigatrees.appspot.com/) 4.4.1 (genealogy site generator).
- *support*: upgrade to *respond.js* v1.4.2.
- *feature*: add ability to add Javascript to `<head>` with
  `CUSTOM_JS_LIST_HEAD`, which is designed to work very similar to
  `CUSTOM_JS_LIST`.
- *feature*: add `JQUERY_JS_IN_HEAD` to move loading JQuery from the end of
  the page to the head section.
- *feature*: support local and absolute URLs for `CUSTOM_CSS_LIST` and
  `CUSTOM_JS_LIST`, and scripts directly for `CUSTOM_JS_LIST`.
- *bug*: Make the output HTML a little cleaner.
- *support*: edit some JS and CSS links to explicitly note the version of the
  library being loaded. This should make both cache-ing and library upgrading a
  little simpler.

### Version 2.4.1 -- October 25, 2018

- *bug*: adjust 404 page text.

### Version 2.4.2 -- September 2, 2019

- *bug*: limit width of images on index pages to 100%.

### Version 2.4.3 -- September 2, 2019

- *bug*: upgrade Tipue Search to version 7.1, and update templates to match.

### Version 2.4.4 -- June 26, 2020

- *bug*: use local version of fonts. (see [issue
  16](https://github.com/MinchinWeb/seafoam/issues/16).)

### Version 2.4.5 -- July 16, 2020

- *bug*: have bullet points list separators go to the next line.
- *bug*: only display comment count if there are comments.

### Version 2.4.6 -- July 18, 2020

- *bug*: add a new non-breaking spaces to help flow of article details on blog
  index.
