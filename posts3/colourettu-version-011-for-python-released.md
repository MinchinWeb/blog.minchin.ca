Title: Colourettu version 0.1.1 for Python released
Date: 2015-08-15 21:26
Author: Minchin Web (noreply@blogger.com)
Tags: Colourettu, Python, releases
Slug: colourettu-version-011-for-python-released

Version 0.1.1 of *Colourettu* has been released.\

\

Colourettu is a Python library I've written for dealing with colours,
and specifically to determine the contrast between two colours.\

\

A quick example:

<div>

\
</p>
    import colourettuc1 = colourettu.colour()                # defaults to #FFFc2 = colourettu.colour("#eee")          # equivalent to #EEEEEEc3 = colourettu.colour("#456bda")c4 = colourettu.colour([3, 56, 129])    # as an RGB tuple or listc5 = colourettu.colour((63, 199, 233))>>> colourettu.contrast("#FFF", "#FFF") # white on white1.0>>> colourettu.contrast(c1, "#000")     # black on white20.999999999999996>>> colourettu.contrast(c4, c5)4.363552233203198

\
</p>
\

The easiest to install *Colourett* (assuming you already have Python
installed) is to use *pip*:\

`pip install colourettu`\

<p>
\
This is the first release of this library. [The code for
*Colourettu*](https://github.com/MinchinWeb/colourettu/) is hosted on
Github.

</div>

<div class="feedflare">

</p>
[![](http://feeds.feedburner.com/~ff/MinchinWeb?i=UFZXZM-l6H8:dWrd99_grK4:XhI0_UKdTUU)](http://feeds.feedburner.com/~ff/MinchinWeb?a=UFZXZM-l6H8:dWrd99_grK4:XhI0_UKdTUU)
[![](http://feeds.feedburner.com/~ff/MinchinWeb?i=UFZXZM-l6H8:dWrd99_grK4:4cEx4HpKnUU)](http://feeds.feedburner.com/~ff/MinchinWeb?a=UFZXZM-l6H8:dWrd99_grK4:4cEx4HpKnUU)
[![](http://feeds.feedburner.com/~ff/MinchinWeb?d=yIl2AUoC8zA)](http://feeds.feedburner.com/~ff/MinchinWeb?a=UFZXZM-l6H8:dWrd99_grK4:yIl2AUoC8zA)

<p>

</div>

![](http://feeds.feedburner.com/~r/MinchinWeb/~4/UFZXZM-l6H8)

</p>

