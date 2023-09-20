Title: minchin.jrnl v7 "Phoenix" released
Date: 2023-09-19 21:39 -0600
First_Draft: 2023-03-12 19:25:43
Tags: Python, releases, minchin.jrnl, forks
Category: minchin.jrnl
Image: images/2023/0330-sdxl-781_432_927-40-20230809_070914.png

Today, I do something that I should have done 5 years ago, and something that
I've been putting off for the last 2 years[^1]: I'm releasing a personal fork
of *jrnl*[^2]! I've given this release the codename **Phoenix**, after the
mythical bird of rebirth, the springs forth renewed from the ashes of the past.

You can install it today:

~~~cmd
pip install minchin.jrnl
~~~

And then to run it from the command line:

~~~cmd
minchin.jrnl
~~~

(or

~~~cmd
jrnl
~~~

)


## Features Today

Today, the codebase is that of *jrnl* v2.6[^3] in a new namespace. In
particular, that gives us a working *yaml exporter*; now you can build your
Pelican sites again (or maybe only I was doing that...).

The version number (7) was picked to be larger than the current *jrnl-org/jrnl*
release (currently at 4.0.1).

I've moved the configuration to a new location on disk[^4], as to not stomp on
your existing *jrnl* (i.e. *jrnl-org/jrnl* or "legacy") installation.

Documentation, to match the current codebase, has been uploaded to my personal
site at [minchin.ca/minchin.jrnl](http://minchin.ca/minchin.jrnl/). (Although
it remains incomplete and very much a work in progress.)

And finally, I extend an invitation to all those current or former users of
*jrnl* to move here. I welcome your contributions and support. If there are
features missing, please feel free to let me know.


## Short Term Update Plans

I've pushed these release out with very few changes from the base codebase in a
effort to get it live. But I have some updates that I'm planning to do very
shortly. There updates will maintain the *Phoenix* codename, even if the major
version number increments.

The biggest of these is to launch my much anticipated plugin system. The code
has been already written (for several years now[^5], actually), can it just
needs to be double checked that it still works as expected.

The other immediate update is to make sure the code works with Python 3.11 (the
current version of Python), which seems to already be the case.


## Medium to Long Term Project Goals, or My Vision

These are features I'd like to add, although I realize this will take more than
tonight. Also this section lays out my visions for the project and some
anti-features I want to avoid.


### The Plugin System

The plugin system I think will be huge movement forward to make *minchin.jrnl*
more useful. In particular, it allows *minchin.jrnl* to import and export to
and from new formats, including allowing you to write one-off export formats
(which I intend to use personally right away!). Displying the journal entries
on the commandline is also handled by exporters, so you'd be able to tweak that
output as well. I also intend to extend the plugin system to the storage
backends.

My hope is that this will futureproof *minchin.jrnl*, allowing new formats to
quickly and easily be added, retiring deprecated formats to external plugins,
and being able to quickly test and integrate new formats by seemlessly bring
external plugins "in-house".

In particular, I'm planning to have separate plugins for "true" yaml + markdown
exports and Pelican-formated markdown, to add an export format for Obsidian[^6]
formatted markdown, and add backend format plugins to support *jrnl* v1 and
whatever format they're dreaming up for *jrnl* v4[^7].

In short, I hope plugins will allow you to make *minchin.jrnl* more useful,
without me being the bottleneck.


### Plain Text Forever

One of the things that drew to the original *jrnl* implementation was that is
was based on plain text, and using plain text to store journal entries. Plain
text has a number of advantages[^8], but the near universal backwards and
forewards compatibility in high on that list. Yes, plain text has it's
limitations[^9], but I think the advantages far outweight the disadvantages,
particularly when it comes to a journal that you might hope will be readable
years or generations from now. Also, plain text just makes it so much easier to
develop *minchin.jrnl*.

**The included, default option for *minchin.jrnl* will always be plain text.**

If you're looking to upgrade your plain text, you might consider Markdown[^10]
or ReStructured Text (ReST)[^11].

