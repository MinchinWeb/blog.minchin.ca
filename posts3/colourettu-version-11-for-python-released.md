Title: Colourettu version 1.1 for Python released
Date: 2015-08-15 21:23
Author: Minchin Web (noreply@blogger.com)
Tags: Colourettu, Python, releases
Slug: colourettu-version-11-for-python-released

<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-6kZnhjuzaP8/Vc4IvTn6GcI/AAAAAAAAEq8/BYlb5PNolzc/s1600/colourettu-logo-4x.png)](http://2.bp.blogspot.com/-6kZnhjuzaP8/Vc4IvTn6GcI/AAAAAAAAEq8/BYlb5PNolzc/s1600/colourettu-logo-4x.png)

</div>

\

</p>
Version 1.1.0 of *Colourettu* has been released.\

\

Colourettu is a Python library I've written for dealing with colours and
"palettes" (groups of colours).\

\

A quick example:

<div>

\
</p>
    import colourettuc1 = colourettu.colour()                # defaults to #FFFc2 = colourettu.colour("#eee")          # equivalent to #EEEEEEc3 = colourettu.colour("#456bda")c4 = colourettu.colour([3, 56, 129])    # as an RGB tuple or listc5 = colourettu.colour((63, 199, 233))c6 = colourettu.colour([0.242, 0.434, 0.165], normalized_rgb=True)all_colours = [c1, c2, c3, c4, c5, c6]p2 = colourettu.palette()p2.from_list(all_colours)p2.to_image('p2.png', max_width=360, vertical=False)

\
</p>
<div class="separator" style="clear: both; text-align: center;">

[![](http://2.bp.blogspot.com/-l6idW-GHcq4/Vc4JgMlj7RI/AAAAAAAAErE/KNCiLvCdSpk/s1600/p2.png)](http://2.bp.blogspot.com/-l6idW-GHcq4/Vc4JgMlj7RI/AAAAAAAAErE/KNCiLvCdSpk/s1600/p2.png)

</div>

</p>
\

The easiest to install (or upgrade) *Colourettu* (assuming you already
have Python installed) is to use *pip*:\

`pip install colourettu --upgrade`\

\

The changes for this version include a project logo (above), and the
addition of the *palette* class.\

\

<p>
[*Colourettu* documentation](http://minchin.ca/colourettu/) is now
online. A [full changelog](http://minchin.ca/colourettu/changelog.html)
is online as part of that. [The code for
*Colourettu*](https://github.com/MinchinWeb/colourettu/) is hosted on
Github.

</div>

<div class="feedflare">

</p>
[![](http://feeds.feedburner.com/~ff/MinchinWeb?i=nTa_IZI_EJA:Wd2u_n6wEQk:XhI0_UKdTUU)](http://feeds.feedburner.com/~ff/MinchinWeb?a=nTa_IZI_EJA:Wd2u_n6wEQk:XhI0_UKdTUU)
[![](http://feeds.feedburner.com/~ff/MinchinWeb?i=nTa_IZI_EJA:Wd2u_n6wEQk:4cEx4HpKnUU)](http://feeds.feedburner.com/~ff/MinchinWeb?a=nTa_IZI_EJA:Wd2u_n6wEQk:4cEx4HpKnUU)
[![](http://feeds.feedburner.com/~ff/MinchinWeb?d=yIl2AUoC8zA)](http://feeds.feedburner.com/~ff/MinchinWeb?a=nTa_IZI_EJA:Wd2u_n6wEQk:yIl2AUoC8zA)

<p>

</div>

![](http://feeds.feedburner.com/~r/MinchinWeb/~4/nTa_IZI_EJA)

</p>

