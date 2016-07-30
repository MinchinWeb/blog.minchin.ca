Title: Colourettu 0.1.1 for Python released
Date: 2014-12-11 17:20
Modified: 2015-08-15 14:26
Author: Wm. Minchin
Tags: Colourettu, Python, releases
Category: Colourettu
Slug: colourettu-version-011-for-python-released

Version 0.1.1 of *Colourettu* has been released.

Colourettu is a Python library I've written for dealing with colours,
and specifically to determine the contrast between two colours.

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

The easiest to install *Colourettu* (assuming you already have Python
installed) is to use *pip*:

    pip install colourettu

This is the first release of this library. [The code for
*Colourettu*](https://github.com/MinchinWeb/colourettu/) is hosted on
Github.