If you're looking for either a database backend or more multimedia
functionality (or both), you're welcome to write something as a backend plugin
for *minchin.jrnl*; that ability is a featured reason for providing the (to be
added shortly!) plugin system in the first place!


### MIT Licensed

The original *jrnl* was initially released under the [MIT
license](https://github.com/jrnl-org/jrnl/blob/v0.2.5/LICENSE), and that only
changed with the v2.4 release to GPLv3[^12]. My hope and goal is to remove all
GPL-licensed code and release future versions of *minchin.jrnl* under the MIT
license[^23].

My opposition to the change[^13] was because I've come to feel that Open Source
work is both *given and received as a gift*, and I feel the GPL license moves
away from that ethos.

I suspect the least fun part of this partial re-write will be getting the
testing system up and running again, as the original library *jrnl* v1 had been
using has gone many years without updates.

To this end, I'm requesting that any code contributions to the project be
dual-licensed under both MIT and GPLv3.


### Documentation in Sphinx

Documentation will eventually be moved over to Sphinx (from the current
MkDocs), a process I've began but not finished. Driving this is the expectation
that I'll have more technical documentation (than is included currently) as I
layout how to work with the plugin API, and Sphinx makes it easy to keep code
and documentation side by side in the same (code) file.

Furthermore, I want to document how to use *minchin.jrnl* as a Python API
generally; this would allow you to interact with your journal from other Python
programs.


### Easy to Push Releases

Knowing my own schedule, I want to be able to sit down for an evening, make
(several) small improvements, and then push out a new release before I go to
bed. To that end, I want to make the streamlined to push out new releases.
Expect lots of small releases. :)


### Drop *poetry*

*poetry* is a powerful Python project management tool, but is one I've never
really liked[^14]. Particular issues include a lack of first class Windows
support[^15] and very conservative upper bounds for dependencies and supported
Python versions. Plus I have refind a system elsewhere using *pip-tools*[^16]
and *setup.py* to manage these same issues that I find works very well for me.

This has been accomplished with the current release!


### Windows Support

*jnrl*, to date, has always had decent Windows support. As I personally work on
Windows, Windows will continue to have first class support.

Where this may show is tools beyond Python will need to be readily available on
Windows before they're used[^33], and the Windows Terminal is fairly
limited in what in can do, at least compared with some Linux terminals.


### Replace the Current *Code of Conduct*

I don't much care for the current *Code of Conduct*[^17]: it seems to be overly
focused on the horrible things people might do to each other, and I'm not sure
I want that to be the introduction people get to the project. I hope to find a
Code of Conduct that focuses more on the positive things I hope people will do
as they interact with each other and the project.

