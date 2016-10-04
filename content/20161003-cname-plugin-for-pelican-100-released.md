title: CName Pelican Plugin 1.0.0 Released
date: 2016-10-03 20:39
tags: pelican, pelican plugins, releases, python
Category: Pelican Plugins

**CName** is a plugin for [Pelican](http://docs.getpelican.com/),
a static site generator written in Python.

**CName** creates a *CNAME* file in the root of your output directory. This
is useful when you are publishing your site to
[GitHub Pages](https://pages.github.com/) on a
[custom domain](https://help.github.com/articles/using-a-custom-domain-with-github-pages/).

<!-- read more -->

## Installation

The easiest way to install **CName** is through the use of pip. This
will also install the required dependencies automatically.

~~~~sh
  pip install minchin.pelican.plugins.cname
~~~~

Then, in your `pelicanconf.py` file, add **CName** to your list of
plugins:

~~~python
  PLUGINS = [
              # ...
              'minchin.pelican.plugins.cname',
              # ...
            ]
~~~

And that's it! No further configuration is needed.


## Usage

No configuration is needed. The value places in the *CNAME* files is based
on your SITEURL` setting.


## Known Issues

As the plugin makes use of the `SITEURL` plugin, if you are using both
a `pelicanconf.py` and a `publishconf.py` settings file, **CName** will
likely generate different results for when you are testing your site locally
and when you push it to production.


## Credits

I can't claim I came up with the original idea. It is based on the
[original code](https://github.com/getpelican/pelican-plugins/pull/566)
by [Dmitriy Kalinin](http://lazycoder.ru/), that has languished as an
open pull request in the `pelican-plugins` repo for the last year.


## Code

The code for this project is available on [GitHub](https://github.com/MinchinWeb/minchin.pelican.plugins.cname). Contributions are welcome!
