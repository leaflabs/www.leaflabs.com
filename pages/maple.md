Title: The Maple
Date: 2010-02-20 17:23
Author: Drews
Category: Uncategorized

[![][]][]Our Maple board consists of the essentials: a fast processor
with lots of peripherals. At the center of Maple is a 72MHz ARM Cortex
M3 chip, providing the increased computational power desired by more
advanced users. In the past, ARM processors were notoriously unfriendly
in non-professional environments due to proprietary tool chains and
unfamiliar instruction sets. Because of this, they were conspicuously
absent from classrooms and hobbyists' workbenches. LeafLabs aims to
change this by providing an ARM tool-chain built from open source
components and a programming environment that is intuitively easy to
use. For those of us who love and are familiar with Arduino, Maple is
offered in an Arduino-compatible format, complete with Arduino pin
layouts and programming environment. In the future, a Cortex native
version is available in order to take full advantage of this fantastic
micro-controller.

<div class="box" style="float: right; width: 250px; margin: 10px;">
</p>

-   Microcontroller: STM32 F103RB
-   Clock Speed: 72 MHz
-   Operating Voltage: 3.3V
-   Input Voltage (recommended): 3.0V-12V
-   Digital I/O Pins: 39
-   Analog Input Pins: 16
-   Flash Memory: 128 KB
-   SRAM: 20KB
-   64 Channel nested vector interrupt handler (including external
    interrupt on GPIO's)
-   Integrated SPI/I2C and 7 Channels of Direct Memory Access (DMA)
-   Supplies up to 800mA @ 3.3v
-   Support for low power and sleep modes (\<500uA)
-   Dimensions: 2.05"x2.1"

</p>
<p>
</div>
</p>

### Board Overview

</p>
The LeafLabs Maple is a microcontroller board based on
the [STM32F103RB][] microprocessor. The Maple runs at a maximum of 72
MHz, has 39 digital input/output pins, 16 analog inputs, native full
speed USB, 3 USARTs (hardware serial ports), integrated SPI/I2C support,
a power jack, and a reset button. Maple is programmable over USB via our
provided DFU bootloader, no extra hardware required! Users can also
program the onboard program flash via external JTAG interface. Maple
offers security support for read/write protected addresses, as well as
User and Handler processor modes. It has a real-time sysTick, useful for
a real time OS or any timing senstitive applications. Four built-in
16-bit timers will help you here as well. Maple can be powered via USB,
a wall adapter, or it can run off of a rechargeable LiPo battery (see
below for more info). The Maple is compatible with shields designed for
the Arduino Duemilanove or Diecimila.

*See the [Maple documentation][] for more details*

Maple is a great way to get started with an advanced 32 bit-processor
that, until now, has principally lived in the commercial domain. Take
your projects to the next level with Maple's fast clock, sophisticated
interrupt architecture, and loads of built-in peripherals.

### Programming

</p>
*See also [Maple Development Environment documentation][]*

Maple can be programmed using an Arduino-style, sketch-based programming
environment, which is open-source and can be downloaded online at our
website. The Cortex-M3 on Maple comes pre-programmed with a boot-loader
– allowing users to upload new code onto it using the USB interface
(supported directly by the Cortex-M3), without the need for an external
hardware programmer. You can also program the microcontroller directly
with an external JTAG interface.

  []: http://farm5.static.flickr.com/4041/4613181199_33a31ca4ab_m.jpg
    "maple-board"
  [![][]]: http://www.flickr.com/photos/48069758@N08/4613181199/
  [STM32F103RB]: http://www.st.com/internet/mcu/product/164487.jsp
  [Maple documentation]: /docs/
  [Maple Development Environment documentation]: /docs/ide.html