My replaced/current Code of Conduct is
[here](https://github.com/MinchinWeb/.github/blob/d01ae8608ad7a74d77304db90cdc6da61b269415/.github/CODE_OF_CONDUCT.md)
(although this may be updated again in the future).


### Open Stewardship Discussion

If the time comes when someone else is assuming stewardship for the project, I
intend for those discussions to be help publicly[^18].


## My History with the Project, and Why the Fork

This section is different: it is much less about the codebase and more focused
on myself and my relationship to it. I warn you it is likely to be somewhat
long and winding.


### My Introduction to *jrnl*

Many years ago now, I was new in Python. At that time[^34] when I came across a
problem that I thought programming might solve, I first went looking from a
Python program that might solve it.

In looking for a way to manage the regular text notes I was taking at work, I
found *jrnl*, which I eventually augmented with DayOne (Classic) for in-field
note entry (on a work-supplied iPad) and Pelican for display.

*Jrnl* was more though: it was the object of my first Pull Request[^35], my
first contribution to Open Source. My meagre help was appreciated and welcomed
warmly, and so I returned often. I found *jrnl* to be incredibly useful in
learning about Python best practices and code organization; here was a program
that was more than a toy but simple enough (or logically separated) that I
could attempt to understand it, to *gork* it, as a whole. I contributed in many
places, but particularly around Windows support, DayOne backend support, and
exports to Markdown (to be fed to Pelican).

In short *jrnl* became part of the code I used everyday.


### *jrnl* Goes Into Hibernation

I have heard it said that rewrites are a great way to kill a project. The
reasons for this are multiple, but in short it (typically) saps the energy to
update the legacy version even as bugs pile up, but the new thing can't go into
everyday use until it is feature-compatible with the legacy version, and the
re-write always takes way more effort that initial estimates.

For reasons now forgotten[^36], a “v2” semi-rewrite was undertaken. And then it
stalled. And then the project maintainer got a life[^19] and the re-write
stalled even moreso.


### The (Near) Endless Beta of v2, or the First Time I Should Have Forked

For me, initially, this wasn't a big deal: I was often running a development
build locally as I tinkered away with *jrnl*, so I just kept doing that. Also,
I had just started working on my plugin system (for exporters first, but
expecting it could easily be extended to importers and backends).

As the months of inactivity on the part of the maintainer stretched on, and
pull requests grew staler, at some point I should have forked the project and
“officially” released my development version. But I never did, because it
seemed like a *scary new thing* to do[^20].


### Invitation to Become a Maintainer

And then[^21] one day out of the blue, I got an email from the maintainer
asking if I wanted to be a co-maintainer for *jrnl*! I was delighted, and
promptly said yes. I was given commit access to the repo on GitHub (but, as far
as I knew, no ability to push releases to PyPI), and then...not much happened.
I reached out to the maintainer to suggest some plans, as it still felt like
"his" project, but I never heard much back. And I was too timid to move forward
without at least something from him. And I was busy with the rest of life too.
After a few months, I realized my first plan wasn't working and started
thinking about how to try again to move the project forward, more on my own. In
front of me was the push to v2.0, and a question of how to integrate my
in-development plug-in system.


### The Coup

And then on a one another day, again out of the blue, I got an unexpected email
that I no longer had commit access to the *jrnl* repo. I searched the project
for updates, including the issue tracker and came up with
[#591](https://github.com/jrnl-org/jrnl/issues/591) where a transition to new
maintainers was brought up; I don't know why I wasn't pinged on it. At the
time[^22], I said I was happy to see new life in the project and to see it move
forward. But it was unsettling that I'd missed the early discussions.

It also seemed odd to me that the two maintainer that stepped forward hadn't
seemed to be involved with the project at all before that point.

For a while, things were ok: a "version 2" was released that was very close to
the v2 branch I was using at home, bugs started getting fixed regularly, and
new releases continued to come out. But my plugins never made it into a
release.


### Things Fall Apart (aka I Get Frustrated)

But things under new management didn't stay rosy.

One of the things they did was completely rewrite the Git history, and thus
change all the commit hashes. This was a small but continueing annoyance (until
I got a new computer), because everytime I would go to push changes to GitHub,
my git client would complain about the "new" (old) tags it was trying to push,
because it couldn't find a commit with the matching hash.

But my two big annoyances were a re-write of the YAML exporter and the
continual roadblocks to getting my plugin system merged in.

My plugin system has the longest history, having been started before the change
in stewardship. Many times (after the change in stewardship), I created a pull
request[^24] and the response would be to make various changes or to split it
into smaller pieces; I would make the changes, and the cycle would continue.
But there was never a plan presented that I felt I could successful complete,
nor was I ever told the plugin system was unaligned with the vision they had
for the project. I lost considerable enthusiasm for trying to get the plugins
merged after rewriting the tests for the third time (as the underlying testing
framework was changed).

The YAML exporter changes are what ultimately left me feeling frozen out of the
project. Without much fanfare, the YAML exporter was changed, because
someone[^25] felt that the resulting output wasn't "true" or "pure" YAML. This
is true, in a sense, because when I had originally written the exporter, it was
designed to output files for Pelican with an assumed Markdown body and YAML
front matter for metadata. At the request of the (then) maintainer, I called it
the "YAML exporter", partly because there was already a "Markdown exporter". I
didn't realize it had been broken until I went to upgrade *jrnl* and render my
Pelican site (which I use to search and read my notes) and it had just stopped
working[^26]. The change wasn't noted (in a meaningful way) in the release
notes, and the version numbers didn't give an indication of when this change
had happened[^30]. I eventually figured out where the change had happened,
explained the history of the exporter (that again, I had written years earlier)
and proposed three solutions, each with a corresponding Pull Request: 1) return
the YAML exporter to it's previous output[^27], 2) duplicate the old exporter
under a new name[^28], or 3) merge my plugin system, which would allow me to
write my own plugin, and solve the problem myself. I was denied on all three,
and told that I 'didn't understand the purpose or function of the YAML
exporter'[^31] (yes, of the plugin I'd written[^37]). The best I got was that
they would reconsider what rose to the level of a "breaking change" when
dealing with versioning[^32].


