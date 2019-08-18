title: PhotoSorter Python script 2.1.0 Released
date: 2017-08-28 15:16
tags: dropbox, python, releases
Category: Python

*Photosorter* is a little Python script to keep my photos from Dropbox organized.

It watches a *source directory* for modifications and moves new image files to
a *target directory* depending on when the photo was taken, using EXIF data and
creation date as a fallback. There is also an option to move existing photos.
<!-- read more -->

Directory and file names follow a simple naming convention
(``YYYY-MM/YYY_MM_DD/YYYY-MM-DD hh:mm:ss.ext``) that keeps everything neatly
organized. Duplicates are detected and ignored based on their SHA1 hash and
folder path. Photos taken in the same instant get de-duplicated by adding a
suffix (``-1``, ``-2``, etc) to their filenames.

The result looks somewhat like this::

    ├── 2013-01
    │   ├── 2013_01_05
    │   │   ├── 2013-01-05\ 13.24.45.jpg
    │   │   ├── 2013-01-05\ 14.25.54.jpg
    │   │   └── 2013-01-05\ 21.28.48-1.jpg
    │   ├── 2013_01_06
    │   │   ├── 2013-01-06\ 16.05.02.jpg
    │   │   ├── 2013-01-06\ 19.59.25.jpg
    │   │   ├── 2013-01-06\ 20.40.28.jpg
    │   │   └── 2013-01-06\ 21.14.38.jpg
    │   └── 2013_01_08
    │       └── 2013-01-08\ 11.45.51.jpg
    ├── 2013-02
    |   └─ ...
    ├── ...
    ├── 2013-12
    ├── 2014-01
    ├── 2014-02
    ├── ...
    ├── 2014-12
    ├── ...

I use ``C:\Users\[windows username]\Dropbox\Camera Uploads`` as the source
directory and ``Z:\Photos`` as the target. This allows me to move my photo from
Dropbox to a local drive, and merge them with the rest of my photo collection.

## Impletmentation Notes

I use a different folder set-up that Dan (in his original script) used. The one
I'm using matches the default folder set-up for my Canon camera.

## Installation

The easiest way to install the script is through pip::

~~~sh
pip install minchin.scripts.photosorter
~~~

## Requirements

The script's requirements will be automatically installed in the script is
installed via *pip* as recommended above. They can also be installed manually,
if required::

~~~sh
pip install argcomplete>=1.3.0
pip install exifread>=2.1.2
pip install watchdog>=0.8.3
~~~

## Usage

Watch `src_dir` and sort incoming photos into ``dest_dir``::

~~~sh
photosorter src_dir dest_dir
~~~

When you're done with it, ``Ctrl + C`` will end the program.

If you also want to move the existing files in ``src_dir`` (which are, by
default, ignored)::

~~~sh
photosorter src_dir dest_dir --move-existing
~~~

## Known Issues

- the tests do not currently run.
- matching (to provide de-duplication) is based on full filepaths matching.
  I.e. if the per day folder is renamed, the script will not look in the
  renamed folder for photo matches.
- Linux daemon setup is untested by myself.

## Changes

### 2.1.0 -- 2017-08-28

- also move MP4 files
- add changelog to readme

### 2.0.0 -- 2017-08-27

- move to ``minchin.scripts.photosorter`` namespace
- do releases via ``minchin.releaser``
- changed generated file folder layout
- add option to move existing files

## License

Distributed under the MIT license. See
[LICENSE.txt](https://raw.githubusercontent.com/MinchinWeb/minchin.scripts.photosorter/master/LICENSE.txt)
for more information.

## Credit

This script is a modified version of the one put together by
[Dan Bader](https://dbader.org/blog/how-to-store-photos-in-the-cloud-and-avoid-vendor-lock-in).
Thanks for providing a great template Dan!
