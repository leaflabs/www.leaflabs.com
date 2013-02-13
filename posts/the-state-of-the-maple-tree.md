Title: the state of the maple tree
Date: 2010-02-14 00:39
Author: jessb
Category: Uncategorized

Hi everyone! As you can probably tell from okie's awesome picture in the post
below, we got back the prototypes for Maple Rev2 about a week ago. You may
recall that the revisions were to fix two issues. The first is that the I/O has
been relabeled in a format we think makes more sense for use with the STM32 –
the pins are no longer divided into analog and digital banks, although we've
made sure the pins in those locations have those capabilities to maintain
Arduino compatibility. Maple pins are now numbered from 0 to 43 have have
labels on each pin indicating its capabilities (don't worry, the library will
still support the numbering scheme from Rev1) like PWM, AIN for analog input,
TX1, RX1 for Serial1 port (there are 3 total), and the pins in all the SPI and
I2C buses.

<center>
<img src="http://dl.dropbox.com/u/42394/maple-v25-front.png" width="300px;"> 
<img src="http://dl.dropbox.com/u/42394/maple-v25-back.png" width="300px;">
</center>

The second issue to fix in this revision was slightly more serious. We had
encountered a pretty significant voltage swing on VCC – a sawtooth that was up
to 1.5 V peak-to-peak, with no code running on the chip, depending on the power
source used. The digital I/O worked fine even with the variation, but we
shipped the Rev1 boards with a 10 uF through-hole bypass cap that was intended
to knock out the swing for those of you working on analog projects. Rev2
incorporated an extra 10 uF bypass into the design.

We got the boards back and the extra bypass seemed to do a pretty impressive
job of knocking out the swing, dropping it down to baseline max 70 mV versus
the aforementioned 1.5 V.\* Still, it's just not quite as good as we would
like.  We're still seeing spikes on VCC of up to 300 mV when pulling on some of
the peripherals (especially USB). And the twelve-bit ADCs, which we've all been
really excited about using, are losing up to six bits of resolution with some
combinations of peripherals turned on.

This isn't totally unexpected -- several of the other STM32 dev boards we
tested are similarly noisy. Even so, we're really just not satisfied with these
results, and after a lot of experimenting and deliberation, we realized we
really just couldn't get the clean signals with a two layer board. Because of
this, we've decided to switch to a four layer board. The next revision of Maple
will have dedicated ground and power planes, which should (we hope!) solve all
of our noise problems.

Of course (bet you saw this coming, didn't you?), what this means for you is
that the next revision of Maples will be shipping out about one to two weeks
later than we hoped for. This means, ultra best case scenario, the new Maples
will be shipping around March 10, and ultra worst case scenario, around
December 2040, considering what good luck we had with production last time.
Okay, just kidding – medium worst case scenario would probably be sometime
around March 31.

okie has been working tirelessly on the new four layer design, and it is nearly
finished, so we should have prototypes back within a week. Once those are back
and tested, we will be sending them to production, and at that time (probably
around February 23) we will once again be taking pre-orders!

We've been getting a lot of really wonderful feedback on the Rev1 boards, and a
lot of interest in Rev2.  For those of you who have been waiting for a Rev2, we
really are truly sorry for the added delay and inconvenience. We just hope you
guys are willing to stick with us a little longer, and that you understand our
desire to avoid sending out a product that's not 100% as sweet as it could be.
Thanks for being so awesome, everyone.

**Maple is switching to a four layer board to solve some lingering noise
issues, and so will be one or two weeks behind schedule – we're really sorry
for the delay!**

\*OK, that isn't 100% true. I mean, it is, but that's not what happened right
away. Here's the entire sordid story for the interested, edited out above for
clarity's sake: we got the boards back and were STILL seeing, baseline with no
code on the board, a sawtooth of about 300 mV, despite the bypass. 

<center>
![maple-r1-VCC-nocap][] ![maple-r1-VCC-ceramic10uF][]
</center>

We were like WTF? So we did a ridiculous amount of tests, and at some point we
dumped ANOTHER bypass on the header (a la our impromptu fix for Rev1), and it
was fixed. Again we were like WTF? So after lots of digging we eventually
realized that the voltage regulator we're using expected a bypass with a
certain equivalent series resistance. The bypass we'd added to the design was
ceramic – very little ESR. The one we'd been putting in the header was aluminum
electrolytic – plenty of ESR. OH. So we replaced the ceramic one with an
electrolytic one and voila, the results detailed above.

<center>
![maple-r1-VCC-electrolytic10uF][]
</center>

We share this story with you just in case you ever come across a similar
problem and are like WTF?, you might learn from our travails.

  [maple-r1-VCC-nocap]: http://leaflabs.com/wp-content/uploads/maple-r1-VCC-nocap-150x150.jpg "maple-r1-VCC-nocap"
  [maple-r1-VCC-ceramic10uF]: http://leaflabs.com/wp-content/uploads/maple-r1-VCC-ceramic10uF-150x150.jpg "maple-r1-VCC-ceramic10uF"
  [maple-r1-VCC-electrolytic10uF]: http://leaflabs.com/wp-content/uploads/maple-r1-VCC-electrolytic10uF-150x150.jpg "maple-r1-VCC-electrolytic10uF"
