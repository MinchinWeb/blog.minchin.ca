Title: Colourettu 1.1.0 for Python released
Date: 2015-07-20 9:25
Modified: 2015-08-15 14:23
Author: Wm. Minchin
Tags: Colourettu, Python, releases
Category: Colourettu
Alias: 2015/07/colourettu-version-11-for-python.html
Slug: colourettu-1-1-0-for-python

Version 1.1.0 of *Colourettu* has been released.

Colourettu is a Python library I've written for dealing with colours and
"palettes" (groups of colours).

A quick example:

    import colourettu
    c1 = colourettu.colour()                # defaults to #FFF
    c2 = colourettu.colour("#eee")          # equivalent to #EEEEEE
    c3 = colourettu.colour("#456bda")
    c4 = colourettu.colour([3, 56, 129])    # as an RGB tuple or list
    c5 = colourettu.colour((63, 199, 233))
    c6 = colourettu.colour([0.242, 0.434, 0.165], normalized_rgb=True)
    all_colours = [c1, c2, c3, c4, c5, c6]
    p2 = colourettu.palette()
    p2.from_list(all_colours)
    p2.to_image('p2.png', max_width=360, vertical=False)

<div markdown=1 class="text-center">
![Colourettu p2]({filename}images/2015/p2.png)
</div>

The easiest to install (or upgrade) *Colourettu* (assuming you already
have Python installed) is to use *pip*:

    pip install colourettu --upgrade

The changes for this version include a project logo (above), and the
addition of the *palette* class.

[*Colourettu* documentation](http://minchin.ca/colourettu/) is now
online. A [full changelog](http://minchin.ca/colourettu/changelog.html)
is online as part of that. [The code for
*Colourettu*](https://github.com/MinchinWeb/colourettu/) is hosted on
Github.
