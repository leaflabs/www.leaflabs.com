Title: Maple Native Arriveth!
Date: 2011-09-09 09:57
Author: Mbolivar
Category: News

The long wait is over! [Maple Native's beta release is on sale!][]
Hurray!

</p>

![][]

<div style="text-align: center; clear: both;">
</p>
<p>
<form target="paypal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
</p>
<input type="hidden" name="cmd" value="_s-xclick">

<input type="hidden" name="hosted_button_id" value="CN8MKPG4VMXH8">

<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_cart_SM.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">

#### \$74.99

</p>
![][1]

<p>
</form>
</p>
<p>
</div>
</p>

### Specifications

</p>

<div>
</p>

-   MCU: [STM32F103ZET6][], a 32-bit ARM Cortex M3 microprocessor.
-   Clock Speed: **72 MHz**
-   **512 KB Flash**, **64 KB SRAM** (on-chip), **1 MB SRAM** (external)
-   106 **GPIOs**
-   17 **PWM** pins, at 16 bit resolution
-   21 **ADC** pins, at 12-bit resolution
-   3 **SPI** peripherals
-   2 **I2C** peripherals
-   12 Channels of direct memory access (**DMA**), with 2 DMA
    controllers
-   3 **USARTs** (serial port), 2 **UARTs**
-   2 advanced, 4 general-purpose, and 2 basic **timers**
-   Dedicated **USB** port for programming and communications
-   Dimensions: 4″ × 2.1″

</p>
<p>
</div>
</p>

### Why is this a Beta?

</p>

Experience has (finally) taught us that finalizing the design of a new
board [might take a couple of tries][]. Thus, rather than trumpeting
this design's utter perfection (from the rooftops or otherwise), we're
going to give ourselves a little wiggle room. That is to say, maybe
we'll move some pins around between now and the final version, like we
did on Maple rev 5. Maybe we'll mess with the silkscreen. Maybe we'll
fix a couple of bugs. Nothing major; just wiggles.

In addition to that, there are still some software issues which we're
working out before we declare this battle station fully operational. In
particular, we're working on making the 1 MB of external SRAM as easy to
use as possible. Technical details for the curious after the jump.

</p>
<!--more-->

As of version 0.0.11, [libmaple][] doesn't deal very well with dynamic
memory allocation. This has never been much of a problem before, since
even the [Maple RET6 Edition][] only has 64 KB of SRAM, so static
allocation is usually sufficient. With a full megabyte of RAM, however,
the story is different. A recent [series][] [of][] [commits][] in
libmaple has fixed dynamic memory allocation, but the heap is still on
the internal SRAM. That's not so great; we expect many (most?) users
will want the heap in external memory, so they can e.g. allocate large
buffers for audio or image processing.

To resolve this issue, we're putting together some additional linker
scripts for the Maple Native, which will transparently put the heap on
the SRAM chip. Using these scripts, `malloc()` and friends will return
pointers into external SRAM.

This might not suit everyone's purposes, for two reasons. First, the
external chip is slower. Second, using it grabs a huge number of GPIOs
on the triple header at the right hand side of the board. For this
reason, the traditional "RAM" and "Flash" builds you're used to are
still available. These keep the heap on internal SRAM, allowing you to
use the extra GPIOs for your own purposes.

Stay tuned for more on this and other updates!

  [Maple Native's beta release is on sale!]: http://leaflabs.com/store/
  []: http://leaflabs.com/wp-content/uploads/2011/09/native-beta-front-600x364.png
  [1]: https://www.paypalobjects.com/en_US/i/scr/pixel.gif
  [STM32F103ZET6]: http://www.st.com/internet/mcu/product/164495.jsp
  [might take a couple of tries]: http://leaflabs.com/docs/hardware/maple.html#maple-identify-rev
  [libmaple]: /docs/libmaple.html
  [Maple RET6 Edition]: /store/#Maple-RET6
  [series]: https://github.com/leaflabs/libmaple/commit/8b9a3f4e7a685480f75da19df1b5ef1adeaad982
  [of]: https://github.com/leaflabs/libmaple/commit/aa4f3b6645a17c98aa4679323208ed8636ba89b1
  [commits]: https://github.com/leaflabs/libmaple/commit/3c0a3ee2516e6709484a922b8298c84eccf87490
