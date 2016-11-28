Title: Colourettu 2.0.0 for Python released
Date: 2015-08-28 15:55
Author: Wm. Minchin
Tags: Colourettu, Python, releases
Category: Colourettu

Version 2.0.0 of *Colourettu* has been released.

Colourettu is a Python library I've written for dealing with colours and
"palettes" (groups of colours).

<!-- read more -->

A quick example:

    from colourettu import Colour, Palette

    p1 = Palette()
    p1.blend()
    p1.to_image('p1_blended.png', 60, vertical=False)

<div markdown=1 class="text-center">
![Colourettu p1 Blended]({filename}images/2016/p1_blended.png)
</div>

    c1 = Colour('#fff')
    c2 = Colour('#7e1e9c')
    p3 = Palette(c1, c3)
    p3.blend(cycles=5)
    p3.to_image('p3.png', max_width=360, vertical=False)

<div markdown=1 class="text-center">
![Colourettu p3]({filename}images/2016/p3.png)
</div>

The easiest to install (or upgrade) *Colourettu* (assuming you already
have Python installed) is to use *pip*:

    pip install colourettu --upgrade

Additions for this version include the *blend* functionality, both as a stand-alone function and as a Palette method.

Breaking changes in this version are the fact that the *Colour* and *Palette* class have been renamed to the CapWords capitialization.

Other changes include:

- the tests are now included by default at the *colourettu.test* namespace. This allows the tests to be run on a system with Colourettu installed by running `green colourettu.test`
- updated documentation build system
- better documentation
- fix bug where using the *max_width* parameter with `Palette.to_image()` would result ina  black strip on the bottom/left of the generated image.

[*Colourettu* documentation](http://minchin.ca/colourettu/) is now
online. A [full changelog](http://minchin.ca/colourettu/changelog.html)
is online as part of that. [The code for
*Colourettu*](https://github.com/MinchinWeb/colourettu/) is hosted on
Github.
