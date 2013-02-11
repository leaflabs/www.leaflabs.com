Title: PyMite
Date: 2011-09-23 15:09
Author: Cospan
Category: Uncategorized

We've got our blink on... Python style!

If you haven't had a chance to check out the specs on [Maple Native][]:

-   72MHz
-   1MB external SRAM
-   DACs
-   I2Cs
-   SPIs
-   UARTs
-   ADCs
-   FSMC

</p>
To summarize, its got some junk in the trunk.

Last week we had a meeting to figure out a good way to demonstrate why
EVERYBODY will not be able to live without it, and AJ chimes in with:
"Has anybody played around with PyMite?"

PYTHON!... on a microcontroller! That you can interact with!  At
runtime! Tooo good to be true.

Took me a week of randomly banging on a keyboard but yesterday we typed
blinky into interactive pymite (IPM) and... let's just say I'm giddy.

[![][]][]

Anyway, we think it might be ready for some users to play around with.
It's still rough around the edges, but if you've got a Maple Native or a
Maple RET6 Edition and want to partake in some luscious Python goodness,
then grab the latest release from our projects repo on GitHub (sorry,
but this little slice of heaven is currently only usable from the
[command line][] toolchain):

`$ git clone git://github.com/leaflabs/projects.git`

Then follow the hastily written up [instructions on the wiki][].

Dave

  [Maple Native]: http://leaflabs.com/devices/#Maple-Native
    "Blatant Advertisement"
  []: http://leaflabs.com/wp-content/uploads/2011/09/Screenshot-1.png
    "Interactive PyMite Session"
  [![][]]: http://leaflabs.com/2011/09/pymite/screenshot-1/
  [command line]: http://leaflabs.com/docs/unix-toolchain.html
  [instructions on the wiki]: http://wiki.leaflabs.com/index.php?title=PyMite
