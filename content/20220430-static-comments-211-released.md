title: Static Comments Plugin 2.1.1 for Pelican Released
date: 2022-04-30 14:17
tags: Pelican, Pelican Plugins, Releases, Python, Pelican Themes, Static Comments
Category: Pelican Plugins

*Static Comments* is a plugin for [Pelican](http://docs.getpelican.com/),
a static site generator written in Python. It is meant as a drop in replacement
for the [Pelican Comment System](https://github.com/Scheirle/pelican_comment_system).

*Static Comments* allows you to have a comment section on your Pelican blog,
while maintaining your blog as a completely static webpage and without relying
on any external services or servers; just an email address is required.
Comments are stored as text files, similiar in structure to Pelican articles.
This gives you complete control over the comments appearing on your site and
allows you to back them up with the rest of your site.

## This Release

This release takes the existing *Pelican Comment System* codebase and upgrades
it to work with Pelican 4 (and should continue to work with Pelican 3). A few
changes are needed in your configuration, but no changes to your comments files
should be needed.

## Installation

The simplest way to install the Python code of *Static Comments* is to use `pip`:

~~~sh
pip install minchin.pelican.plugins.static-comments --upgrade
~~~

If you are using Pelican 4.5+, the plugin will automatally be loaded (although
not activated).

If you are an earlier version of Pelican, or non-namespace plugins, you will
need to add the auto-loader to your list of plugins:

```python
# pelicanconf.py

PLUGINS = [
    # others
    "minchin.pelican.plugins.autoloader",
]
```

Activate the plugin by adding the following line to your `pelicanconf.py`:

```python
# pelicanconf.py

PELICAN_COMMENT_SYSTEM = True
```

and then set the email you want to receive comment emails at:

```python
# pelicanconf.py

PELICAN_COMMENT_SYSTEM_EMAIL_USER = "your.email"
PELICAN_COMMENT_SYSTEM_EMAIL_DOMAIN = "gmail.com"
```

Finally, modify the `article.html` of your theme (if your theme doesn't
support *Static Comments* out of the box) to both display comments already
submitted and to have a comment submission form. The sample submission form works
by using JavaScript to convert the form contents (the commenter's name, site,
and comment body) to an email the user then sends to you. Note, this is an
example of the code you might use for your theme, but please feel free to
modify it to suit your needs.

```jinja+html
{% macro comments_styles() %}
{% if PELICAN_COMMENT_SYSTEM %}
{# NOTE:
 # Instead of using this macro copy these styles in your main css file
 # This marco is only here to allow a quickstart with nice styles
 #}
<style>
#pcs-comment-form input,
#pcs-comment-form textarea {
    width: 100%;
}
#pcs-comment-form-display-replyto {
    border: solid 1px black;
    padding: 2px;
}
#pcs-comment-form-display-replyto p {
    margin-top: 0.5em;
    margin-bottom: 0.5em;
}
#pcs-comments ul {
    list-style: none;
}
#pcs-comments .comment-left {
    display: table-cell;
    padding-right: 10px;
}
#pcs-comments .comment-body {
    display: table-cell;
    vertical-align: top;
    width: 100%;
}
</style>
{% endif %}
{% endmacro %}

{% macro comments_form() %}
{% if PELICAN_COMMENT_SYSTEM %}
<section>
    <form id="pcs-comment-form" action="#">
        <legend>Add a Comment</legend>
        <input type="hidden" id="pcs-comment-form-input-replyto">
        <fieldset>
            <label for="pcs-comment-form-input-name">Name</label>
            <input  id="pcs-comment-form-input-name" type="text" placeholder="Enter your name or nickname" />
        </fieldset>
        <fieldset>
            <label for="pcs-comment-form-input-website">Website</label>
            <input  id="pcs-comment-form-input-website" type="text" placeholder="Enter your website (optional)" />
        </fieldset>
        <fieldset>
            <label   for="pcs-comment-form-input-textarea">Your Comment</label>
            <textarea id="pcs-comment-form-input-textarea" rows="5" style="resize:vertical;" placeholder="Your comment"></textarea>
            <p>You can use the <a href="https://en.wikipedia.org/wiki/Markdown">Markdown</a> syntax to format your comment.</p>
            <div style="display: none; " id="pcs-comment-form-display-replyto"></div>
        </fieldset>

        <button type="submit"
                id="pcs-comment-form-button-submit"
                {# Piwik Track click on comment button
                onclick="javascript:_paq.push(['trackEvent', 'comment', '{{ article.title }}', document.getElementById('pcs-comment-form-input-textarea').value]);" #}
                >Post via email</button>

        {% if PELICAN_COMMENT_SYSTEM_FEED and article %}
            <a href="{{ SITEURL }}/{{ PELICAN_COMMENT_SYSTEM_FEED|format(article.slug) }}">
                Comment Atom Feed
            </a>
        {% endif %}
    </form>
</section>
{% endif %}
{% endmacro %}

{% macro comments_with_form() %}
{% if PELICAN_COMMENT_SYSTEM %}
<section id="pcs-comments">
    <header>
        <h2>Comments</h2>
        <hr/>
    </header>
    {% if article.comments %}
        <ul>
        {% for comment in article.comments recursive %}
            <li id="comment-{{comment.slug}}">
                <div class="comment-left">
                    <img    src="{{ SITEURL }}/{{ comment.avatar }}"
                            alt="Avatar"
                            height="{{ PELICAN_COMMENT_SYSTEM_IDENTICON_SIZE }}"
                            width="{{ PELICAN_COMMENT_SYSTEM_IDENTICON_SIZE }}">
                </div>
                <div class="comment-body">
                    <div style="float:right;">
                        <a role="button" href="{{ SITEURL }}/{{ article.url }}#comment-{{comment.slug}}" rel="bookmark" title="Permalink to this comment">Permalink</a>
                        <button onclick="CommentSystem.setReply('{{comment.slug | urlencode}}', '{{comment.author | urlencode}}');">Reply</button>
                    </div>
                    <h4>
                        {% if comment.metadata['website'] %}
                            <a href="{{comment.metadata['website']}}">{{ comment.author }}</a>
                        {% else %}
                            {{ comment.author }}
                        {% endif %}
                    </h4>
                    <p>
                        Posted on
                        <time datetime="{{ comment.date.isoformat() }}" title="{{ comment.date.isoformat() }}">{{ comment.locale_date }}</time>
                    </p>
                    <div class="pcs-comment-content" {# class used as id in comments.js#}>
                        {{ comment.content }}
                    </div>
                    {% if comment.replies %}
                        <hr>
                        <ul>
                            {{ loop(comment.replies) }}
                        </ul>
                    {% endif %}
                </div>
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>There are no comments yet.</p>
    {% endif %}
    {{ comments_form() }}
</section>
{% endif %}
{% endmacro %}


{% macro comments_js(user, domain, includeJquery=True) %}
{% if PELICAN_COMMENT_SYSTEM %}
    {% if includeJquery %}
        <script type="text/javascript" src="http://code.jquery.com/jquery-2.1.4.min.js"></script>
    {% endif %}
    <script type="text/javascript" src="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/js/comments.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            CommentSystem.email_user   = "{{ user }}";
            CommentSystem.email_domain = "{{ domain }}";
            CommentSystem.display_replyto_html = function(comment_content, article_slug, author) { 
                return ''
                    + '<button style="float:right;" onclick="CommentSystem.cancelReply(); return false;" title="Cancel the reply">'
                    +     '×'
                    + '</button>'
                    + '<p>This comment will be posted as a reply to \'<a title="'+comment_content+'" href="#comment-'+article_slug+'">'+author+'</a>\'</p>';
            };

            $('#pcs-comment-form').on("submit",
                function( event )
                {
                    event.preventDefault();
                    $(location).attr('href', CommentSystem.getMailtoLink("{{ article.slug }}"));
                }
            );
        });
    </script>
{% endif %}
{% endmacro %}

{% macro comments_quickstart(user, domain) %}
    {{ comments_styles() }}
    {{ comments_with_form() }}
    {{ comments_js(user, domain) }}
{% endmacro %}
```

## What A Comment File Looks Like

When a user submits a comment, you will get an email with the details. You then
take those details from your email and create a text file within your Pelican
site, one for each comment. By default, the plugin will look for comments in a
folder `comments` in your root content folder (probably the same one your have
your Pelican articles in), and then in subfolders that match the slug of the
article the comment applies to.

The actual comment file will look something like this:

```markdown
email: noreplay@blogger.com
date: 2019-07-15T12:20+01:00
author: Mahassine
replyto: comment-slug-2382md

Sample comment body.

<!-- content/comments/article-slug/comment-slug-2342.md -->
```

The `replyto` tag is only needed if this comment is indeed a reply to another
comment. The value of the `replyto` tag is the slug of the comment, which is
the filename plus the file extension, but not the period between them.

The comment files can be in any format Pelican is set up to read (typically
Markdown and ReStructed Text, but many others supported).

I realize that this is fairly involved to activate as far as Pelican plugins
go, so if you run into issues, please leave a comment on this post!

## Upgrading (from the Pelican Comment System)

Upgrading from the *Pelican Comment System* should be seemless, and should be
as simple as uninstalling the *Pelican Comment System* (and removing it from
your `pelicanconf.py`) and installing *Static Comments*.

~~~sh
pip uninstall pelican-comment-system
pip install minchin.pelican.plugins.static-comments --upgrade
~~~

Existing comments files should work out of the box, and the setting haven't
been renamed.

## Known Issues

- To get this to work, you'll need to update your theme (or find one, like
  [Seafoam](https://blog.minchin.ca/category/seafoam/), that works out of the
  box). I appologize for how involved this is, but Pelican doesn't have any
  framework for editing themes from plugins.
- The current setup requires JavaScript, and there probably isn't a great "no
  script" solution. As an alternative, you can ask people to just email you
  their comments directly and offer to post them. I actually do a version of
  this on my [Genealogy site](http://minchin.ca/genealogy/) and get a rather
  consistent stream of emails, so it may be a viable option.
- You have to manually add comments to your site, regenerate it, and reupload
  it before the comments will show on your site. This means that comments won't
  immediately show, and the the workflow may not be feasible if you have a high
  comment volume.
- The documentation that is on the Github repo has been reviewed, but may still
  be out of date in places. Please let me know if you notice any issues there.
- If you are moving your site to Pelican from another system, importing your
  existing comments can be rather involved. There is an included script for
  Blogger comments that I used myself, but because such imports tend to be
  one-offs, these scripts don't get checked that often and so could break if
  the export format changes. If you have a significant volume of comments you
  want to import, you may have to write your own script (which I'd be happy to
  include with the plugin if you send me a pull request!).

## Future Plans

At this point, the plugin seems feature complete. I expect future changes will
be about fixing code errors or to keep it working as Pelican progresses.

## Personal Thoughts

I'm excited to get this updated and out into the world. I'm a little sad that
the old *Pelican Comment System* seems to be no longer being updated, although
it looks like it got stuck halfway through a "version 2" complete rewrite, so
add this as another warning about ground up rewrites. But this is the wonder of
Open Source: I can take the existing codebase, fix the errors and issues, and
release a new working version back into the world.

There is also a more general question of whether comments are worth keeping
around. Considering that you're reading this, and I released this plugin, I
think we are both in agreement that the answer is "yes". I have definitely seen
a the number of comments posted to my blog drop over the years (this blog has
been up since 2006!), but I suspect that is mostly tied to lower traffic
volumes. As for comments generally, Twitter and Reddit I think provides proof
that people still want to add their two cents on things, and personally, I
would rather have the conversion here rather than on another site (like Reddit)
that I don't control and have the ability to backup that conversation.

Overall, I'm pretty satisfied with this solution. The biggest downside is that
comments don't post automatically and so can take some time to show as I have
to manually post them, but I think that tradeoff is worth not having to
maintain a separate server just for commenting.

As with all my plugins, if the *pelican-plugins* group wants to adopt these,
I'd be happy to have the community support there.
