title: Jinja Filters 1.1.0 & 2.1.0 for Pelican Released
date: 2021-04-30 9:37
tags: pelican, pelican plugins, releases, python, pelican themes, jinja filters
Category: Pelican Plugins

**Jinja Filters** is a plugin for [Pelican](http://docs.getpelican.com/), a
static site generator written in Python.

**Jinja Filters** provides a selection of functions (called *filters*) for
templates to use when building your website. They are packaged for Pelican, but
may prove useful for other projects that make use of
[Jinja2](http://jinja.pocoo.org/).

## This Release
<!-- PELICAN_BEGIN_SUMMARY -->
This post actually covers three releases:

- **v1.1.0** doesn't add any functionality or bugfixes directly, but is
  designed to point users to the new v2 releases.
- **v2.0.0** reorganized the project codebase to make this work as a "namespace
  plugin". Added by Pelican 4.5 is a feature to automatically activate such
  plugins. It also transfers the code repo to the
  [Pelican-Plugins](https://github.com/pelican-plugins/jinja-filters0)
  organization and moved the PyPI package to `pelican-jinja-filters`.
- **v2.1.0** adds two filters -- *merge_date_url* and *datetime_from_period*.
  It also lowers the minimum Pelican version to 3 (from 4.5). Under the hood,
  it also updates the local development infrastructure to work better on
  Windows.
<!-- read more -->

## Upgrading

### to v1.1.0

To upgrade simply use `pip`:

~~~sh
pip install minchin.pelican.jinja-filters --upgrade
~~~

v1.1.0 actually depends on v2.1.0 or newer, which will automatically be
installed. 

As a side, this (having one version of a package rely on another
version of the "same" package) is generally not desirable or even possible. But
PyPI/pip has no real concept of package re-naming, and the two different
package names is what makes this work.

If you run v1.1.0, you will get a warning message when you generate your site
with Pelican encouraging you to upgrade to v2. This is mostly for those who
won't stumble upon this blog entry! That said, the plugin will continue to work
as it has previously without further effort on your part.

### to v2.0.0

v2.0.0 has a different package name, so you'll have to uninstall the old
package and install the new one. Again, `pip` is the simplest way:

~~~sh
pip install pelican-jinja-filters --upgrade
pip uninstall minchin.pelican.jinja-filters
~~~

The new package name and file layout is to make the plugin a "namespace
plugin". *Namespace plugins* are actually a really cool idea that if you create
your package in the right way, your "host" program can find the plugins simply
by having them installed on your system! For Pelican, they need to be in the
`pelican.plugins` namespace.

Two caveats of this approach is that you'll need Pelican version 4.5 (or later)
to automatically load these namespace plugins, and (at least if my
understanding is correct) you have to either rely on namespace plugins alone OR
the `PLUGINS` setting of your `pelicanconf.py`; i.e. if you specify `PLUGINS`
in your settings, auto-loading of namespace plugins is turned off. Neither of
these are deal breakers, but this background may prove useful in debugging your
setup. Overall, I think namespace plugins are an awesome idea, and I hope it
doesn't take too long to get everything switched over.

So if you're using other non-namespace plugins, or a Pelican version before
4.5, you'll also need to update your `pelicanconf.py` with the new plugin name:

~~~python
# pelicanconf.py

PLUGINS = [
    # others...
    # minchin.pelican.jinja_filters  # <-- remove this line
    "pelican.plugins.jinja_filters",
]
~~~

Finally, v2.0.0 bumps the minimum Pelican version up to 4.5; if you're using an
older version of Pelican and don't want to upgrade yet, then use v2.1.0 of the
plugin.

### to v2.1.0

Assuming you've done the steps listed above to upgrade to v2.0.0, `pip` remains
the simplist way to upgrade:

~~~sh
pip install pelican-jinja-filters --upgrade
~~~

This version lowers the minimum Pelican version 3 (which is something I needed
to incrementally upgrade my site; I'm stuck at v3.7.1 for a bit yet while I
upgrade some other plugins).

It also added two new filters: *merge_date_url* and *datetime_from_period*. I
added these in particular for use on the period archive pages (i.e. yearly,
monthly, and daily archives) and will be used by the next version of
[seafoam](https://blog.minchin.ca/label/seafoam/) (the theme on this site).

## Details on the New Features (of v2.1.0)

### datetime_from_period

By way of background, Pelican feeds a tempate variable called `period` to the
template when generating period archive pages. However, the variable is a tuple
with the month (when present) as a string. If the text is already formatted the
way you want (and the default is generally sensible), then you can just display
it as is. However, this filter can turn that tuple into a "proper"
`datetime.datetime` object to be further processed.

You might use it like this:

~~~html+jinja
{{ period | datetime_from_period | datetime('%Y') }}
~~~

(*datetime*, as used here, is another filter provided by this plugin.)

As an implementation note, if the month is not supplied (e.g. on a yearly
archive page), this filter will assume it is January; if the date is not
supplied (i.e. on a yearly or monthly archive page), the 1st is assumed.

### merge_date_url

When given a datetime (on the left to operate on), and provided with a period
archive url (typically a Pelican setting like `YEAR_ARCHIVE_URL`), it will
"apply" the date to the URL.

So the two might be used together like this (example pulled from the pending
[seafoam](https://blog.minchin.ca/label/seafoam/) release):

~~~html+jinja
<a href="{{ SITEURL -}} /
         {{- period | datetime_from_period | merge_date_url(YEAR_ARCHIVE_URL) }}">
    {{ period | datetime_from_period | datetime('%Y') }}
</a>
~~~

while will result in the generated HTML:

~~~html
<a href="https://blog.minchin.ca/posts/2021/>2021</a>
~~~

## Thoughts on These Releases and the Future

This part is more of a personal than technical note.

Eagle-eyed among you may notice that the initial version 2 release happened
back in August. I was actively involved in [the
process](https://github.com/pelican-plugins/jinja-filters/pull/4), but it's
taken some time to decide what to make the changes that involved.

Overall, I still think moving the plugin to a organization repo is a good
thing. This should help with visibility, and hopefully this will result in more
people contributing to it. But it is also weird to "let go" of this code, in
the sense that it is no longer under my username on GitHub.

The biggest technical changes on the backend side involved a complete
replacement of the release machinery. Previously I'd been using a home-grown
script ([minchin.releaser](https://github.com/MinchinWeb/minchin.releaser)) to
do releases; it was mine, and I could punch out a release from a single
command. That was replaced by [AutoPub](https://github.com/autopub/autopub),
which is a "bot" to automatically publish releases from your project's
continuous integration system; this has the benefit of basically being
completely automated. And for a multi-user environment (like the hope is with
the new code repo location), this new setup makes a lot of sense.

One oddity of giving up, or a least sharing, ownership of the code, is that I
had [Justin Mayer](https://github.com/justinmayer) (who manages both the
Pelican project and Pelican-Plugins) review my proposed changes. I think my
code is better for it; I know for many of the changes I ended up writing a
whole bunch about what and why I wanted the changes I was proposing, sometimes
longer than the actual code in question.

The last big change was a switch from a `setup.py`/`requirements.txt` setup
(supported by [pip-tools](https://github.com/jazzband/pip-tools)) to a
[poetry](https://python-poetry.org/)/`pyproject.toml` setup. I don't know if
this is "the way of the future" (as some have made it out to be), but this is
the change I'm least sold on. *poetry* has proved tricky to configure at times,
is very opinionated, and sometimes hides it's logic under the covers. As well,
I'm not sure it's solved any problem I didn't already have solved. But I'll use
it for projects like this, and just count it among the (slight) costs of
working with others.

Moving forward, I'm not sure if every release will get a release post. I
suspect the releases I'm involved in will get a post, but hopefully there will
be some without my involvement!

Now, only 11 more plugins to go! I want to move all the plugins I use to
namespace plugins and then upgrade from Pelican 3.7.1 to 4.6 (or whatever the
then-current version is). I'm a little bit closer. :)
