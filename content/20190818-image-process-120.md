title: Image Process Plugin 1.2.0 for Pelican Released
date: 2019-08-18 17:13
tags: pelican, pelican plugins, releases, python
Category: Pelican Plugins

*Image Process* is a plugin for [Pelican](http://docs.getpelican.com/),
a static site generator written in Python.

*Image Process* let you automate the processing of images based on their
class attribute. Use this plugin to minimize the overall page weight and
to save you a trip to Gimp or Photoshop each time you include an image
in your post.

*Image Process* is used by
[this blog's theme](https://github.com/MinchinWeb/seafoam) to resize the source
images so they are the correct size for thumbnails on the main index page and
the larger size they are displayed at on top of the articles.

## This Release

<!-- PELICAN_BEGIN_SUMMARY -->

Version 1.2.0 of the plugin has been released and
posted [PyPI](https://pypi.org/project/minchin.pelican.plugins.image-process/).

The biggest change this version brings is support for Pelican version 4. Thanks
to Nick Perkins for [reporting the
issue](https://github.com/MinchinWeb/minchin.pelican.plugins.image_process/issues/5),
and to Therry van Neerven for providing a [Pull
Request](https://github.com/whiskyechobravo/image_process/pull/19) I could crib
a solution from.

<!-- read more -->

I've also made some improvements in the test suite. It still fails on Windows
due to issues with filepath separators, but most tests now pass on Travis. The
remaining failing test appears to be due to some changes in exactly how Pillow
(the image processing library used here) transforms the images.

## Upgrading

To upgrade simply use `pip`:

~~~sh
pip install minchin.pelican.plugins.image_process --upgrade
~~~
