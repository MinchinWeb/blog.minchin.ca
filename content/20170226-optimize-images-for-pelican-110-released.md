title: Optimize Images Plugin 1.1.0 for Pelican Released
date: 2017-02-26 20:00
tags: Pelican, Pelican Plugins, Releases, Python, Optimize Images
Category: Pelican Plugins

*Optimize Images* is a plugin for [Pelican](http://docs.getpelican.com/), a
static site generator written in Python.

*Optimize Images* applies lossless compression on JPEG and PNG images, with no
effect on image quality. It uses [jpegtran](http://jpegclub.org/jpegtran/) and
[OptiPNG](http://optipng.sourceforge.net/).
<!-- read more -->

## Installation

The easiest way to install *Optimize Images* is through the use of pip. This
will also install the required Python dependencies automatically (currently
none beyond Pelican itself).

~~~sh
pip install minchin.pelican.plugins.optimize_images
~~~

It is assumed both jpegtran and OptiPNG are installed and available on the
system path.

Then, in your ``pelicanconf.py`` file, add ``Optimize Images`` to your list of
plugins:

~~~python
PLUGINS = [
           # ...
           'minchin.pelican.plugins.optimize_images',
           # ...
           ]
~~~

## Requirements

*Optimize Images* depends on (and is really only useful with) Pelican. This can
be manually installed with pip:

~~~sh
pip install pelican
~~~

It is assumed both jpegtran and OptiPNG are installed on system path. On
Windows, installers are available at each respective website. On Ubuntu systems
(including Travis-CI), the two can be installed via *apt-get*.

~~~sh
apt-get install optipng libjpeg-progs
~~~

## Configuration and Usage

The plugin will activate and optimize images upon *finalized* signal of
Pelican.

The plugin has no user settings.

## Known Issues

Image manipulation like this can take some time to run. You may consider only
adding this plugin to your `publishconf.py` (rather than your base
`pelicanconf.py`), which will then only run this image optimization in
preparation for site publication.

An issue, as such, is that there is no formal test suite. Testing is currently
limited to my in-use observations. I also run a basic check upon uploaded the
package to PyPI that it can be downloaded and loaded into Python.

The package is tested in Python 3.6; compatibility with other version of Python
is unknown, but there should be nothing particular keeping it from working with
other "modern" versions of Python.

## Credits

Original plugin from the [Pelican-Plugins
repo](https://github.com/getpelican/pelican-plugins).

## License

The plugin code is assumed to be under the AGPLv3 license (this is the
license of the Pelican-Plugins repo).
