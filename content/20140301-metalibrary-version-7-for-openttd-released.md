Title: MetaLibrary 7 for OpenTTD released
Date: 2014-03-01 22:43
Modified: 2015-08-14 8:11
Author: Wm. Minchin
Tags: MetaLibrary, NoAI, OpenTTD, releases
Category: MetaLibrary
Alias: 2014/03/metalibrary-version-7-for-openttd.html
Slug: metalibrary-7-for-openttd

*[MetaLibrary](http://minchin.ca/openttd-metalibrary/)* moves forward
again!

Building off my recent announcement that [documentation is now
live]({filename}20140201-metalibrary-documentation-live.md),
I have completed a fairly major update to *MetaLibrary*.

To recap, *MetaLibrary* is a collection of code I've written to simplify
writing an AI for [OpenTTD](http://www.openttd.org/), a remake of my
childhood favorite, Transport Tycoon.

This update particularly focused on adding robustness to the Ship
Pathfinder. To that end, I wrote *Lakes* as a replacement for *Waterbody
Check*. Both serve the same purpose of determining if two tiles are
within the same waterbody, i.e. if a ship could sail between the two
tiles. What sets *Lakes* apart from its predecessor is *Lakes* maintains
a 'memory' of the tiles it has already considered, therefore increasing
the speed of subsequent requests. Subsequent requests on an already
checked route run in the order of 4 ticks, or about half of a game day.

*Lakes* has already seen a ten-fold increase in speed, although it, at
least for the first run, is slower than the old *Waterbody* *Check*. New
versions of *MetaLibrary* will likely continue to see speed ups and
tweaks to *Lakes*.

Other improvements include:

-   Ship Pathfinder now uses Lakes rather than WaterBodyCheck
-   Ship Pathfinder now makes sure every point is in the same waterbody
    before adding it to the path
-   WaterBodyCheck is now deprecated in favour of Lakes
-   [Documentation for
    MetaLibrary](http://minchin.ca/openttd-metalibrary/) is now online
    at Minchin.ca
-   Fix array creation bugs in Array.Create2D(), Array.Create3D()
-   Added `Array.RemoveDuplicates(Array)`
-   Added `Array.ToAIList(Array)`
-   Added `Extras.MinDistance(TileID, TargetArray)`; can be used as a
    valuator
-   Split Constants from Extras (file only, function access remains the
    same)
-   Split Industry from Extras (file only, function access remains the
    same)
-   Split Station from Extras (file only, function access remains the
    same)
-   Bumped maximum Log `Debug_Level` to 8
-   Added separate Changelog file
-   Rename `Readme.txt` to `Readme.md`
-   Update requirement to Fibonacci Heap, v.3
-   Automated creation of tar files for upload to BaNaNaS
-   Automated translation for the Game Script version

The [forum thread for *MetaLibrary*
discussion](http://www.tt-forums.net/viewtopic.php?f=65&t=57903) is on
TT-Forums, the [code for
*MetaLibrary*](https://github.com/MinchinWeb/openttd-metalibrary/) is
available on GitHub, the [documentation for
*MetaLibrary*](http://minchin.ca/openttd-metalibrary/) is now online at
Minchin.ca, and *MetaLibrary* can be downloaded from BaNaNaS ([AI
version](http://bananas.openttd.org/en/ailibrary/), [GS
version](http://bananas.openttd.org/en/gslibrary/)) or the in-game
downloader (recommended).
