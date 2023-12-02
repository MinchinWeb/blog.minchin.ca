Title: Website Redesign Time?
Date: 2023-11-13 17:23
Author: Wm. Minchin
Tags: Homepage Redesign, blog, Minchin.ca
Image: images/2016/minchindotca-theme-article.png

I've started toying with redesigning my blog. The last time I did that was ~[7
years ago]({filename}20160912-i-redesigned-my-blog.md), when I moved the blog
off of Blogger to run on Pelican. The system has worked well enough, but a few
ideas have started tickling around the back of my head.

The reasons to *not* do this are clear enough: it's an easy project to start,
but long, hard work to bring the new version up to feature parity with the old.
Also, as I wrote in 2016:

> Why You Shouldn’t Do This
>
> To start with, you shouldn't do the same thing [i.e. redesigning your blog
> and moving it from one backend provider to another]. In a word, **time**.
> I've spent numerous evenings over the last <del>two</del> four months to get
> this done. This has proved far more than a simple weekend project. If you're
> time available for your blog is limited (which it almost always is), and your
> blogging system isn't broken at some fundamental level, your time is probably
> better spend creating content (i.e. writing blog posts) than rebuilding your
> backend.

As a general rule, we have to be careful we don't spend more time tinkering
with our tools (in this case, my blog) than actually using them.

But here are some of the reasons I'm considering investing the effort anyway:

### Sidenotes

I find in my writing, I consistently like to add asides to the main body of
text; usually I put these in parathesis, and you just get to read them inline
(see, like this!). Some of these things, by rights, could be footnotes, but
these notes are most useful when those in context to their anchor, and
footnotes tend to disappear down...somewhere as the article gets longer.
"Sidenotes", or margin notes, much like you might write in the margin of a book
as you study it yourself, seem like a wonderful solution. There is a wonderful
implementation called [Tufte CSS](https://edwardtufte.github.io/tufte-css/),
inspired by the (print) works of Edward Tufte, who tended to include large
outside margins and copious notes. As [another summed it
up](https://bookdown.org/yihui/rmarkdown/tufte-handouts.html):

> Tufte’s style is known for its extensive use of sidenotes, tight integration
> of graphics with text, and well-set typography.

and provided a nice example:

![Tufte Example]({static}images/2023/tufte-overview.png)

This idea of sidenotes is probably the biggest thing pushing me to a redesign
rather than a "simple" change to the existing design, as the current design
lacks the right margin to insert these notes into. Also, I haven't found a
great way of dealing with these on smaller, mobile screens.

If we cross the bridge of having to review the website's horizontal
partitioning, it seems worthwhile to consider some other changes, even if their
implementation doesn't happen day one.

### A "Fat" Footer

Common on corporate sites for some time now is the idea of a "fat" header menu
or a "fat" footer. The more traditional design idea was to have a website menu,
but only have a handful (or two) of items in it, and items beyond that either
fell into sub-menus (sometimes, but not always, displayed on a fly-out;
sometimes only displayed on the corresponding subpage), or would only be found
as a link on a sitemap (which seem much less common than in previous times). As
the top menu grew fat enough, it seemed to get to a point were it was too much
to put at the top of the page, and so a trim menu remained up top and a larger
collection of links was added to the page footer.

My current site has a very trim top menu, and very small footer, limited mostly
to attribution (e.g. the author, the theme, etc).

But a fat footer seems like a good way to help the discoverability of my
various online projects. In particular, I would like to add deeper links in my
geneology pages (e.g. to family lines) and to have a place to list my many
somewhat (mostly Python) projects. For example, I currently have 13 [Pelican
plugins]({tag}Pelican Plugins) on the go, but no obvious place to have that
list.

### Colours, and a "Paper Feel"



- sidenotes/endnotes
- "fat" footer
    - discovery of my Python projects, like my Pelican plugins
- mobile vs desktop design
- colours??
    - light writing on dark
    - font choice
- paper feel
    - postmarks
    - line length
- push Pelican to do crazy things
    - CommonMark Reader
- move from JS, from Bootstrap
    - flexbox?
    - columns
    - HTML5, semantic web
        - <div> vs <nav>, <article>
- integration with the rest of my site
    - technical documentation
    - genealogy


