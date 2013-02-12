Title: State of the Maple Redux
Date: 2012-04-30 14:29
Author: Jessb
Category: Uncategorized

The current manufacturing run of Maples and Maple Minis is done and en
route to us. If you're impatient, you can already buy them from [Seeed
Studio][]: [Maple][] and [Maple Mini][]. Regarding distribution, we are
(hopefully) no longer going to be selling boards directly from our site
any more, and instead will be relying solely on distributors. We'll keep
you guys updated regarding which boards are available where, as that
occurs over the next couple of weeks.

Point of interest: these boards should be functionally identical to the
previous revisions, but with a couple of minor changes and additions to
the silkscreens. Most notably, the silkscreens now indicate a max input
voltage of 5V. The power circuitry is unchanged, but there was continual
confusion over how much current could safely be pulled at varying
voltage inputs, so now the party line is 5V max. If you were safely
running off a higher voltage previously, it should still work fine. More
information about power regulation on Maple and Maple Mini can be found
[here][]. In addition, we pulled off a diode on Maple Mini so the USB 5V
line is accessible from the VIN pin. Refer to the [schematic][] for
details.

Last but not least, Maple II and Maple Native II designs have been sent
out for prototyping! So we should have the first release candidates in
our hands within a week or two. We'll keep you updated.

![][]

  [Seeed Studio]: http://www.seeedstudio.com/depot/
  [Maple]: http://www.seeedstudio.com/depot/leaf-maple-cortex-m3-p-670.html?cPath=132_137
  [Maple Mini]: http://www.seeedstudio.com/depot/maple-mini-p-861.html?cPath=132_137
  [here]: http://leaflabs.com/docs/hardware/maple.html#powering-the-maple
  [schematic]: http://github.com/leaflabs/maplemini
  []: http://leaflabs.com/wp-content/uploads/2012/04/MNII-770x407.png "MNII"
