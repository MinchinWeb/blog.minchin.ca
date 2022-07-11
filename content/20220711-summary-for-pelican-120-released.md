title: Summary Plugin 1.2.0 for Pelican Released
date: 2022-07-11 22:12 +0200
tags: Pelican, Pelican Plugins, Releases, Python, Summary (Pelican)
Category: Pelican Plugins

**Summary** is a plugin for [Pelican](http://docs.getpelican.com/), a static
site generator written in Python.

**Summary** allows easy, variable length summaries directly embedded within the
body of your articles.

## This Release

<!-- PELICAN_BEGIN_SUMMARY -->
This release, version 1.2.0, makes a few fixes to allow the plugin to support
Pelican 4 and also supports my
[autoloader](http://localhost:8000/label/autoloader/).
<!-- read more -->

## Upgrading

To upgrade, simply use `pip`:

~~~sh
pip install minchin.pelican.plugins.summary --upgrade
~~~

The autoloader plugin should be automatically installed.

If you are using Pelican 4.5+, the plugin will automatally be loaded.

If you are an earlier version of Pelican, or non-namespace plugins, you will
need to add the auto-loader to your list of plugins (and no longer need to list
the summary plugin):

~~~python
# pelicanconf.py

PLUGINS = [
    # others
    "minchin.pelican.plugins.autoloader",
    # summary plugin no longer needs to be listed
]
~~~

## Credits

Thanks to [Henry Swainson](https://github.com/HenrySwanson) for the [pull
request](https://github.com/MinchinWeb/minchin.pelican.plugins.summary/pull/1)
that forms the basis of most of this release!

## Personal Note

With this, I'm finally able to upgrade to Pelican 4! It's been a long time
coming...
