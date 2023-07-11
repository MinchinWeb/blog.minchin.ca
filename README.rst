===============
Blog.Minchin.ca
===============

This is the source code for my blog, hosted at `blog.minchin.ca
<https://blog.minchin.ca>`_

It is a static site, generated via Pelican.

Notes to Self
=============

To update requirements::

    pip-compile --update

To update the (local) virtual environment::

    pip-sync

(Note that ``pip-sync`` can't update itself on Windows.)

To generate a "filename" for comments::

    random.randint(1 10**19-1)
