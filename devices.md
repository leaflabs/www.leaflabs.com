Title: Devices
Date: 2010-02-19 07:05
Author: Drews
Category: Uncategorized

At the core of every LeafLabs project is a base board. These come in
three species: [Maple][], [Oak][], and [Willow][].

<div style="clear: both;">
</p>

[Maple][1] (Rev5)
-----------------

</p>

This board has all the essentials: a fast processor with lots of
peripherals. At Maple's core is a [72MHz STM32 processor][], an [ARM
Cortex M3][] chip. In the past, ARM processors were notoriously
unfriendly to non-professionals, due to proprietary tool chains,
unfamiliar instruction sets, and impenetrable supporting literature.
LeafLabs has changed this for Maple by providing a complete ARM
platform, built from open source components, which includes an intuitive
programming environment and [friendly, thorough documentation][].

</p>

For all the Arduino lovers out there, Maple is offered in an
Arduino-compatible format, complete with an Arduino pin layout and
[programming environment][]. Maple is a great way to get started with an
advanced 32 bit processor that, until now, has principally lived in the
commercial domain. Take your projects to the next level with Maple’s
fast clock, sophisticated interrupt architecture, and loads of built-in
peripherals.

</p>

<table style="border: none; padding: none;" cellspacing="0" cellpadding="0" width="67%" align="right">
</p>
<p>
<tbody>
</p>
<p>
<tr>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Processor:***

</td>
</p>
<p>
<td style="border: none;">
32-bit ARM Cortex M3 at 72MHz (STM32F103RB)

</td>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Peripherals:***

</td>
</p>
<p>
<td style="border: none;">
4 4-channel timers, 2 I^2^Cs, 2 SPIs, 3 USART serial ports

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Memory:***

</td>
</p>
<p>
<td style="border: none;">
120KB Flash and 20KB SRAM

</td>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Dimensions:***

</td>
</p>
<p>
<td style="border: none;">
2.05x2.1 inches (5.21x5.33cm)

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***I/O Pins:***

</td>
</p>
<p>
<td style="border: none;">
43 (of which 15 provide PWM output at 16-bit resolution)

</td>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Power:***

</td>
</p>
<p>
<td style="border: none;">
Integrated LiPo battery charging; sleep, stop, and standby modes

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***ADCs:***

</td>
</p>
<p>
<td style="border: none;">
15 (at 12-bit resolution)

</td>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Debugging:***

</td>
</p>
<p>
<td style="border: none;">
Serial wire debug and JTAG

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: none; text-align: center;" colspan="4">
[Check the docs!][]

</td>
</p>
<p>
</tr>
</p>
<p>
</tbody>
</p>
<p>
</table>
</p>
[![][]][1]

<p>
</div>
</p>

<div style="clear: both;">
</p>
<a name="Maple-Mini"></a>

Maple Mini
----------

</p>
[![][2]][]

Maple Mini is a "breadboard-able" PCB for applications where space is
limited, or simply if a breadboard is the preferred prototyping tool.
Smaller than a stick of gum, Maple Mini features a [smaller, 48-pin
STM32][] with the same speed and memory as the [Maple][]. Maple Mini
also sports a complete silkscreen, making it uniquely detailed for a
board its size.

</p>

<table style="border: none;" cellspacing="2" cellpadding="4" width="75%" align="left">
</p>
<p>
<tbody>
</p>
<p>
<tr>
</p>
<p>
<td style="border: none; text-align: center;">
***Dimensions:***

</td>
</p>
<p>
<td style="border: none;">
2.02 x 0.72 inches

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: none; text-align: center;">
***Microprocessor:***

</td>
</p>
<p>
<td style="border: none;">
32-bit ARM Cortex M3 at 72MHz (STM32F103CBT6)

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: none; text-align: center;">
***Memory:***

</td>
</p>
<p>
<td style="border: none;">
120 KB Flash and 20 KB SRAM

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: none; text-align: center;">
***I/O Pins:***

</td>
</p>
<p>
<td style="border: none;">
34 (of which 12 provide PWM output at 16-bit resolution)

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: none; text-align: center;">
***ADCs:***

</td>
</p>
<p>
<td style="border: none;">
9 (at 12-bit resolution)

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: none; text-align: center;">
***Peripherals:***

</td>
</p>
<p>
<td style="border: none;">
4 timers, 2 I^2^Cs, 2 SPI ports, 3 USARTs

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: none; text-align: center;">
***Other:***

</td>
</p>
<p>
<td style="border: none;">
Sleep, stop, and standby modes; serial wire debug and JTAG interfaces

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: none; text-align: center;" colspan="2">
[Check the docs!][3]

