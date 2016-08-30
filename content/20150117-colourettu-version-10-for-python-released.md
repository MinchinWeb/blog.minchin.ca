Title: Colourettu 1.0.0 for Python released
Date: 2015-01-17 9:21
Modified: 2015-08-15 14:25
Author: Wm. Minchin
Tags: Colourettu, Python, releases
Category: Colourettu
Alias: 2015/01/colourettu-version-10-for-python.html
Slug: colourettu-1-0-0-for-python

Version 1.0.0 of *Colourettu* has been released.

Colourettu is a Python library I've written for dealing with colours,
and specifically to determine the contrast between two colours.

<!-- read more -->

A quick example:

    import colourettu
    c1 = colourettu.colour()                # defaults to #FFF
    c2 = colourettu.colour("#eee")          # equivalent to #EEEEEE
    c3 = colourettu.colour("#456bda")
    c4 = colourettu.colour([3, 56, 129])    # as an RGB tuple or list
    c5 = colourettu.colour((63, 199, 233))

    >>> colourettu.contrast("#FFF", "#FFF") # white on white
    1.0
    >>> colourettu.contrast(c1, "#000")     # black on white
    20.999999999999996
    >>> colourettu.contrast(c4, c5)
    4.363552233203198

The easiest to install (or upgrade) *Colourettu* (assuming you already
have Python installed) is to use *pip*:

    pip install colourettu --upgrade

The biggest change with this release is that [*Colourettu*
documentation](http://minchin.ca/colourettu/) is now online. A [full
changelog](http://minchin.ca/colourettu/changelog.html) is online as
part of that. [The code for
*Colourettu*](https://github.com/MinchinWeb/colourettu/) is hosted on
Github.
