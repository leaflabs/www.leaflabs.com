Title: Maple Rev5 Now Available!
Date: 2010-11-05 15:40
Author: poslathian
Category: Uncategorized

After a tense 30 day inventory gap after the complete sellout of Maple
Rev3, we have finally completed the first fab run of Maple Rev5! The new
design incorporates a few changes that our users have been asking for -
compatibility with 1/10" spacing (meaning shields can be made out of
proto-board or breadboard instead of expensive custom PCB's) on the
additional header and the analog supply has been broken out on the power
header for low-noise applications. Additionally, we made some
improvements to the silkscreen that we think you will find useful.
Testing and flashing is completed on these boards, and we will start
shipping them out very shortly (~Nov. 13)! Unfortunately, much of this
batch has already been purchased in volume by independent groups and
distributors, leaving us only 50 boards! The good news is that we have
already ordered the next batch, which should be about 35 days out. The
bad news is that this will almost certainly mean another inventory gap,
so if you want a board for Christmas this year, head over to the store
page soon.

<a rel="attachment wp-att-1435" href="http://leaflabs.com/2010/11/maple-rev5-now-available/p1240903/"><img class="alignnone size-medium wp-image-1435" title="P1240903" src="/static/images/old/2010/11/P1240903-300x225.jpg" alt="" width="300" height="225" /></a><a rel="attachment wp-att-1436" href="http://leaflabs.com/2010/11/maple-rev5-now-available/p1240906/"><img class="alignnone size-medium wp-image-1436" title="P1240906" src="/static/images/old/2010/11/P1240906-300x225.jpg" alt="" width="300" height="225" /></a><a rel="attachment wp-att-1437" href="http://leaflabs.com/2010/11/maple-rev5-now-available/p1240908/"><img class="alignnone size-medium wp-image-1437" title="P1240908" src="/static/images/old/2010/11/P1240908-300x225.jpg" alt="" width="300" height="225" /></a><a rel="attachment wp-att-1442" href="http://leaflabs.com/2010/11/maple-rev5-now-available/p1240905/"><img class="alignnone size-medium wp-image-1442" title="P1240905" src="/static/images/old/2010/11/P1240905-300x225.jpg" alt="" width="300" height="225" /></a>

We have some other projects on the way to heighten brighten your holiday
season even more. Maple Mini is in its final testing stages, and we will
be getting the first 200 of these boards in shortly. Target price for
these boards is in the $33 range, and because the first run is a pretty
small one we will likely put them up for pre-order as soon as were
satisfied with the production samples. Maple Native is also on its way
to fab, and our programming tools have been expanded to fully support
both of these new boards.

Speaking of software tools, we've begun dog-fooding our pre-alpha
version of the new IDE! Whats new about it? First off its all written in
python, from the ground up. The interface is the same as what youre used
to, and all our command line tools will still be available. But this new
frontend is more stable, extensible, and most importantly - hackable
than its java predecessor, forked from the Arduino project. My favorite
new features? optional Emacs keybindings, and improved compiler and
debug reporting. The serial interface is substantially improved as well.

On the libmaple side, we're finishing up a comprehensive interface for
Direct Memory Access (DMA). This core feature of the stm32 allows for
data to be copied asynchronously, without incurring the performance cost
of code that busies the processor by reading data from A and writing it
to B. The DMA allows you to do things such as creating magic buffers
that are always filled with the latest readings from the ADC, or
configuring the I2C to write out a whole swath of data, whilst your
program can go off and do other things. The DMA even allows for your
code to copy data between two local memory buffers asynchronously. In a
lot of ways, it feels like threading - but restricted to memory copy and
data transfer operations.

Because of the addition of DMA support, previously unavailable features
of other peripherals will become usable. For example, hardware I2C,
advanced ADC configurations, and fast asynchronous serial channels will
open new opportunities for higher performance in your applications.

We are excited to see how you put all these things to use and we're
putting some tutorials together to help get you started. For example,
how to drive a VGA monitor to make a pong game, how to create a 20
channel synthesizer capable of reproducing the famous THX deep note, and
how to build a 44KHz 16bit in/out programmable audio effects pedal! Stay
tuned!

