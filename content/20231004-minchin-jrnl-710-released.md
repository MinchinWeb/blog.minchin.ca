Title: minchin.jrnl v7.1 "Phoenix" released
Date: 2023-10-04 11:23 -0600
Tags: Python, releases, minchin.jrnl, forks (software)
Category: minchin.jrnl
Image: images/2023/0330-sdxl-781_432_927-40-20230809_070914.png

Today, the lastest update of *minchin.jrnl* was released! This release add
custom exporters and importers!

## Upgrading

You can upgrade it today:

~~~cmd
pip install minchin.jrnl --upgrade
~~~

## Custom Plugins (Importers and Exporters)

Under the hood, custom plugins rely to Python's namespaces. Python code (in the
right format and with the right attributes) placed in the
`minchin.jrnl.contrib.importer` namespace (for importers) and the
`minchin.jrnl.contrib.exporter` namespace (for exporters) will automatically be
loaded by *minchin.jrnl*.

You can read more about how to write plugins in the
[documentation](http://minchin.ca/minchin.jrnl/reference/plugins/). I also
wrote a custom exporter to Obsidian flavoured Markdown (for my immediate use!).
You can review the code on
[GitHub](https://github.com/MinchinWeb/minchin.jrnl.contrib.exporter.obsidian)
if you want to see a working example.

Custom plugins can override the built-in functionality. Do see what plugins you
have active, you can run `jrnl --diagnostic`, and you will get output similiar to:

~~~txt
minchin.jrnl: 7.1.0 "Phoenix"
Python: 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)]
OS: Windows 10

Active Plugins:
    Importers:
        jrnl     : 7.1.0 from minchin.jrnl.plugins.importer.jrnl
    Exporters:
        boxed    : 7.1.0 from minchin.jrnl.plugins.exporter.fancy
        dates    : 7.1.0 from minchin.jrnl.plugins.exporter.dates
        default  : 7.1.0 from minchin.jrnl.plugins.exporter.pretty
        fancy    : 7.1.0 from minchin.jrnl.plugins.exporter.fancy
        json     : 7.1.0 from minchin.jrnl.plugins.exporter.json
        markdown : 7.1.0 from minchin.jrnl.plugins.exporter.markdown
        md       : 7.1.0 from minchin.jrnl.plugins.exporter.markdown
        pelican  : 7.1.0 from minchin.jrnl.plugins.exporter.pelican
        pretty   : 7.1.0 from minchin.jrnl.plugins.exporter.pretty
        short    : 7.1.0 from minchin.jrnl.plugins.exporter.short
        tags     : 7.1.0 from minchin.jrnl.plugins.exporter.tag
        text     : 7.1.0 from minchin.jrnl.plugins.exporter.text
        txt      : 7.1.0 from minchin.jrnl.plugins.exporter.text
        xml      : 7.1.0 from minchin.jrnl.plugins.exporter.xml
        yaml     : 7.1.0 from minchin.jrnl.plugins.exporter.yaml
~~~


## Short Term Update Plans

When I first [released v7]({filename}20230919-minchin-jrnl-700-released.md), I
had three major short term objectives: get the project live, lift the Python
version cap, and get the plugin system working. With today's release, all of
those three have been accomplished!

Several of my medium term goals have also been accomplished (easy to push
releases, drop *poetry*, replace the Code of Conduct) or are underway
(documentation in Sphinx, posted on [my
site](http://minchin.ca/minchin.jrnl/reference/plugins/)).

However, I realize that my notetaking now mostly happens through Obsidian, and
so I'm not sure how much I'll be using *minchin.jrnl* going forward. That said,
I'm about to start a new job, and so may end up using it again to take daily
notes; time will tell.

## Changelog

Version 7.1.0 "Phoenix" was released October 4th, 2023.

- **feature**: merge external plugin support, as per legacy [Pull Request
  #1216](https://github.com/jrnl-org/jrnl/pull/1216). Also merges relevant
  parts of legacy [Pull Request
  #1115](https://github.com/jrnl-org/jrnl/pull/1115); c.f. legacy [Pull Request
  #1281](https://github.com/jrnl-org/jrnl/pull/1281).
- **feature**: allow top-level `__version__` without use of an `__init__.py`
  file. c.f. legacy [Pull Request
  #1296](https://github.com/jrnl-org/jrnl/pull/1296). This had (previously?)
  been required for namespace plugins to load.
- **bug**: allow exporting files to nested directories.
- **bug**: Work with updated (v4 or later) `tzlocal` API. (DayOne classic
  journal particular issue.) c.f. legacy [Pull Request
  #1528](https://github.com/jrnl-org/jrnl/pull/1528).

## Other Links

- [all release posts]({tag}minchin.jrnl) for *minchin.jrnl*
- code, on GitHub at <https://github.com/MinchinWeb/minchin.jrnl>
- [full changelog](http://minchin.ca/minchin.jrnl/changelog/)
