Title: Push a Hg Repo to GitHub
Date: 2012-10-24 19:25
Author: Wm. Minchin
Tags: Git, GitHub, Mercurial
Slug: push-hg-repo-to-github

So the scenario is thus: There is a project that I want to contribute to
that is a Mercurial (Hg) repository (or 'repo' for short). I've taken a
liking to Git; [GitHub](http://www.github.com/) in particular with
[their new and beautiful Windows frontend](http://windows.github.com/).
So how do I take a remote Hg repo and push it to GitHub. As follows (the
following assumes you have a Ubuntu box available to play with, although
I imagine many Linux machines would work the same way):

-   So first, [create your repo on
    GitHub](https://github.com/repositories/new). You don't have to do
    anything more with it at this time, just make a note of its name.
-   Next, add your machine's RSA public key to GitHub. I won't go
    through that here, but if you walk through [GitHub's setup steps for
    Linux](https://help.github.com/articles/generating-ssh-keys), it
    will explain all of this.
-   Ok next, install Git and Mercurial:

        $ sudo apt-get install git mercurial

-   Next, we install a little program that will link Mercurial to Git

        $ sudo apt-get install python-setuptools
        $ sudo easy_install hggit

-   Now, create a folder as needed (for example, an 'hgrepo' folder in
    your home folder)

        $ cd ~
        $ mkdir hgrepo
        $ cd hgrepo

-   Now pull down the existing hg repo.

        $ hg clone http://web.address.of.hp.repo/repo-name

-   I might make a subfolder and put your repo there. That's alright.
    Move to that new directory.

        $ cd new-hg-repo-folder

-   Now we're going to add the info we need to push to GitHub

        $ cd .hg`

-   Find a file named "hgrc". Add the following lines:

        [path]
        git =
        git+ssh://git@github.com/your-username/your-new-github-repo.git

        [extensions]
        hggit =

    There will probably be a line in there pointing to your original hg
    repo. It's fine. Leave it there.

-   Now push your repo to GitHub!
    
        $ hg push git

If everything worked right, your repo should now be available on GitHub!

------------------------------------------------------------------------

One issue I didn't address was contributor names. See the [bottom of
this
page](https://confluence.atlassian.com/pages/viewpage.action?pageId=269982882)
for an example of how to fix that.

[This
page](http://hgtip.com/tips/advanced/2009-11-09-create-a-git-mirror/) on
*hg tip* was also very helpful.
