Title: TRB (Transportation Research Board) Bibliography Style Updated for Word 2013/2016
Date: 2017-08-30 12:04
Author: Wm. Minchin
Tags: BibWord, Microsoft Word, TRB, Word 2013, Word 2016, releases
summary: Updating my version of the Transportation Research Board (TRB) reference style for use with the reference manager in Microsoft Word 2013 and 2016.

<div markdown=1 class="text-center">
![Word 2016 Reference Tab]({filename}images/2017/word-2016-reference-tab.png)
</div>

Seven years ago, I released a
[TRB (Transportation Research Board) Bibliography Style for Word 2010]({filename}20100707-trb-transportation-research-board-bibliography-style-for-word-20072010.md).
In the years since, that post has proved to be one of my most popular. However,
after the initial project I needed it for, I haven't needed it again, and so it
just let it lie. Then, internal changes in Word made the style un-usable with
the 2013 release. I was disappointed, but unsure of how to fix it.

So imagine my delight last week to receive an email, out of the blue, from
Maggie McNamara saying that she'd found a way to update the Bibiliography style
for Word 2013! As a bonus, she's also added DOI support (which I'd never heard
of when I first created the style).

### Installation

This updated version should work with all versions of Word after 2007 (although
I haven't personally been able to test them all). One thing that does change
between Word versions is where to put the XSL file:

Word 2007 (Windows)
:   `<winword.exe directory>\Bibliography\Style`

Word 2010 (Windows)
:   `<winword.exe directory>\Bibliography\Style`

Word 2010 (32 bit systems) (Windows)
:   `%programfiles%\Microsoft Office\Office14\Bibliography\Style`

Word 2016 and Office 365 (Windows)
:   `C:\Users\<currentusername>\AppData\Roaming\Microsoft\Bibliography\Style`, or
    `%AppData%\Microsoft\Templates\LiveContent\15\Managed\Word Document Bibliography Styles`

Word 2008 and Word 2011 (Mac OS)
:   To use the bibliography styles, right-click on Microsoft Word 2008 and
    select show package contents. Put the files in `Contents/Resources/Style/`.
    On most Macs with Microsoft Word 2008 this will be
    `/Applications/Microsoft Office 2008/Microsoft Word.app/Contents/Resources/Style/`

Word 2016 for Mac (version 15.17.0 and up)
:   `/Library/AppSupport/Microsoft/Office365/Citations/`

Office 365 (Mas OS)
:   `/Applications/Microsoft Word.app/Contents/Resources/Style`

### Example Output

In-text references are numeric, based on reference order.

Repeated references reuse the original number.

> ... Different pedestrian behaviour is associated not only
> with different physical characteristics but also the differing purpose
> of
> pedestrians (*1, 2*). Studies have been
> carried out for crowds associated with transportation systems (*3, 4,
> 5*), sporting and
> general spectator occasions (*6*), holy sites (*7, 8*), political
> demonstrations (*9*),
> and fire escapes (*10*).

The bibliography output is as follows:

> 1. Polus, A., J.L.
> Schofer, and A. Ushpi. Pedestrian flow and level of service.
> <i>Journal of
> Transportation Engineering Proceedings, ASCE</i>, Vol. 109, 1983, pp.
> 46-57.
>
> 2. Toshiyuki, A.
> Prediction system of passenger flow, in *Engineering for Crowd
> Safety*,
> Smith, R.A., and J.F. Dickie. Amsterdam: Elsevier, 1993, pp. 249-258.
>
> 3. Smith, R.A., and J.F.
> Dickie. *Engineering for Crowd Safety*. Amsterdam, 1993.
>
> 4. Tanaka, T. A study for
> performance based design of means of escape in fire, in <i>Fire Safety
> Science
> -- Proceedings of the 3rd International Symposium</i>, Cox, G., and B.
> Langford.
> Amsterdam: Elsevier, 1991, pp. 729-738.
>
> 5. Wikipedia
> contributors. List of metro systems. *Wikipedia, The Free
> Encyclopedia*,
> June 17, 2010.
> <http://en.wikipedia.org/w/index.php?title=List_of_metro_systems&oldid=368658114>.
> Accessed June 17, 2010.

### Known Issues

- in Word 2016, it lists the style as *First Edition*, and I haven't figured
  out how to change this yet.

### Download

[TRB Bibliography format for Word
2007/2010/2013/2016](http://minchin.ca/TRB_Minchin.ca.2013.XSL) (right-click and select
"Save Link As...")

Thanks again Maggie for the update!

### Links

- [Original Release Post]({filename}20100707-trb-transportation-research-board-bibliography-style-for-word-20072010.md)
  (July 7, 2010)
- [BibWord source code](https://github.com/codingo/BibWord) -- This is the
  original project for creating custom Bibliography styles for Word. If you
  need a style other than TRB and the built-in styles, this may provide a
  starting point for you to build your own custom style.
