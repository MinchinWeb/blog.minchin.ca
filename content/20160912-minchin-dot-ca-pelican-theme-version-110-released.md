title: Minchin dot CA Pelican Theme 1.1.0 Released
date: 2016-09-12 19:29
tags: pelican, pelican themes, releases, python
Category: Minchin dot CA theme


This update was the final touches needed to make my site go live.

I've been in the process of redesigning my blog and so as part of that I've
tried to make as many pieces as possible installable from `pip`. To that end,
I've packaged my website theme and uploaded it to PyPI.

The theme is based on [Daan Debie](http://dandydev.net/)'s wonderful [Bootstrap
3
theme](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3),
although heavily modified. Because of the heavy modifications, I'm not sure how
useful this will be to others, but I think it is still a useful
proof-of-concept as I am aware of no other Pelican themes available on PyPI.

To use this theme, first install it via `pip`:

    pip install minchin.pelican.themes.minchindotca

Next, update your `pelicanconf.py` to use the theme, with its default settings:

    from minchin.pelican.themes import minchindotca

    THEME = minchindotca.get_path()
    BOOTSTRAP_THEME = 'minchindotca'

    IMAGE_PROCESS = {
      'article-feature': ["scale_in 848 848 True"],
      'index-feature': ["scale_in 263 263 True"],
    }

    # Jijna2 filters
    def datetimefilter(value, format='%Y/%m/%d %H:%M'):
        """convert a datetime to a different format."""
        return value.strftime(format)


    def article_date(value):
        """Converts a date to the format we want it displayed on the article
           template.
        """
        return value.strftime('%A, %B %-d, %Y')


    def breaking_spaces(value):
        """Converts non-breaking spaces to regular spaces."""
        return value.replace('\u00A0', ' ')


    JINJA_FILTERS = {
      'datetimefilter': datetimefilter,
      'article_date':   article_date,
      'breaking_spaces': breaking_spaces,
    }

And then regenerate your site.

The theme depends on the pathlib library, that was introduced in Python 3.4, so
the theme won't work on earlier versions of Python. Installing the pathlib2
library should provide the necessary functionality for the theme to work, but
this is currently untested by me.

The full settings are not particularly well documented (by me anyway), although
the the
[ReadMe](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3)
for the base theme goes over most of the settings.

For future updates, I would like to simplify the adding the required settings,
move the Jinja filters to their own package, work on the documentation of all
the various settings, and add a proper changelog.
