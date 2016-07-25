Title: Free Hosting for Static Websites
Date: 2012-03-23 22:10
Author: Wm. Minchin
Tags: Git, GitHub, Web Hosting, Web Services
Slug: free-hosting-for-static-websites

In addition to my blog, I have a couple of static webpages that I host
at [Minchin.ca](http://minchin.ca/). Sadly, they've been a little
neglected of late, but I've enjoyed being able to put a few pages and
play around with HTML. Since I don't run any ads on them, or run a
business from them, I've trying to avoid having to pay for hosting. In
the almost 5 years they've been online, I've managed to find a place to
host them for free: first at Google Pages, and then at Microsoft Office
Small Business. Google closed 'Pages' in 2009 and Microsoft's offering
will start charging for hosting the end of next month. So I've been
looking for a new place to host them. Today I completed the move to
[GitHub](http://www.github.com/)!

Github offers hosting for static webpages for free. I think the idea is
to provide developers and programmers a space to showcase their open
source programming projects, but you can use it from other personal
websites too. To get up and running with GitHub:

1. Create a user account on [GitHub.](http://www.github.com/)
2. If you're not familiar with Git, read through the [GitHub Help
pages](http://help.github.com/set-up-git-redirect). This will walk you
through installing any software you might need to work with GitHub.
3. [Create a repository](http://help.github.com/create-a-repo) named
*{your_username}.github.com*
4. Push the static files of your website to your new repository.

    1.  Your page will go live at *http://{your_username}.github.com*
    2.  If you want to use a different web address (and you own the domain),
        include a file called *CNAME* that lists that other web address in
        your repository. You will also need to create a A record for that
        domain pointing to `207.97.227.245` (Get your domain name registrar
        to help you with that one).

5. You might have to wait 10 minutes for it to go live...
6. You have a free website!

While I admit that using GitHub might seem a little involved, it is
rather simple (for web hosting), it works, and it's free! And I think
they'll continue to host my page for the foreseeable future. If you get
stuck, GitHub has a [good introduction to GitHub
Pages](http://pages.github.com/).
