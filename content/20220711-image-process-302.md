title: Image Process Plugin 3.0.2 for Pelican Released
date: 2022-07-11 13:02
Modified: 2022-07-11 17:39
tags: Pelican, Pelican Plugins, Releases, Python, Pelican Themes, Image Process
Category: Pelican Plugins

*Image Process* is a plugin for [Pelican](http://docs.getpelican.com/),
a static site generator written in Python.

*Image Process* let you automate the processing of images based on their HTML
class attributes. Use this plugin to minimize the overall page weight and to
save you a trip to Gimp or Photoshop each time you include an image in your
post.

*Image Process* is used by
[this blog's theme](https://github.com/MinchinWeb/seafoam) to resize the source
images so they are the correct size for thumbnails on the main index page and
the larger size they are displayed at on top of the articles.

## This Release

<!-- PELICAN_BEGIN_SUMMARY -->
This post actually covers three releases:

- **v3.0.0** adds support for Pillow v9. No changes were made that would make
  the plugin incompatible with earlier versions of Pillow, other than the test
  output images are slightly different between Pillow 8 and 9. This version
  also removed (official) support for Python 3.6, which isn't supported by
  Pillow 9.
- **v3.0.1** fixes function calls that will be deprcated by Pillow v10,
  scheduled to be released in about a year from now. These changes probrobably
  make the plugin incompatible with versions of Pillow before v9.1.0.
- **v3.0.2** bumps the lowest officially supported version of Pillow to v9.1.0
  and (preemptively) adds support for v10.
<!-- read more -->

## Upgrading

### to v3.0.0

To upgrade simply use `pip`:

~~~sh
pip install pelican-image-process --upgrade
~~~

This should automatically upgrade Pillow (if needed) as well.

Python 3.6 is no longer officially supported.

The code for this release was ready back in February, but issues with the
release framework kept the "official" release from happening until now.

### to v3.0.1 and v3.0.2

Again, use `pip`, as above.

This should work with Pillow 10 when it is released.
