title: Jinja Filters 1.0.0 for Pelican Released
date: 2016-11-18 17:41
tags: pelican, pelican plugins, releases, python
Category: Pelican Plugins


**Jinja Filters** is a plugin for [Pelican](http://docs.getpelican.com/),
a static site generator written in Python.

**Jinja Filters** provides a selection of functions (called *filters*) for
templates to use when building your website. They are packaged for Pelican, but
may prove useful for other projects that make use of
[Jinja2](http://jinja.pocoo.org/).

<!-- read more -->

## Installation

The easiest way to install **Jinja Filters** is through the use of pip. This
will also install the required dependencies automatically.

~~~~sh
pip install minchin.pelican.jinja_filters
~~~~

Then, in your `pelicanconf.py` file, add **Jinja Filters** to your list of
plugins:

~~~python
PLUGINS = [
          # ...
          'minchin.pelican.jinja_filters',
          # ...
        ]
~~~

And that's it! The filters are now available for use in your templates.


## Usage

At present, the plugin includes the following filters:

- *datetime* -- allows you to change to format displayed for a datetime
  object. Optionally supply a [datetime format string](https://docs.python.org/3.6/library/datetime.html#strftime-and-strptime-behavior)
  to get a custom format.
- *article_date* -- a specialized version of *datetime* that returns
  datetimes as wanted for article dates; speciefically
  *Friday, November 4, 2016*.
- *breaking_spaces* -- replaceds non-breaking spaces (HTML code *&nbsp*)
  with normal spaces.
- *titlecase* -- Titlecases the supplied string

For example, within your theme templates, you might have code like:

~~~html+jinja
<span class="published">
    Article Published {{ article.date | article_date }}
</span>
~~~

gives:

~~~    
    Article Published Friday, November 4, 2016
~~~

Or with your own dateformat:

~~~html+jinja
<span class="published">
    Article Published {{ article.date | datetime('%b %d, %Y') }}
</span>
~~~

gives:

~~~
    Article Published Nov 04, 2016
~~~

Fitlers can also be chained, or applied in sequence. For example to remove
breaking spaces and then titlecase a catgory name, you might have code like:

~~~html+jinja
<a href="{{ SITEURL }}/{{ article.category.url }}">
    {{ article.category | breaking_spaces | titlecase}}
</a>
~~~


## Known Issues

An issue, as such, is that there is no formal test suite. Testing is
currently limited to my in-use observations. I also run a basic check upon
uploaded the package to PyPI that it can be downloaded and loaded into
Python.

The package is tested in Python 3.5; compatibility with other version of
Python is unknown.

## Code

The code for this project is available on [GitHub](https://github.com/MinchinWeb/minchin.pelican.jinja_filters). Contributions are welcome!