</td>
</p>
<p>
</tr>
</p>
<p>
</tbody>
</p>
<p>
</table>
</p>
<p>
</div>
</p>

<div style="clear: both;">
</p>
<a name="Maple-Native">

Maple Native
------------

</a>

</p>

**Please note: Maple Native Beta is closed, and we are working on Maple
Native II, which will feature an STM32F407ZE chip.** Maple Native Beta
features hardware similar to [Maple's][Maple], but it is designed to
fully exploit the powerful STM32F103 line. With over twice as many pins,
an additional megabyte of on-board RAM, and support for true analog
output, Maple Native can easily handle extremely demanding tasks. And
unlike other advanced microcontroller platforms out there, Maple Native
delivers all this while maintaining the Arduino-style libraries and
programming environment you're used to.

</p>

![][4]

<table style="border: none;" cellspacing="0" cellpadding="0" width="70%" align="right">
</p>
<p>
<tbody>
</p>
<p>
<tr>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Processor:***

</td>
</p>
<p>
<td style="border: none;">
32-bit ARM Cortex M3 at 72MHz (STM32F103ZE)

</td>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Peripherals:***

</td>
</p>
<p>
<td style="border: none;">
2 I^2^Cs, 3 SPI, 3 USART, and 2 UART.

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Memory:***

</td>
</p>
<p>
<td style="border: none;">
512KB Flash and 64KB SRAM (on-chip), 1MB SRAM (external)

</td>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***ADCs:***

</td>
</p>
<p>
<td style="border: none;">
21 (at 12-bit resolution)

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***DAC (analog output):***

</td>
</p>
<p>
<td style="border: none;">
2 channels at 12-bit resolution

</td>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Dimensions:***

</td>
</p>
<p>
<td style="border: none;">
4" x 2.1"

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***I/O Pins:***

</td>
</p>
<p>
<td style="border: none;">
106 (of which 17 provide PWM at 16-bit resolution)

</td>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Debugging:***

</td>
</p>
<p>
<td style="border: none;">
Serial wire and JTAG

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***FSMC:***

</td>
</p>
<p>
<td style="border: none;">
45-pins, connected to 1 MB SRAM chip; also broken out to headers

</td>
</p>
<p>
<td style="border: medium none; text-align: center; width: 5%;">
***Power:***

</td>
</p>
<p>
<td style="border: none;">
Integrated LiPo battery charging, sleep, stop, and standby modes

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td style="border: none; text-align: center;" colspan="4">
[Check the docs!][5]

</td>
</p>
<p>
</tr>
</p>
<p>
</tbody>
</p>
<p>
</table>
</p>
<p>
</div>
</p>

<div style="clear: both;">
</p>

### <a name="Oak">Oak</a>

</p>
Oak is built from the same Cortex M3 foundation as Maple but also boasts
a 250k gate Xilinx Spartan 3E, making it the first product in its class
to feature an on-board FPGA. This makes Oak a full featured processing
platform suitable for robotics, machine vision, surveillance, gaming,
and a host of other applications. For users who are unfamiliar with
programming FPGAs, LeafLabs offers a wide library of functions that
exploit the powerful FPGA architecture. These can be integrated into
your project with minimal overhead and without having to get into the
down and dirty of learning a hardware description language.

<p>
</div>
</p>

<div style="clear: both;">
</p>

### <a name="Willow">Willow</a>

</p>
There will be more information on Willow as it becomes available. The
Willow model is in the very early stages of development.

<p>
</div>
</p>

  [Maple]: #Maple
  [Oak]: #Oak
  [Willow]: #Willow
  [1]: /devices/maple/
  [72MHz STM32 processor]: http://www.st.com/internet/mcu/product/164487.jsp
  [ARM Cortex M3]: http://www.arm.com/products/processors/cortex-m/cortex-m3.php
  [friendly, thorough documentation]: /docs/
  [programming environment]: http://leaflabs.com/docs/ide.html
  [Check the docs!]: http://leaflabs.com/docs/hardware/maple.html
  []: http://leaflabs.com/wp-content/uploads/2010/02/maple-r5-brd-300x293.png
  [2]: http://leaflabs.com/wp-content/uploads/2010/02/maplemini-r21-e1296209736468-128x300.png
  [![][2]]: http://leaflabs.com/wp-content/uploads/2010/02/maplemini-r21.png
  [smaller, 48-pin STM32]: http://www.st.com/internet/mcu/product/189782.jsp
  [3]: http://leaflabs.com/docs/hardware/maple-mini.html
  [4]: http://www.leaflabs.net/wp-content/uploads/2010/02/maple_native_proto-157x300.png
    "maple_native_proto"
  [5]: http://leaflabs.com/docs/hardware/maple-native-beta.html
