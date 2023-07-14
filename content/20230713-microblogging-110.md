title: Microblogging 1.1.0 for Pelican Released
date: 2023-07-14 11:52 -0600
tags: Pelican, Pelican Plugins, Releases, Python, Microblogging (Pelican)
Category: Pelican Plugins

*Microblogging* is a plugin for [Pelican](http://docs.getpelican.com/),
a static site generator written in Python.

*Microblogging* is a plugin to allow you to have "micro" (or "&micro;" or
small) posts, similarly (at least outwardly) to Twitter, Mastodon, or Threads.
<!-- read more -->

This is by no means a complete replacement for Twitter (or Mastodon), but if
you want to record your thoughts, especially your short ones, on your own site,
this should allow you to do that. (For longer thoughts, at this point you've
already got Pelican set up, so don't be afraid to create "real" blog posts!)

For best results, you probably want to upgrade your theme to support
&micro;posts, but it should work out of the box with your existing theme
(assuming it supports posts generally).
*[Seafoam](http://blog.minchin.ca/label/seafoam/)* will have a release
presently with support for &micro;posts.

Pull Requests to extend the functionality of the plugin are by all means
welcomed!

## Installing

The simplest way to install (and upgrade) *Microblogging* is to use `pip`:

~~~sh
pip install minchin.pelican.readers.microblog --upgrade
~~~

If you're using *seafoam* as your theme, you will want to upgrade that to at
least v2.9.0.


## Configuration

The plugin tries to provide sensible defaults, and so no configuration should
be necessary to get it up and running.

Available configuartion options (place these in your `pelicanconf.py` file) and
their defaults:

MICROBLOG_FOLDER = "micro"

: Folder containing your &micro;posts, relative to your content root folder.

MICROBLOG_MAX_LENGTH = 140

: How long should your &micro;posts be limited to. Pelican will emit a warning
   if you exceed this.

MICROBLOG_SAVE_AS = ARTICLE_SAVE_AS

: What to save the &micro;posts' output file as. Defaults to using the same
   file structure as you are using for articles (aka "regular" posts). c.f.
   `MICROBLOG_URL`.

MICROBLOG_SLUG = "u{date:%Y%m%d%H%M}"

: The slug that will be used for &micro;posts. Eg. `u202307091701`. Note
that Pelican expects slugs to be universally unique.

MICROBLOG_URL = ARTICLE_URL

: What URL to post the &micro;posts to. Defaults to using the same URL
   structure as you are using for articles (aka "regular" posts). c.f.
   `MICROBLOG_SAVE_AS`.


## Sample &micro;posts

These are samples of what the source for &micro;posts might look like. Place
them in a subfolder called `micro` of your main content folder.

Basic &micro;post:

```md
<!-- ./content/micro/202307091701.md -->

date: 2023-07-09 17:01

I'm microblogging with Pelican!
https://blog.minchin.ca/label/microblogging-pelican
```

---

Or a post with an (featured) image:

```md
<!-- ./content/micro/202307112138.md -->

date: 2023-07-11 21:38
image: images/birger-strahl-olI66vtMgNo-unsplash.jpg

Microblog posts can have "feature" images too! (URL of photo should
automatically be added.)
```

The image path is relative to your `content` folder. A URL of the photo is
added to the end of the post as well.

---

Or with tags (or hashtags):

```md
<!-- ./content/micro/202307131456.md -->

date: 2023-07-13 14:56
tags: Python, Pelican, Microblogging

I'm now Microblogging with Pelican!
```

This will add links at the end of your post to the tags to the tag page for
your (Pelican) site.

For now, the plugin is not smart enough to pull tags out of the body of your
post.


# Updating Your Theme

Although updating your theme is not *strictly* necessary, you will probably get
more satifactory results if you do. Some pointers as you go about your update:

- &micro;posts are considered `Articles` by Pelican, and will be included
  in the `articles` and `dates` "lists" provided by the templating engine.
- each &micro;post is tagged with `article.micro = True`, so this can be used
  as a test for conditional formating.
- &micro;posts have a title (as required for Pelican), but you probably want to
  hide/not display the title, as titles are of the form `u201307180934`.
- &micro;posts are short; by default they are encouraged to be no more than 140
  displayed characters. If you intend to abide by that, there are several
  places (like your archive list) where it may make sense to show the whole
  &micro;post (`article.content`) rather than the title and a link to the full
  post page.


## Release History

This release is v1.1.0, released July 13, 2023.

- **feature**: Support hashtags, if given in frontend post metadata. See [Issue
  #7](https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/7).

Version 1.0.0, released July 11, 2023.

- **feature**: Support feature image for microblog posts.
- **feature**: Supports basic posting and processing of "micro" blog posts.
  Posts are assumed to be written in Markdown (so plain text works as well).
  Posts must have a `date` metadata key.
- Initial public release!


## Known Issues

- hashtags can't be pulled out of post body
- &micro;posts seem to mess up the ordering of the `articles` list passed to
  the templating engine. Use `dates` instead (which is sorted by date)?
- text (metadata and body) processing relies on Pelican's built-in Markdown
  reader.


## Personal Thoughts (on the Plugin, Development, and Microblogging)

In terms of development, it is perhaps interesting to note that this project
was "Readme Driven Development"[^RDD], where I first wrote the Readme file, and
then developed the feature set to be able to provide what I'd outlined in the
Readme. I was able to do this initial "development work" on my phone in
*vim*[^phone-vim] (via *Termux*), but I was glad to move to the larger screen
of my desktop for the coding portion, in particular because I was updating
another plugin (*autoloader*), updating my Pelican theme (*seafoam*), and
taking random dives into the Pelican documentation and codebase all as I
developed this plugin. The update to *seafoam* will be released as soon as I
have this blog post to link to. :)

It has also been very satisfying to go from *idea* to *working* in under a
week.

I'm still not certain how this will effect my personal blog. Part of me still
longs for the early days of Facebook when I could privately post random
thoughts on my *Wall* for my friends to see. That died when Facebook played
with the privacy settings so many times that I wasn't convinced they intended
to keep anything private (plus, most of my social life had moved elsewhere).
I've had a Twitter account for years, but never really used it to post
anything. With the current chaos at Twitter and excitement around Mastodon (and
Threads), I considered setting up a Mastodon account, but it seems the sensible
thing would be to stand up my owner server for my own account; this is way less
work! The missing part of this plugin in its current form is the social aspect,
and that will take more thought on how to implement. For now, I have comments
via email, as with any other post on this site.

So will I be comfortable write more microposts? Will they seem less serious,
and so can be *off the cuff*? Time will see, I guess.

Let me know how it works for you if you install this, and if you don't, let me
know what keeps you from using this.


## Other Links

- [all release posts]({tag}Microblogging (Pelican)) for *microblogging* (only
  this post so far!)
- code, including full configuration directions, on GitHub at
  [MinchinWeb/minchin.pelican.readers.microblog](https://github.com/MinchinWeb/minchin.pelican.readers.microblog)
- [full changelog](https://github.com/MinchinWeb/minchin.pelican.readers.microblog/blob/master/CHANGELOG.rst)


[^RDD]: as opposed to Test Driven Developement (TDD) or Behavior Driven
    Development (BDD). Tom Preston-Werner actually provides a [good
    overview](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html)
    of the theory of Readme Driven Development.
[^phone-vim]: I'm still looking for a good "graphical" plain text editor for my
    Android phone. Suggestions?
