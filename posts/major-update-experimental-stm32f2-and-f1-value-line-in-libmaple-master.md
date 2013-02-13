Title: Major update: STM32F2 and F1 value line in libmaple master!
Date: 2012-06-27 12:42
Author: mbolivar
Category: Uncategorized
Slug: major-update-experimental-stm32f2-and-f1-value-line-in-libmaple-master

It took forever, but the [libmaple][] work we've been doing to prepare
for the in-development Maple 2 is finally in a state where we think it's
ready to live in the  [master branch on GitHub][]. The major new
features are:

-   [STM32F1 value line support][], thanks to Anton Eltchaninov
-   Experimental support for [STM32F2][] series microcontrollers
-   Significantly simplified method for adding support for your own
    boards

**[Command-line toolchain][] users: please try it out!** Though there
are tons of changes (and some deprecations), it's a top priority to keep
old code working. Your existing Maple, Maple Mini, etc. programs should
work unchanged with this new libmaple. Please test them out and report
any bugs or other regressions to [info@leaflabs.com][] or on the
[forum][], so we can iron them out before the next release. More details
on these long-awaited changes after the jump.

<!--more-->Adding support for STM32F2 was the major task we needed for
Maple 2. Though Maple 2 will have an STM32F4, F2 support was an
important prerequisite (F4s are basically F2s with faster clocks and
hardware floating point support). Now that that's largely done, we'll be
working on the necessary tweaks to get things running on F4.

Adding F2 support was no small task. [ST Application note 3427][]
(AN3427) describes ST's official recommendations for migrating code for
STM32F1 microcontrollers (like what's on Maple and all other LeafLabs
boards released to date) to STM32F2. ST's firmware libraries for F1 and
F2 are totally different, and many of the peripherals' register
interfaces have changed as well. Because of that, in many cases, ST's
recommendations amount to "you'll need to rewrite it all."

Given our mission to make the STM32 easy to use, it probably goes
without saying that we found AN3427-style migration... unsatisfactory.
From this dissatisfaction, the new and improved libmaple was born.

Following the grand C tradition of portable interfaces, with carefully
segregated target-specific implementations, we've partitioned libmaple
and Wirish into portable and nonportable sections. The nonportable
sections largely exist to provide F1- or F2-specific implementations of
common interfaces that work everywhere. This means that, in many cases,
switching from F1 to F2 is no harder than changing some command line
flags when you build libmaple; your code itself can often go unchanged.
This [example program using USART with DMA][] illustrates the point: the
same code works on F1 and F2, even though the DMA peripherals on each
are completely different.

This work made it simple to port Wirish (the Wiring/Arduino
compatibility layer) to STM32F2. The directories [wirish/stm32f1][] and
[wirish/stm32f2][] contain the series-specific pieces of the library. Go
take a look at them if you're curious: there's almost nothing inside.
libmaple's C layer really does end up doing almost all of the heavy
lifting.

Of course, it's not all sunshine and unicorn giggles. Here are the known
issues and gotchas:

-   Some existing libmaple interfaces were too F1-specific, and just
    couldn't port. We're deprecating those to encourage you to move to
    the new portable interfaces. A detailed changelog and porting guide
    is in the works, and our documentation will cover things as
    thoroughly as you've come to expect.
-   F2 support is still experimental, and some pieces are missing. In
    particular, there's no i2c.h or HardwareSPI on F2 yet.
-   F2 is currently missing USB support, and we don't expect to add it
    by the time the next release rolls around.

That said, we're excited to get this into master, and we really hope you
try it out. Happy hacking!

  [libmaple]: http://leaflabs.com/docs/libmaple.html
  [master branch on GitHub]: https://github.com/leaflabs/libmaple/commit/ccc23369719f8909fe61a8423fdf382582414702
  [STM32F1 value line support]: https://github.com/leaflabs/libmaple/commit/2fb91678e08fc25299d70b1500495bbe06ee61be
  [STM32F2]: http://www.st.com/internet/mcu/subclass/1520.jsp
  [Command-line toolchain]: http://leaflabs.com/docs/unix-toolchain.html
  [info@leaflabs.com]: mailto:info@leaflabs.com
  [forum]: http://forums.leaflabs.com/
  [ST Application note 3427]: http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/APPLICATION_NOTE/DM00033267.pdf
  [example program using USART with DMA]: https://github.com/leaflabs/libmaple/blob/ccc23369719f8909fe61a8423fdf382582414702/examples/test-usart-dma.cpp
  [wirish/stm32f1]: https://github.com/leaflabs/libmaple/tree/ccc23369719f8909fe61a8423fdf382582414702/wirish/stm32f1
  [wirish/stm32f2]: https://github.com/leaflabs/libmaple/tree/ccc23369719f8909fe61a8423fdf382582414702/wirish/stm32f2
