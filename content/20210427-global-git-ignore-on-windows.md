title: Global Git Ignore on Windows
date: 2021-04-28 21:16
Author: Wm. Minchin
Tags: Git, Windows

*Git* has an handy feature that you can get a system-wide *.gitignore* file. This
is particularly helpful to keep your project *.gitignore* files lean. However,
*Git* was originally built for Linux and sort of begrudgingly supports Windows,
which sometimes leads to oddities (like this):

**Where do you put your global *.gitignore* file on Windows to automatically
have it loaded?**
<!-- read more -->

Turns out it's ridiculously hard to find the answer; it's not
even on the official [Git docs](https://git-scm.com/docs/gitignore) or in
[GitHub
help](https://docs.github.com/en/github/getting-started-with-github/ignoring-files).
(Note I want the auto-loading location.)

In the end, I found the answer on an issue for a random project
([Broot Issue #212](https://github.com/Canop/broot/issues/212)):

> it is stated in the [Git] documentation that `$XDG_CONFIG_HOME/git/ignore`
> (or `$HOME/.config/git/ignore` if `$XDG_CONFIG_HOME` is not set) is the
> default value of core.excludesFile.

So, translated to Windows-ese, the answer is:

`C:\Users\<username>\.config\git\ignore`

`ignore` is the filename. The contents of the file are the same as any other
*.gitignore* file, except they will be applied to all your projects.

Hope this is helpful to someone else!
