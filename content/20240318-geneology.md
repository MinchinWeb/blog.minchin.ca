title: Genealogy -- March 2024 Update
date: 2024-03-18 20:54-0600
tags: Genealogy
category: Genealogy

It's been 6 years, but my [genealogy website](https://genealogy.minchin.ca/) has
finally been updated!

I'm not sure exactly why I stopped updating the site; I think it was mostly
that the generator ([Gigatrees](https://gigatrees.com/)) that I was using had
updated and broke my process (again...). At the time, I figured I had spent so
much time wrangling *Gigatrees* to work the way I wanted, that I could have
built my own site generator in that time! I did start
[that](https://github.com/MinchinWeb/exodus), but it's the dreaded re-write,
and died on the vine before it got usable. For now, I've pulled out the old
(working) version of *Gigatrees* out of my archives, and it at least generates
the site for now.

Another downside of the current process is that I run the *Gigatrees* output
through *Pelican* to get (final) generated site to match the style of the rest
of my site, but that step alone takes 45 minutes![^20240318-1]

The immediate push for picking this up again is that we are planning a Minchin
reunion[^20240318-2] for this summer, and I'd like to have the family history
in shape to be presented and updated at the reunion.

For now, the immediate things I've been working has been adding details from
the 1901 and 1911 census. It's proving a good way to confirm family
relationships and residences.

There are lots of things that I'm not sure are working, and so I should
probably look into making the most recent version of *Gigatrees* work, or get
serious about my own generator....

One positive it is proves how well a static website (like this) works. After
all, even after all this time left along, the site was still working!

To an update, sooner than 2030!

[^20240318-1]: In fairness, I'm running *Pelican* on over 10,000 source files,
and the output site is ~1 GB in size, so it's not like I expect it to be
instantaneous. But this is perhaps one of the times when "Python is slow"
actually applies.... Maybe while I waiting for one of these runs, I'll take to
profiling and speeding up *Pelican*.

[^20240318-2]: For the decendants of [Alex
Minchin](https://genealogy.minchin.ca/profiles/i17) (1890-1963).
