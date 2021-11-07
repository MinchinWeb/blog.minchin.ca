title: Image Process Plugin 1.2.1 & 2.1.1 for Pelican Released
date: 2021-05-15 14:46
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
This post actually covers five releases:

- **v1.2.1** doesn't add any functionality or bugfixes directly, but is
  designed to point users to the new v2 releases.
- **v1.3.0** returned the plugin to the stewardship of [Whisky Echo
  Bravo](https://github.com/whiskyechobravo/), who wrote the first versions of
  this plugin. This is the first version of the plugin available on PyPI as `pelican-image-process`.
- **v2.0.0** reorganized the project codebase to make this work as a "namespace
  plugin". Added by Pelican 4.5 is a feature to automatically activate such
  plugins. This release also fixed a bug with the crop API, and added the
  ability to create progressive JPEGs and to work within Atom feeds. It also
  transfers the code repo (and project stewardship) to the
  [Pelican-Plugins](https://github.com/pelican-plugins/image-process)
  organization.
- **v2.1.0** adds the ability to copy EXIF data to processed photos.  
- **v2.1.1** lowers the minimum Pelican version to 3 (from 4.5). Under the hood,
  it also updates the local development infrastructure to work better on
  Windows.
<!-- read more -->

## Upgrading

### to v1.2.1

To upgrade simply use `pip`:

~~~sh
pip install minchin.pelican.plugins.image-process --upgrade
~~~

If you run v1.2.1, you will get a warning message when you generate your site
with Pelican encouraging you to upgrade to v2. This is mostly for those who
won't stumble upon this blog entry! That said, the plugin will continue to work
as it has previously without further effort on your part.

### to v1.3

I'd recommend you skip this update, at this point, and go straight to v2.
There's nothing wrong with this release, *pre se*, but I'm not in a position to
test any installation instructions.

### to v2

v1.3 introduced a different package name, so you'll have to uninstall the old
package and install the new one. Again, `pip` is the simplest way:

~~~sh
pip install pelican-image-process --upgrade
pip uninstall minchin.pelican.plugins.image-process
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
    # minchin.pelican.plugins.image_process  # <-- remove this line
    "pelican.plugins.image_process",
]
~~~

Finally, v2.0.0 bumps the minimum Pelican version up to 4.5; if you're using an
older version of Pelican and don't want to upgrade yet, then use v2.1.1 of the
plugin.

The new features (generating progressive JPEGs and applying to Atom feed images)
are automatically enabled.

As for the change in the crop API, it's a bugfix so the plugin behaviour should now match the documented (anticipated) behaviour; specifically `crop <top> <left> <right> <bottom>`.

### to v2.1.0

Assuming you've done the steps listed above to upgrade to v2.0.0, `pip` remains
the simplest way to upgrade:

~~~sh
pip install pelican-image-process --upgrade
~~~

To copy over EXIF data, you'll need to set `IMAGE_PROCESS_COPY_EXIF_TAGS` (in your `pelicanconf.py`) to `True`. You will also need to install [ExifTool](https://exiftool.org/). I haven't tried it but it looks like ExifTool supports Windows, just be sure that it's been added to your PATH.

### to v2.1.1

Assuming you've done the steps listed above to upgrade to v2.1.0, `pip` remains
the simplest way to upgrade:

~~~sh
pip install pelican-image-process --upgrade
~~~

This version lowers the minimum Pelican version 3 (which is something I needed
to incrementally upgrade my site; I'm stuck at v3.7.1 for a bit yet while I
upgrade some other plugins).

## Thoughts on These Releases and the Future

This part is more of a personal than technical note, and continuation of my
thoughts about the last *[Jinja
Filters]({filename}20210430-jinja-filters-210.md#personal-thoughts)* release.

The "ownership" of this code is even more involved that the *Jinja Filters*
plugin. With *Jinja Filters*, that was code that I'd written myself, packaged,
and eventually moved (at my request) to be under the Pelican Plugins
organization. Here, I adopted someone else's existing code, packaged it and used
it myself, and eventually they returned from the woodwork to reclaim it (and
then transferred it to the Pelican Plugins organization). On one hand, this
represent the wonder of Open Source in that I resurrect a "dead" plugin; on the
other, it raises an interesting question of what does *ownership* mean in such a
landscape? Did I ever "own" this code? Was it mine to give away or surrender? I
think the language fails here, and so perhaps the term "stewardship" rather than
"ownership" is more helpful.

In any case, I'm excited to see that the plugin is being maintained without
requiring a bunch of my personal effort and is getting features added as well.
When I had assumed stewardship for maintenance, I always felt at a disadvantage
because I didn't have the deep understanding that would have come from writing
the original code, so I'm happy to let someone else take that on. I'm slightly
sad though because this plugin represented my most starred repo on GitHub, and
was the one Pelican plugin that I'd put out to the world that I knew other
people were actually using.

Moving forward, I'm not sure if every release will get a release post. I
suspect the releases I'm involved in will get a post, but hopefully there will
continue to be some without my involvement!

Now, only 10 more plugins to go! I want to move all the plugins I use to
namespace plugins and then upgrade from Pelican 3.7.1 to 4.6 (or whatever the
then-current version is). I'm a little bit closer. :)
