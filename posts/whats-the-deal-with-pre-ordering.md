Title: What's the deal with pre-ordering?
Date: 2009-10-15 20:13
Author: Hadley
Category: Uncategorized

Some of you may have noticed that there has been a store page flickering
on and off on our blog. Yes, it's pre-order season.

We had a few kinks left with paypal, but they should be straightened and
now you can pre-order your very own Maple! But why, you may ask?

Well, most relevant to you, we are only getting 100 boards on this first
run. If you really want a Maple you might want to pre-order. You'll get
the board at the same time and not risk them selling out. Also, we are
really interested in gauging the interest in this first round of Maple,
and we figured the number of pre-orders and how fast the boards sell
would be a decent proxy.  This kind of info will be a factor in deciding
how many to run for the next run of Maple and Maple Native.

Also, if you've tried to pre-order a board and paypal told you it was
sold out.... paypal lied. Now that things are worked out, you should be
able to pre-order a board [here][].

PS. For waiting so nicely, here's a pretty picture of the old prototype:

<img src="http://leaflabs.com/img/wiki_up/DSC_0456.jpg">

(The release version differs in that power selection is made using a
jumper, between standard barrel jack / USB power / LiPo batter, there is
a larger external header to connect to all the external I/O pins not
used by the Arduino pin-compatible layout and minor changes have been
made to the silkscreen and layout.)

okie edit:

Here's a picture of the third (we care a lot  about getting it right)
prototype for Maple. It has no soldermask or silkscreen because these
barebones PCBs are cheap and [Advanced Circuits][] ships them the next
day. The layout on this one is a lot better than the one in the picture
above. The traces have more direct routes, the microcontroller is closer
to the pins in the Analog section so that those trace lengths are
minimized, and those traces are also farther apart to minimize
crosstalk. The LiPo/Li-Ion battery charger on the board seems to work
well. I've been repeatedly charging and discharging a LiPo battery. It
charges it from nearly completely dead in about 20 minutes. A red LED
means that a battery is connected and is charging, which you can do by
USB power, a wall adapter, or another DC power source greater than 5V.
When the battery is charged, a green LED comes on. The charging
component is pretty smart in measuring the battery and determining when
and how to charge it. It's probably used in cell phones, media players,
etc.

<center>
<img src="/static/images/old/maple_barebones-768x1024.jpg" alt="maple_barebones" width="300px">
</center>

<center>
![red-maple-tree][]
</center>

The components on the boards that are going out for preorders are
machine placed. The pads are gold plated. The soldermask is
<span style="color: #ff0000;">**deep red**</span> like the leaves of a
maple tree in the late fall. There aren't a lot of things much better
than working with beautiful hardware on a crispy cool fall night.

Here's a screen capture of it:

<center>
<img alt="maple_eaglecapture" src="/static/images/old/maple_eaglecapture-1024x921.png" width="300px">
</center>

This also has alternate header pads that are in standard 0.1" spacing
with the other headers for those who also like perf board.

  [here]: http://leaflabs.com/store
  [Advanced Circuits]: http://www.4pcb.com
  [red-maple-tree]: /static/images/old/red-maple-tree-150x150.jpg "red-maple-tree"
