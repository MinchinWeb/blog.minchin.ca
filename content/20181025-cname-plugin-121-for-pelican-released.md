title: CName Plugin 1.2.1 for Pelican Released
date: 2018-10-25 20:37
tags: pelican, pelican plugins, releases, python
Category: Pelican Plugins

**CName** is a plugin for [Pelican](http://docs.getpelican.com/),
a static site generator written in Python.

**CName** creates a *CNAME* file in the root of your output directory. This
is useful when you are publishing your site to
[GitHub Pages](https://pages.github.com/) on a
[custom domain](https://help.github.com/articles/using-a-custom-domain-with-github-pages/).

## Updates

<!-- PELICAN_BEGIN_SUMMARY -->

Writing these posts about the new releases is often a little funny becuase the
changes made are often so small that they don't really feel worthy of their own
post, but collectively, they start adding up. So this post actually covers five
releases combined: 1.0.3, 1.0.4, 1.1.0, 1.2.0, 1.2.1.

<!-- read more -->

- **v1.0.3** was updated to include the [Framework :: Pelican ::
  Plugins](https://pypi.org/search/?c=Framework+%3A%3A+Pelican+%3A%3A+Plugins)
  classifier that had been added to PyPI. Sadly, there hasn't been much uptake
  of the classifer: I have 6 of the 7 packages listed. But maybe I should be so
  surprised: Pelican plugins have traditionally been distributed via a large
  [shared repository](https://github.com/getpelican/pelican-plugins) rather
  than via PyPI.
- **v1.0.4** was released to make sure the license file was included in the
  distrubtion uploaded to PyPI.
- **v1.1.0** was me reworking the release process to be based on my
  *[minchin.releaser](https://github.com/MinchinWeb/minchin.releaser)*. I was
  already using an earlier version of the scripts, but I find it helpful to
  have my release process stardardized and semi-automated. This in turn is part
  of the reason there have so many small releases: it's easy to do. So easy,
  that these last three releases were all pushed out today!
- **v1.2.0** added support for protocol-less `SITEURL` settings. I've been in
  the process (for some time now) of moving my site to HTTPS. However,
  sometimes a site will be available on both HTTP and HTTPS, and so to serve
  the same files, you can specify links without a protocol using just the
  double slashes: i.e. `SITEURL = "//minchin.ca"`. Because of this, the main
  part of my site (<https://minchin.ca>) is now available on both HTTP and
  HTTPS.
- **v1.2.1** limits some of the internal text replacements to try and avoid
  future bugs.

You should be able to update through pip without any issues

~~~~sh
pip install --upgrade minchin.pelican.plugins.cname
~~~~

The code for this project is available on
[GitHub](https://github.com/MinchinWeb/minchin.pelican.plugins.cname).
Contributions are welcome!
