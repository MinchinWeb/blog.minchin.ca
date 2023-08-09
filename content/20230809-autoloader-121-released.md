title: AutoLoader Plugin 1.2.1 for Pelican Released
date: 2023-08-09 15:49 -0600
tags: Pelican, Pelican Plugins, Releases, Python, Autoloader, CName, NoJekyll, Optimize Images, Post Stats, Static Comments, Summary (Pelican)
Category: Pelican Plugins

*AutoLoader* is a plugin for [Pelican](http://docs.getpelican.com/),
a static site generator written in Python.

*AutoLoader* is a "meta plugin" in that it doesn't directly affect your Pelican
site, but rather works to make your other plugins better.

<!-- PELICAN_BEGIN_SUMMARY -->
This release of *Autoloader* is to fix a crashing bug when no plugins in the
`minchin.pelican.readers` namespace are loaded.

I also updated a number of other plugins to blacklist v1.2.0 to avoid these
crashes.
<!-- read more -->

This actually came about because someone emailed me a bug report. So if you
have issues, please feel free to reach out.

## Upgrading

The simplest way to upgrade (and install) *AutoLoader* is to use `pip`:

~~~sh
pip install minchin.pelican.plugins.autoloader --upgrade
~~~

## Configuration

There are no configuration changes needed.

## This Release

This release is v1.2.1, released August 9, 2023.

- **bug**: don't break if no plugins exist in the namespace you are trying to
  load from.

## Other Links

- [all release posts]({tag}autoloader) for *autoloader*
- code, including full configuration directions, on GitHub at
  [MinchinWeb/minchin.pelican.plugins.autoloader](https://github.com/MinchinWeb/minchin.pelican.plugins.autoloader)
- [full
  changelog](https://github.com/MinchinWeb/minchin.pelican.plugins.autoloader/blob/master/CHANGELOG.rst)

---

## Other Plugins Updated

These plugins were updated to blacklist the previous version of *Autoloader*
(v1.2.0), and to add autoloading support if it wasn't previously in place.

- [minchin.pelican.plugins.cname](https://github.com/MinchinWeb/minchin.pelican.plugins.cname)
  v1.3.4
    - release version numbers 1.3.0 through 1.3.3 actually got "eaten" in
      making the release process work as expected, and so don't represent
      "proper" releases.
- [minchin.pelican.plugins.nojekyll](https://github.com/pelican-plugins/nojekyll)
  v1.2.0
    - this plugin is actually hosted by the
      [Pelican-Plugin](https://github.com/pelican-plugins) organization, but
      remains maintained by me for the time being.
- [minchin.pelican.plugins.optimize_images](https://github.com/MinchinWeb/minchin.pelican.plugins.optimize_images) v1.2.2
- [minchin.pelican.plugins.post_stats](https://github.com/MinchinWeb/minchin.pelican.plugins.post_stats) v1.2.0
- [minchin.pelican.plugins.static_comments](https://github.com/MinchinWeb/minchin.pelican.plugins.static_comments) v2.1.2
- [minchin.pelican.plugins.summary](https://github.com/MinchinWeb/minchin.pelican.plugins.summary) v1.2.1
