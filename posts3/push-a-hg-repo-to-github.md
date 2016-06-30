Title: Push a Hg Repo to GitHub
Date: 2012-10-25 01:25
Author: Minchin Web (noreply@blogger.com)
Tags: Git, GitHub, Mercurial
Slug: push-a-hg-repo-to-github

So the scenario is thus: There is a project that I want to contribute to
that is a Mercurial (Hg) repository (or 'repo' for short). I've taken a
liking to Git; [GitHub](http://www.github.com/) in particular with
[their new and beautiful Windows frontend](http://windows.github.com/).
So how do I take a remote Hg repo and push it to GitHub. As follows (the
following assumes you have a Ubuntu box available to play with, although
I imagine many Linux machines would work the same way):\

-   So first, [create your repo on
    GitHub](https://github.com/repositories/new). You don't have to do
    anything more with it at this time, just make a note of its name.
-   Next, add your machine's RSA public key to GitHub. I won't go
    through that here, but if you walk through [GitHub's setup steps for
    Linux](https://help.github.com/articles/generating-ssh-keys), it
    will explain all of this.
-   Ok next, install Git and Mercurial:

    </p>
    \

    <p>
    `$ sudo apt-get install git mercurial`

-   Next, we install a little program that will link Mercurial to Git

    </p>
    \

    `$ sudo apt-get install python-setuptools`

    <p>
    \$ sudo easy\_install hggit</code>

-   Now, create a folder as needed (for example, an 'hgrepo' folder in
    your home folder)

    </p>
    \

    `$ cd ~`

    \$ mkdir hgrepo\

    <p>
    \$ cd hgrepo</code>

-   Now pull down the existing hg repo.

    </p>
    \

    <p>
    `$ hg clone http://web.address.of.hp.repo/repo-name`

-   I might make a subfolder and put your repo there. That's alright.
    Move to that new directory.

    </p>
    \

    <p>
    `$ cd new-hg-repo-folder`

-   Now we're going to add the info we need to push to GitHub

    </p>
    \

    <p>
    `$ cd .hg`

-   Find a file named "hgrc". Add the following lines:

    </p>
    \

    `[path]`

    git =
    git+ssh://git@github.com/your-username/your-new-github-repo.git\

    \

    [extensions]\

    hggit =</code>

    \
    \

    <p>
    There will probably be a line in there pointing to your original hg
    repo. It's fine. Leave it there.

-   Now push your repo to GitHub!

    </p>
    \

    <p>
    `$ hg push git`

</p>
If everything worked right, your repo should now be available on GitHub!

\

------------------------------------------------------------------------

</p>
One issue I didn't address was contributor names. See the [bottom of
this
page](https://confluence.atlassian.com/pages/viewpage.action?pageId=269982882)
for an example of how to fix that.\

\

[This
page](http://hgtip.com/tips/advanced/2009-11-09-create-a-git-mirror/) on
*hg tip* was also very helpful.

<div class="feedflare">

</p>
[![](http://feeds.feedburner.com/~ff/MinchinWeb?i=Z5pcWoK1q-0:SJzh8aqCU-o:XhI0_UKdTUU)](http://feeds.feedburner.com/~ff/MinchinWeb?a=Z5pcWoK1q-0:SJzh8aqCU-o:XhI0_UKdTUU)
[![](http://feeds.feedburner.com/~ff/MinchinWeb?i=Z5pcWoK1q-0:SJzh8aqCU-o:4cEx4HpKnUU)](http://feeds.feedburner.com/~ff/MinchinWeb?a=Z5pcWoK1q-0:SJzh8aqCU-o:4cEx4HpKnUU)
[![](http://feeds.feedburner.com/~ff/MinchinWeb?d=yIl2AUoC8zA)](http://feeds.feedburner.com/~ff/MinchinWeb?a=Z5pcWoK1q-0:SJzh8aqCU-o:yIl2AUoC8zA)

<p>

</div>

![](http://feeds.feedburner.com/~r/MinchinWeb/~4/Z5pcWoK1q-0)

</p>

