title: Summary Plugin 1.1.0 for Pelican Released
date: 2017-02-05 15:29
modified: 2017-02-21 14:51
tags: Pelican, Pelican Plugins, Releases, Python, Summary (Pelican)
Category: Pelican Plugins

**Summary** is a plugin for [Pelican](http://docs.getpelican.com/), a static
site generator written in Python.

**Summary** allows easy, variable length summaries directly embedded into the
body of your articles.
<!-- read more -->

## Installation

The easiest way to install **Summary** is through the use of pip. This will
also install the required dependencies automatically (currently none beyond
Pelican).

~~~~sh
pip install minchin.pelican.plugins.summary
~~~~

Then, in your `pelicanconf.py` file, add **Summary** to your list of
plugins:

~~~python
PLUGINS = [
          # ...
          'minchin.pelican.plugins.summary',
          # ...
        ]
~~~

You may also need to configure the summary start and end markers (see
Configuration below).

## Configuration and Usage

This plugin introduces two new settings: `SUMMARY_BEGIN_MARKER` and
`SUMMARY_END_MARKER`: strings which can be placed directly into an article to
mark the beginning and end of a summary. When found, the standard
`SUMMARY_MAX_LENGTH` setting will be ignored. The markers themselves will also
be removed from your articles before they are published. The default values are
`<!-- PELICAN_BEGIN_SUMMARY -->` and `<!-- PELICAN_END_SUMMARY -->`.

If no beginning or end marker is found, and if `SUMMARY_USE_FIRST_PARAGRAPH` is
enabled in the settings, the summary will be the first paragraph of the post.

The plugin also sets a `has_summary` attribute on every article. It is True for
articles with an explicitly-defined summary, and False otherwise. (It is also
False for an article truncated by `SUMMARY_MAX_LENGTH`.) Your templates can use
this e.g. to add a link to the full text at the end of the summary.

## Known Issues

<del>An issue, as such, is that there is no formal test suite. Testing is
currently limited to my in-use observations. I also run a basic check upon
uploaded the package to PyPI that it can be downloaded and loaded into
Python.</del>

<del>The package is tested in Python 3.5; compatibility with other version of
Python is unknown.</del>

Tests are actually included and can be run from the root directory:

~~~sh
python minchin/pelican/plugins/summary/test_summary.py
~~~

## Changes

This version is basically just repackaging the plugin and making it available
on pip.

## Code

The code for this project is available on [GitHub](https://github.com/MinchinWeb/minchin.pelican.plugins.summary). Contributions are welcome!

## Credits

Original plugin from the [Pelican-Plugins repo](https://github.com/getpelican/pelican-plugins).

## License

The plugin code is assumed to be under the AGPLv3 license (this is the license
of the Pelican-Plugins repo).
