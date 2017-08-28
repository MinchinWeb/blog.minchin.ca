title: Image Process Plugin 1.1.3 for Pelican Released
date: 2017-05-27 16:00
tags: pelican, pelican plugins, releases, python
Category: Pelican Plugins
Updated: 2017-05-31 11:46

*Image Process* is a plugin for [Pelican](http://docs.getpelican.com/),
a static site generator written in Python.

*Image Process* let you automate the processing of images based on their
class attribute. Use this plugin to minimize the overall page weight and
to save you a trip to Gimp or Photoshop each time you include an image
in your post.

*Image Process* also makes it easy to create responsive images using the
new HTML5 `srcset` attribute and `<picture>` tag. It does this by
generating multiple derivative images from one or more sources.
<!-- read more -->

*Image Process* will not overwrite your original images.

*Image Process* is used by
[this blog's theme](https://github.com/MinchinWeb/seafoam) to resize the source
images so they are the correct size for thumbnails on the main index page and
the larger size they are displayed at on top of the articles.

## This Release

This post is up because version 1.1.3 of the plugin has been released and posted
[PyPI](https://pypi.org/project/minchin.pelican.plugins.image-process/). This
version was released because version 1.1.2, as posted to PyPI, was broken; among
other issues I couldn't generated my blog!

To upgrade simply use `pip`:

~~~sh
pip install minchin.pelican.plugins.image_process --upgrade
~~~

The bulk of the README is included below as I haven't posted it to the blog 
before. This plugin is a rather powerful, but as such is more involved to
configure than many other Pelican plugins.

A special thanks to the team at [Whisky Echo
Bravo](https://github.com/whiskyechobravo/image_process) who developed the code
of the plugin.

## Installation

The easiest way to install *Image Process* is through the use of pip.
This will also install the required dependencies automatically.

~~~sh
pip install minchin.pelican.plugins.image_process
~~~

Then, in your `pelicanconf.py` file, add `Image Process` to your list of
plugins:

~~~python
PLUGINS = [
            # ...
            'minchin.pelican.plugins.image_process',
            # ...
          ]
~~~

You will also need to configure your desired transformations (see
*Usage* below) and add the appropriate class to images you want
processed.

## Requirements

*Image Process* requires Beautiful Soup, Pillow, Six, and Pelican. All
these can be manually installed with pip:

~~~sh
pip install pillow beautifulsoup4 six pelican
~~~

If you encounter errors while processing JPEG files (on Linux), you may need to
install the JPEG development library:

~~~sh
pip uninstall pillow
apt-get install libjpeg-dev
pip install pillow
~~~

## Usage

*Image Process* scans your content for `<img>` tags with special
classes. It then maps the classes to a set of image processing
instructions, computes new images and modifies HTML code according to
the instructions.

### Define transformations

The first step in using this module is to define some image
transformations in your Pelican configuration file. Transformations are
defined in the `IMAGE_PROCESS` dictionary, mapping a transformation name
to a list of operations. There are three kinds of transformations: image
replacement, responsive image and picture set.

#### Image replacement

The simplest image processing will replace the original image by a new,
transformed image computed from the original. You may use this, for
example, to ensure that all images are of the same size, or to compute a
thumbnail from a larger image:

~~~python
IMAGE_PROCESS = {
    'article-image': ["scale_in 300 300 True"],
    'thumb': ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
    }
~~~

These transformations tell *Image process* to transform the image
referred by the `src` attribute of an `<img>` according to the list of
operations specified and replace the `src` attribute by the URL of the
transformed image.

For consistency with the other type of transformations described below,
there is an alternative syntax for the processing instructions:

~~~python
IMAGE_PROCESS = {
    'thumb': {'type': 'image',
              'ops': ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
              }
    'article-image': {'type': 'image',
                      'ops': ["scale_in 300 300 True"],
                      }
    }
~~~

To apply image replacement to the images in your articles, you must add
them the special class `image-process-` followed by the name of the
transformation you wish to apply. For example, let\'s pretend you have
defined the transformation described above. If you write your content in
HTML or in Markdown, do something like this:

~~~html
<img class="image-process-article-image" src="/images/pelican.jpg"/>
~~~

In reStructuredText, use the `:class:` attribute of the `image` or the
`figure` directive:

~~~rst
.. image:: /images/pelican.png
   :class: image-process-article-image

.. figure:: /images/pelican.png
   :class: image-process-article-image
~~~

<div class="admonition note">

The reStructuredText reader will convert underscores (`_`) to dashes
(`-`) in class names. To make sure everything runs smoothly, do not use
underscores in your transformation names.

</div>

#### Responsive Images

You can use *Image process* to automatically generate a set of images
that will be selected for display by browsers according to the viewport
width or according to the device resolution. To accomplish this,
*Image process* will add a `srcset` attribute (and maybe a `media` and a
`sizes` attribute) to the `<img>` tag.

Note that the `srcset` syntax is currently not supported by all
browsers. However, browsers who do not support the `srcset` attribute
will fall back to a default image specified by the still-present `src`
attribute. See [Can I Use](http://caniuse.com/#feat=srcset) for the
current status on `srcset` support.

HTML5 supports two types of responsive image set. The first one is
device-pixel-ratio-based, selecting higher resolution images for higher
resolution devices; the second one is viewport-based, selecting images
according to the viewport width. If you want to know more about HTML5
responsive images, I recommend
[this
article](http://www.smashingmagazine.com/2014/05/14/responsive-images-done-right-guide-picture-srcset/)
for a gentle introduction to the `srcset` and `<picture>` syntaxes.

To tell *Image process* to generate a responsive image, add a
`responsive-image` transformation to your your `IMAGE_PROCESS`
dictionary, with the following syntax:

~~~python
IMAGE_PROCESS = {
    'crisp': {'type': 'responsive-image',
              'srcset': [('1x', ["scale_in 800 600 True"]),
                         ('2x', ["scale_in 1600 1200 True"]),
                         ('4x', ["scale_in 3200 2400 True"]),
                         ],
               'default': '1x',
             },
    'large-photo': {'type': 'responsive-image',
                    'sizes': '(min-width: 1200px) 800px, (min-width: 992px) 650px, \
                              (min-width: 768px) 718px, 100vw',
                    'srcset': [('600w', ["scale_in 600 450 True"]),
                               ('800w', ["scale_in 800 600 True"]),
                               ('1600w', ["scale_in 1600 1200 True"]),
                               ],
                    'default': '800w',
                   },
    }
~~~

The `crisp` transformation is an example of a transformation enabling
device-pixel-ratio-based selection. The `srcset` is a list of tuple,
each tuple containing the image description (`'1x'`, `'2x'`, etc.) and
the list of operations to generate the derivative image from the
original image (the original image is the value of the `src` attribute
of the `<img>`). Image descriptions are hints about the resolution of
the associated image and must have the suffix `x`. The `default` names
the image to use to replace the `src` attribute of the image. This is
the image that will be displayed by browsers that do not support the
`srcset` syntax.

The `large-photo` transformation is an example of a transformation
enabling viewport-based selection. The `sizes` contains a rule to
compute the width of the displayed image from the width of the viewport.
Once the browser knows the image width, it will select an image source
from the `srcset`. The `srcset` is a list of tuple, each tuple
containing the image description (`'600w'`, `'800w'`, etc.) and the list
of operations to generate the derivative image from the original image
(the original image is the value of the `src` attribute of the `<img>`).
Image descriptions are hints about the width in pixels of the associated
image and must have the suffix `w`. The `default` names the image to use
to replace the `src` attribute of the image. This is the image that will
be displayed by browsers that do not support the `srcset` syntax.

In the two examples above, the `default` is a string referring to one of
the images in the `srcset`. However, the `default` value could also be a
list of operations to generate a different derivative image.

To make the images in your article responsive, you must add them the
special class `image-process-` followed by the name of the
transformation you wish to apply, exactly like you would do for the
image replacement case, described above. So, if you write your content
in HTML or in Markdown, do something like this:

~~~html
<img class="image-process-large-photo" src="/images/pelican.jpg" />
~~~

In reStructuredText, use the `:class:` attribute of the `image` of the
`figure` directive:

~~~rst
.. image:: /images/pelican.png
   :class: image-process-large-photo

.. figure:: /images/pelican.png
   :class: image-process-large-photo
~~~

#### Picture Set

*Image process* can be use to generate the images used by a `<picture>`
tag. The `<picture>` syntax allows for more flexibility in providing a
choice of image to the browser. Again, if you want to know more about
HTML5 responsive images, see [this
article](http://www.smashingmagazine.com/2014/05/14/responsive-images-done-right-guide-picture-srcset/)
for a gentle introduction to the `srcset` and `<picture>` syntaxes.

To tell *Image process* to generate the images for a `<picture>`, add a
`picture` entry to your `IMAGE_PROCESS` dictionary with the following
syntax:

~~~python
IMAGE_PROCESS = {
  'example-pict': {'type': 'picture',
                   'sources': [{'name': 'default',
                                'media': '(min-width: 640px)',
                                'srcset': [('640w', ["scale_in 640 480 True"]),
                                           ('1024w', ["scale_in 1024 683 True"]),
                                           ('1600w', ["scale_in 1600 1200 True"]),
                                           ],
                                'sizes': '100vw',
                                },
                               {'name': 'source-1',
                                'srcset': [('1x', ["crop 100 100 200 200"]),
                                           ('2x', ["crop 100 100 300 300"]),
                                           ]
                                }
                               ],
                   'default': ('default', '640w'),
                   },
  }
~~~

Each of the `sources` entry is very similar to the `responsive image`
describe above. Here, each source must have a `name`, which will be used
to find the URL of the original image for this source in your article.
The source may also have a `media`, which contains a rule used by the
browser to select the active source. The `default` names the image to
use to replace the `src` attribute of the `<img>` inside the
`<picture>`. This is the image that will be displayed by browsers that
do not support the `<picture>` syntax. In this example, it will use the
image `640w` from the source `default`. A list of operations could have
been specified instead of `640w`.

To generate a responsive `<picture>` for the images in your articles,
you must add to your article a pseudo `<picture>` tag that looks like
this:

~~~html
<picture>
    <source class="source-1" src="/images/pelican-closeup.jpg"></source>
    <img class="image-process-example-pict" src="/images/pelican.jpg" />
</picture>
~~~

Each `<source>` tag maps a source name (the `class` attribute) to a file
(the `src` attribute). The `<img>` must have the special class
`image-process-` followed by the name of the transformation you wish to
apply. The file referenced by the `src` attribute of the `<img>>` will
be used as the special `default` source in your transformation
definition.

The pseudo `<picture>` tag above can be used in articles written in
HTML, Markdown or restructuredText. In reStructuredText, however, you
can also use the `figure` directive to generate a `<picture>`. The
figure image file will be used as the special `default` source; other
sources must be added in the the legend section of the `figure` as
`image` directives. The figure class must be `image-process-` followed
by the name of the transformation you wish to apply, while the other
images must have two classes: `image-process` and the name of the source
they provide an image for:

~~~rst
.. figure:: /images/pelican.png
   :class: image-process-large-photo

    Test picture

    .. image:: /images/pelican-closeup.jpg
       :class: image-process source-1
~~~

The images in the legend section that are used as source for the
`<picture>` will be removed from the image legend, so that they do not
appear in your final article.

Transformations
---------------

Available operations for transformations are:

crop *top* *left* *right* *bottom*

:   Crop the image to the box (*left*, *top*)-(*right*, *bottom*).
    Values can be absolute (a number) or relative to the size of the
    image (a number followed by a percent sign `%`).

flip\_horizontal

:   Flip the image horizontally.

flip\_vertical

:   Flip the image vertically.

grayscale

:   Convert the image to grayscale.

resize *width* *height*

:   Resize the image. This operation does *not* preserve the image
    aspect ratio. Values can be absolute (a number) or relative to the
    size of the image (a number followed by a percent sign `%`).

rotate degree

:   Rotate the image.

scale\_in *width* *height* *upscale*

:   Resize the image. This operation preserves the image aspect ratio
    and the resulting image will be no larger than *width* x *height*.
    Values can be absolute (a number) or relative to the size of the
    image (a number followed by a percent sign `%`). If *upscale* is
    False, smaller images will not be enlarged.

scale\_out *width* *height* *upscale*

:   Resize the image. This operation preserves the image aspect ratio
    and the resulting image will be no smaller than *width* x *height*.
    Values can be absolute (a number) or relative to the size of the
    image (a number followed by a percent sign `%`). If *upscale* is
    False, smaller images will not be enlarged.

blur

:   Apply the `pillow.ImageFilter.BLUR` filter to the image.

contour

:   Apply the `pillow.ImageFilter.CONTOUR` filter to the image.

detail

:   Apply the `pillow.ImageFilter.DETAIL` filter to the image.

edge\_enhance

:   Apply the `pillow.ImageFilter.EDGE_ENHANCE` filter to the image.

edge\_enhance\_more

:   Apply the `pillow.ImageFilter.EDGE_ENHANCE_MORE` filter to the
    image.

emboss

:   Apply the `pillow.ImageFilter.EMBOSS` filter to the image.

find\_edges

:   Apply the `pillow.ImageFilter.FIND_EDGES` filter to the image.

smooth

:   Apply the `pillow.ImageFilter.SMOOTH filter` to the image.

smooth\_more

:   Apply the `pillow.ImageFilter.SMOOTH_MORE` filter to the image.

sharpen

:   Apply the `pillow.ImageFilter.SHARPEN` filter to the image.

You can also define your own operations; the only requirement is that
your operation should be a callable object expecting a `pillow.Image` as
its first parameter and it should return the transformed image:

~~~python
def crop_face(image):
    """Detect face in image and crop around it."""
    # TODO: Fancy algorithm.
    return image

IMAGE_PROCESS = {
    'face-thumbnail': [crop_face, "scale_out 150 150 True"]
    }
~~~

### Additional settings

#### Destination directory

By default, the new images will be stored in a directory named
`derivative/<TRANSFORMATION_NAME>` in the output folder at the same
location as the original image. For example if the original image is
located in the `content/images` folder. The computed images will be
stored in the `output/images/derivative/<TRANSFORMATION_NAME>`. All the
transformations are done in the output directory in order to avoid
confusion with the source files or if we test multiple transformations.
You can replace `derivative` by something else using the
`IMAGE_PROCESS_DIR` setting in your Pelican configuration file:

~~~python
IMAGE_PROCESS_DIR = 'derivees'
~~~

#### Force image processing

If the transformed image already exists and is newer than the original
image, the plugin assumes that it should not recompute it again. You can
force the plugin to recompute all images by setting
`IMAGE_PROCESS_FORCE` to `True` in your Pelican configuration file.

~~~python
IMAGE_PROCESS_FORCE = True
~~~

#### Selecting a HTML parser

You may select the HTML parser which is used. The default is the builtin
`html.parser` but you may also select `html5lib` or `lxml` by setting
`IMAGE_PROCESS_PARSER` in your pelican configuration file , e.g.:

~~~python
IMAGE_PROCESS_PARSER = "html5lib"
~~~

For details, refer to the [BeautifulSoup documentation on
parsers](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser).

#### File Encoding

You may select a different file encoding to be used by BeautifulSoup as
it opens your files. The default is `uft-8`.

~~~python
IMAGE_PROCESS_ENCODING = "uft-8"
~~~

## Known Issues

-   Pillow, when resizing animated GIF files, does not return an
    animated file
-   the `setup.py` file for this project does not run on Python 2.7.
    However, wheels of this project are \"universal\" and so can be
    generated by Python 3 and subsequently installed by Python 2.7.
-   test require access to the `pelican.tests` module, which isn\'t
    included in the pelican distribution on PyPI.
-   version 1.1.2, as uploaded to PyPI, is broken; use a different
    version. (see [issue
    #2](https://github.com/MinchinWeb/minchin.pelican.plugins.image_process/issues/2)
    for details)

### Credits

Pelican image in test data by Jon Sullivan. Source:
<http://www.pdphoto.org/PictureDetail.php?mat=&pg=5726>

Original Plugin developed by the team at [Whisky Echo
Bravo](https://github.com/whiskyechobravo/image_process).