### I Walk Away

The combined experience left me feeling very frustrated: *jrnl* was broken (to
me) and all my efforts to fix it were forably rebuffed.

When I tried to express my frustrations at my inability to get a "working"
version of *jrnl*, I was encouraged to take a mantal health break. While I
appreciate the awareness of mental health, stepping away wouldn't be helpful in
this particlar case because the nothing would happen to fix my broken tooling
(the cause of my frustrations). It seemed like the "right words"(tm) someone
had picked up at a workshop, but the same workshop figured that the "right
words"(tm) would solve everything without requiring a deeper look or deeper
changes.

So I took my leave. I've been running an outdated version (v2.6) ever since,
and because of the strictness of the Poetry metadata[^29], I can't run it on
anything newer than Python 3.9.


### I Return (Sort Of); The Future and My Fears

So this marks my return. My "mental health break" is over. As I realize I can
only change myself (and not others), I will do the work to fix the deeper
issues (e.g. broken Pelican exports, lack of "modern" Python support) by
managing my own fork. And so that is the work I'll do.

Looking forward, if I'm the only one that uses my fork, that would be somewhat
disappointing, but also fine. After all, I write software, first and foremost,
for my own usecase and offer it to others as a gift. On the other hand, if a
large part of the community moves here, I worry about being able to shepherd
that community any better than the one I am leaving.

I worry too that either due to there being conflict at all, or that all of my
writings are publically displayed, others will think less of my work or myself
because of the failings they see there. It is indeed very hard to get through a
disagreement like this without failing in some degree.

But it seems better to act, than to suffer in silence.


## A Thank You

Thank you to all those who have worked to make *jrnl* as successful as it has
been to date.

If you've gotten this far, thank you for reading this all. I hope you will join
me, and I hope your experiences with *minchin.jrnl* are positive!

*The header image was generated locally by Standard Diffusion XL.*


## Footnotes

