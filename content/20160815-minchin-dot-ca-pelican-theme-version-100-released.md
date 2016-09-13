title: Minchin dot CA Pelican Theme 1.0.0 Released
date: 2016-08-15 11:19
stared: False
tags: pelican, pelican themes, releases, python
Category: Minchin dot CA theme
uuid: F1B13C708C91438AAA5C7D0C844BAED0
creator:
    device agent: iPad/iPad5,2
    generation date: 2016-08-15 17:19:49
    host name: William’s iPad
    os agent: iOS/9.3.4
    software agent: Day One iOS/1.17.9

I've been in the process of redesigning my blog and so as part of that I've tried to make as many pieces as possible installable from `pip`. To that end, I've packaged my website theme and uploaded it to PyPI.

The theme is based on [Daan Debie](http://dandydev.net/)'s wonderful [Bootstrap 3 theme](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3), although heavily modified. Because of the heavy modifications, I'm not sure how useful this will be to others, but I think it is still a useful proof-of-concept as I am aware of no other Pelican themes available on PyPI.

To use this theme, first install it via `pip`:

    pip install minchin.pelican.themes.minchindotca

Next, update your `pelicanconf.py` to use the theme, with its default settings:

    from minchin.pelican.themes import minchindotca

    THEME = minchindotca.get_path()
    BOOTSTRAP_THEME = 'minchindotca'

And then regenerate your site.

The theme depends on the pathlib library, that was introduced in Python 3.4, so the theme won't work on earlier versions of Python. Installing the pathlib2 library should provide the necessary functionality for the theme to work, but this is currently untested by me.

The full settings are not particularly well documented (by me anyway), although the the [ReadMe](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) for the base theme goes over most of the settings.
