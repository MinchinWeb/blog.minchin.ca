Title: TRB (Transportation Research Board) Bibliography Style for Word 2007/2010
Date: 2010-07-07 11:34
Modified_1: 2012-06-28 7:17
Modified_2: 2016-08-08 21:25
Modified: 2017-08-30 12:27
Author: Wm. Minchin
Tags: BibWord, Microsoft Word, TRB, Word 2007, releases
Alias: 2010/07/trb-transportation-research-board.html
Slug: trb-transportation-research-board-bibliography-style-for-word-2007-2010
summary: Introducing my version of the Transportation Research Board (TRB) reference style for use with the reference manager in Microsoft Word 2007 and 2010.

A wonderful citation
manager was introduced in Microsoft Word 2007 (found on the 'Reference'
tab, see below).

<div markdown=1 class="text-center">
![Reference in Word]({filename}/images/2010/References_in_Word.png)
</div>

It allows one to add sources to a paper or report as it is being typed in a
nearly automated fashion and will then compile your reference list too. For me,
it's been a godsend; I like writing papers (well enough, anyway) but get
annoyed when 'minor' details, like what referencing styles should be used,
start taking up major time. Great as it is, the one problem that remained was
Word was limited to a few built-in styles; if the required style wasn't on the
list, you were just out of luck. Well, it turns out that the Word system is
actually quite extendable. The open source project
[BibWord](http://bibword.codeplex.com/) has provided a framework to quickly add
new styles and has generated a number of new ones. Based on that work, I here
present my version of the TRB reference style based on their [Guide for
Authors](http://onlinepubs.trb.org/onlinepubs/AM/InfoForAuthors.pdf) (PDF).

In-text references are numeric, based on reference order.

Repeated references reuse the original number.

> ... Different pedestrian behaviour is associated not only with different
> physical characteristics but also the differing purpose of pedestrians (*1,
> 2*). Studies have been carried out for crowds associated with transportation
> systems (*3, 4, 5*), sporting and general spectator occasions (*6*), holy
> sites (*7, 8*), political demonstrations (*9*), and fire escapes (*10*).

The bibliography output is as follows:

> 1. Polus, A., J.L. Schofer, and A. Ushpi. Pedestrian flow and level of
>    service. <i>Journal of Transportation Engineering Proceedings, ASCE</i>,
>    Vol. 109, 1983, pp. 46-57.
>
> 2. Toshiyuki, A. Prediction system of passenger flow, in *Engineering for
>    Crowd Safety*, Smith, R.A., and J.F. Dickie. Amsterdam: Elsevier, 1993,
>    pp. 249-258.
>
> 3. Smith, R.A., and J.F. Dickie. *Engineering for Crowd Safety*. Amsterdam,
>    1993.
>
> 4. Tanaka, T. A study for performance based design of means of escape in
>    fire, in <i>Fire Safety Science -- Proceedings of the 3rd International
>    Symposium</i>, Cox, G., and B. Langford. Amsterdam: Elsevier, 1991, pp.
>    729-738.
>
> 5. Wikipedia contributors. List of metro systems. *Wikipedia, The Free
>    Encyclopedia*, June 17, 2010.
>    <http://en.wikipedia.org/w/index.php?title=List_of_metro_systems&oldid=368658114>.
>    Accessed June 17, 2010.

To use this, download the file below and place it in the `<winword.exe
directory>\Bibliography\Style` directory. Reopen Word and it should show up in
the list of available styles as "TRB [Minchin.ca]". This remains a work in
progress, and so if you find this useful or find something that needs to be
corrected, please contact me!

**Download**: [TRB Bibliography format for Word
2007/2010](http://minchin.ca/TRB_Minchin.ca.XSL) (right-click and select
"Save Link As...")

### Update (August 8, 2016)

It would appear that changes made in recent version of Word (Word 2016, at
least) have broken this. The format appears to be similar, but I haven't (yet)
had time to investigate what's changed.

So, for now, this sadly doesn't work with Word 2016.

### Update 2 (August 30, 2017)

[An updated
version]({filename}20170830-trb-bibliography-style-for-word-updated.md) has
been provided by a blog reader, Maggie McNamara, that will work with Word 2013
and 2016! Thanks so much Maggie!