[^1]: October 18, 2021 todo item: "fork jrnl"
[^2]: main landing page at [jrnl.sh](https://jrnl.sh/en/stable/), code at
    [jrnl-orl/jrnl on GitHub](https://github.com/jrnl-org/jrnl), and
    [jrnl](https://pypi.org/project/jrnl/) on PyPI
[^3]: <https://github.com/jrnl-org/jrnl/tree/v2.6>
[^4]: this varies by OS, so run ``jrnl --list`` to see where yours is stored.
[^5]: [Pull Request #1115](https://github.com/jrnl-org/jrnl/pull/1115)
[^6]: I've started using [Obsidian](https://obsidian.md/) to take notes on my
    workstation and on my phone, and find it incredible. The backend format
    remains Markdown with basically yaml front matter, but the format is
    slightly different from Pelican, and exported file layout differs.
[^7]: The initial draft of this post was written before the v4 release, when
    there was talk of changing how the journal files were kept. v4 has since
    been released, and I'm unclear if that change ever happened, or what
    "breaking change" occurred that bumped the version number from 3 to 4
    generally. In any case, if they change their format, with the plugin system
    it becomes fairly trivial to add a format-specific importer.
[^8]: also: tiny file size, easy to put under version control, no proprietary
    format or data lock-in, portability across computing platforms, and
    generally are human readable
[^9]: includes limitations on embedded text formating, storing pictures,
    videos, or sound recordings, and lacking standardized internal metadata
[^10]: Markdown has several variants and many extensions. If you're starting
    out, I recommend looking at the [CommonMark
    specification](https://spec.commonmark.org/0.30/). Note however that
    Markdown was originally designed as a shortcut for creating HTML documents,
    and so has no built in features for managing groups of Markdown documents.
    It is also deliberately limited in the formating options available, while
    officially supporting raw HTML as a fallback for anything missing.
[^11]: ReST is older than Markdown and has always had a [full
    specification](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html).
    It was originally designed for the Python language documentation, and so
    was designed from the beginning to deal with the interplay between several
    text documents. Sadly, it doesn't seem to have been adopted much outside of
    the Python ecosystem.
[^12]: [version 2.3.1
    license](https://github.com/jrnl-org/jrnl/blob/v2.3.1/LICENSE) (MIT);
    [version 2.4
    license](https://github.com/jrnl-org/jrnl/blob/v2.4/LICENSE.md) (GPLv3),
    released April 18, 2020.
[^13]: as I detailed [at the
    time](https://github.com/jrnl-org/jrnl/pull/918#issuecomment-619683220).
    But the [issue](https://github.com/jrnl-org/jrnl/pull/918) (#918)
    announcing the change was merged within 20 minutes of being opened, so I'm
    not sure anything I could have said would have changed their minds.
[^14]: this can and should be flushed out into a full blog post. But another day.
[^15]: and I work on Windows. And I work with Python because Python has had
    good Windows support.
[^16]: <https://pip-tools.readthedocs.io/en/latest/>
[^17]: [jrnl-org/jrnl's Code of
    Conduct](https://github.com/jrnl-org/jrnl/blob/c7b204022a0201a174244163c6ebfa107e8906d2/CODE_OF_CONDUCT.md):
    the *Contributor Code of Conduct*.
[^18]: I imagine in the issue tracker for the project.
[^19]: I think he got a job with or founded a startup, and I suspect he
    probably moved continents.
[^20]: In the intervening time, I ended up releasing personal forks of several
    Pelican plugins. The process is no longer new or scary, but still can be a
    fair bit of work. And that experience has given me the confidence to go
    forward with this fork.
[^21]: February 16, 2018
[^22]: July 5, 2019; [my comment, at the
    time](https://github.com/jrnl-org/jrnl/issues/591#issuecomment-508821983)
[^23]: my (pending) codename for these releases is ⚜ *Fluer-de-lis*. The
    reference is to the Lily, a flower that is a symbol of purity and rebirth.
[^24]: see [Pull Request #1216](https://github.com/jrnl-org/jrnl/pull/1216) and
    [Discussion #1006](https://github.com/jrnl-org/jrnl/issues/1006)
[^25]: [Issue #1065](https://github.com/jrnl-org/jrnl/issues/1065)
[^26]: in particular, Pelican could no longer find the metadata block and
    instead rendered the text of each entry as if it was a code block.
[^27]: I'm sure I wrote the code to do this, but can't find the Pull Request at
    the moment. Maybe I figured the suggestion wouldn't go anyway.
[^28]: [Pull Request #1337](https://github.com/jrnl-org/jrnl/pull/1337/files)
[^29]: <https://github.com/jrnl-org/jrnl/blob/v2.6/pyproject.toml#L25>
[^30]: perhaps because I was looking for a *breaking change* rather than a *bug
    fix*.
[^31]: [this
    comment](https://github.com/jrnl-org/jrnl/pull/1337#discussion_r711646511)
    and [this
    one](https://github.com/jrnl-org/jrnl/pull/1337#discussion_r730316274), in
    particular. I can't find those exact quoted words, but that was the
    sentiment I was left with.
[^32]: [this comment](https://github.com/jrnl-org/jrnl/pull/1337#discussion_r711646511)
[^33]: So no *make*. But [Invoke](https://www.pyinvoke.org/), written in
    Python, works well for many of *make*'s use cases.
[^34]: and still today
[^35]: [Pull Request #110](https://github.com/jrnl-org/jrnl/pull/110), dated
    November 27, 2013
[^36]: but likely recorded in the issue tracker
[^37]: [Pull Request #258](https://github.com/jrnl-org/jrnl/pull/258), opened
    July 30, 2014.
