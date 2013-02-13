Title: Maple Native Arriveth!
Date: 2011-09-09 09:57
Author: mbolivar
Category: News

The long wait is over!  <a href="http://leaflabs.com/store/">Maple Native's
beta release is on sale!</a>  Hurray!

<img src="http://leaflabs.com/wp-content/uploads/2011/09/native-beta-front-600x364.png" style="display: block; width: 600px; clear: both; margin: 0 auto;"/>

<div style="text-align: center; clear: both;">
<form target="paypal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="CN8MKPG4VMXH8">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_cart_SM.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<h4 style="color: green; clear: both;">$74.99</h4>
 <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>
</div>

<h3>Specifications</h3>

<div>
<ul>
<li>MCU: <a href="http://www.st.com/internet/mcu/product/164495.jsp">STM32F103ZET6</a>, a 32-bit ARM Cortex M3 microprocessor.</li>
<li>Clock Speed: <strong>72 MHz</strong></li>
<li><strong>512 KB Flash</strong>, <strong>64 KB SRAM</strong> (on-chip), <strong>1 MB SRAM</strong> (external)</li>
<li>106 <strong>GPIOs</strong></li>
<li>17 <strong>PWM</strong> pins, at 16 bit resolution</li>
<li>21 <strong>ADC</strong> pins, at 12-bit resolution</li>
<li>3 <strong>SPI</strong> peripherals</li>
<li>2 <strong>I2C</strong> peripherals</li>
<li>12 Channels of direct memory access (<strong>DMA</strong>), with 2 DMA controllers</li>
<li>3 <strong>USARTs</strong> (serial port), 2 <strong>UARTs</strong></li>
<li>2 advanced, 4 general-purpose, and 2 basic <strong>timers</strong></li>
<li>Dedicated <strong>USB</strong> port for programming and communications</li>
<li>Dimensions: 4″ × 2.1″</li>
</ul>
</div>

<h3>Why is this a Beta?</h3>

<p>
Experience has (finally) taught us that finalizing the design of a new board <a href="http://leaflabs.com/docs/hardware/maple.html#maple-identify-rev">might take a couple of tries</a>.  Thus, rather than trumpeting this design's utter perfection (from the rooftops or otherwise), we're going to give ourselves a little wiggle room.  That is to say, maybe we'll move some pins around between now and the final version, like we did on Maple rev 5.  Maybe we'll mess with the silkscreen.  Maybe we'll fix a couple of bugs.  Nothing major; just wiggles.

<p>
In addition to that, there are still some software issues which we're working out before we declare this battle station fully operational.  In particular, we're working on making the 1 MB of external SRAM as easy to use as possible.  Technical details for the curious after the jump.
</p>
<!--more-->

As of version 0.0.11, <a href="/docs/libmaple.html">libmaple</a> doesn't deal very well with dynamic memory allocation.  This has never been much of a problem before, since even the <a href="/store/#Maple-RET6">Maple RET6 Edition</a> only has 64 KB of SRAM, so static allocation is usually sufficient.  With a full megabyte of RAM, however, the story is different.  A recent <a href="https://github.com/leaflabs/libmaple/commit/8b9a3f4e7a685480f75da19df1b5ef1adeaad982">series</a> <a href="https://github.com/leaflabs/libmaple/commit/aa4f3b6645a17c98aa4679323208ed8636ba89b1">of</a> <a href="https://github.com/leaflabs/libmaple/commit/3c0a3ee2516e6709484a922b8298c84eccf87490">commits</a> in libmaple has fixed dynamic memory allocation, but the heap is still on the internal SRAM.  That's not so great; we expect many (most?) users will want the heap in external memory, so they can e.g. allocate large buffers for audio or image processing.

To resolve this issue, we're putting together some additional linker scripts for the Maple Native, which will transparently put the heap on the SRAM chip.  Using these scripts, <tt>malloc()</tt> and friends will return pointers into external SRAM.

This might not suit everyone's purposes, for two reasons.  First, the external chip is slower.  Second, using it grabs a huge number of GPIOs on the triple header at the right hand side of the board.  For this reason, the traditional "RAM" and "Flash" builds you're used to are still available.  These keep the heap on internal SRAM, allowing you to use the extra GPIOs for your own purposes.

Stay tuned for more on this and other updates!
