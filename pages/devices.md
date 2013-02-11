Title: Devices
Date: 2010-02-19 07:05
Author: Drews
Category: Uncategorized

At the core of every LeafLabs project is a base board. These come in three species: <a href="#Maple">Maple</a>, <a href="#Oak">Oak</a>, and <a href="#Willow">Willow</a>.

<div style="clear: both;">
<h2><a name="Maple" href="/devices/maple/">Maple</a> (Rev5)</h2>
<p>
This board has all the essentials: a fast processor with lots of peripherals.  At Maple's core is a <a href="http://www.st.com/internet/mcu/product/164487.jsp">72MHz STM32 processor</a>, an <a href="http://www.arm.com/products/processors/cortex-m/cortex-m3.php">ARM Cortex M3</a> chip. In the past, ARM processors were notoriously unfriendly to non-professionals, due to proprietary tool chains, unfamiliar instruction sets, and impenetrable supporting literature.  LeafLabs has changed this for Maple by providing a complete ARM platform, built from open source components, which includes an intuitive programming environment and <a href="/docs/">friendly, thorough documentation</a>.
</p>

<p>
For all the Arduino lovers out there, Maple is offered in an Arduino-compatible format, complete with an Arduino pin layout and <a href="http://leaflabs.com/docs/ide.html">programming environment</a>.  Maple is a great way to get started with an advanced 32 bit processor that, until now, has principally lived in the commercial domain. Take your projects to the next level with Maple’s fast clock, sophisticated interrupt architecture, and loads of built-in peripherals.
</p>

<table style="border: none; padding: none;" cellspacing="0" cellpadding="0" width="67%" align="right">
<tbody>
<tr>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Processor:</em></strong></td>
<td style="border: none;">32-bit ARM Cortex M3 at 72MHz (STM32F103RB)</td>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Peripherals:</em></strong></td>
<td style="border: none;">4 4-channel timers, 2 I<sup>2</sup>Cs, 2 SPIs, 3 USART serial ports</td>
</tr>
<tr>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Memory:</em></strong></td>
<td style="border: none;">120KB Flash and 20KB SRAM</td>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Dimensions:</em></strong></td>
<td style="border: none;">2.05x2.1 inches (5.21x5.33cm)</td>
</tr>
<tr>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>I/O Pins:</em></strong></td>
<td style="border: none;">43 (of which 15 provide PWM output at 16-bit resolution)</td>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Power:</em></strong></td>
<td style="border: none;">Integrated LiPo battery charging; sleep, stop, and standby modes</td>
</tr>
<tr>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>ADCs:</em></strong></td>
<td style="border: none;">15 (at 12-bit resolution)</td>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Debugging:</em></strong></td>
<td style="border: none;">Serial wire debug and JTAG</td>
</tr>
<tr>
<td style="border: none; text-align: center;" colspan="4"><a href="http://leaflabs.com/docs/hardware/maple.html">Check the docs!</a></td>
</tr>
</tbody>
</table>
<a href="/devices/maple/"><img style="width: 31%; float: left; margin-top: 1%; margin-left: 1.25%; margin-right: 0.75%;" src="http://leaflabs.com/wp-content/uploads/2010/02/maple-r5-brd-300x293.png" alt="" /></a>
</div>

<div style="clear: both;">
<a name="Maple-Mini"/><h2>Maple Mini</h2>
<a href="http://leaflabs.com/wp-content/uploads/2010/02/maplemini-r21.png"><img style="float: right; margin-left: 1%; margin-right: 4%; width: 20%;" src="http://leaflabs.com/wp-content/uploads/2010/02/maplemini-r21-e1296209736468-128x300.png" alt="" /></a>

<p>
Maple Mini is a "breadboard-able" PCB for applications where space is limited, or simply if a breadboard is the preferred prototyping tool.  Smaller than a stick of gum, Maple Mini features a <a href="http://www.st.com/internet/mcu/product/189782.jsp">smaller, 48-pin STM32</a> with the same speed and memory as the <a href="#Maple">Maple</a>.  Maple Mini also sports a complete silkscreen, making it uniquely detailed for a board its size.
</p>

<table style="border: none;" cellspacing="2" cellpadding="4" width="75%" align="left">
<tbody>
<tr>
<td style="border: none; text-align: center;"><em><strong>Dimensions:</strong></em></td>
<td style="border: none;">2.02 x 0.72 inches</td>
</tr>
<tr>
<td style="border: none; text-align: center;"><em><strong>Microprocessor:</strong></em></td>
<td style="border: none;">32-bit ARM Cortex M3 at 72MHz (STM32F103CBT6)</td>
</tr>
<tr>
<td style="border: none; text-align: center;"><strong><em>Memory:</em></strong></td>
<td style="border: none;">120 KB Flash and 20 KB SRAM</td>
</tr>
<tr>
<td style="border: none; text-align: center;"><strong><em>I/O Pins:</em></strong></td>
<td style="border: none;">34 (of which 12 provide PWM output at 16-bit resolution)</td>
</tr>
<tr>
<td style="border: none; text-align: center;"><strong><em>ADCs:</em></strong></td>
<td style="border: none;">9 (at 12-bit resolution)</td>
</tr>
<tr>
<td style="border: none; text-align: center;"><strong><em>Peripherals:</em></strong></td>
<td style="border: none;">4 timers, 2 I<sup>2</sup>Cs, 2 SPI ports, 3 USARTs</td>
</tr>
<tr>
<td style="border: none; text-align: center;"><strong><em>Other:</em></strong></td>
<td style="border: none;">Sleep, stop, and standby modes; serial wire debug and JTAG interfaces</td>
</tr>
<tr>
<td style="border: none; text-align: center;" colspan="2"><a href="http://leaflabs.com/docs/hardware/maple-mini.html">Check the docs!</a></td>
</tr>
</tbody>
</table>
</div>

<div style="clear: both;">
<a name="Maple-Native"><h2>Maple Native</h2></a>
<p>
<b>Please note: Maple Native Beta is closed, and we are working on Maple Native II, which will feature an STM32F407ZE chip.</b> Maple Native Beta features hardware similar to <a href="#Maple">Maple's</a>, but it is designed to fully exploit the powerful STM32F103 line. With over twice as many pins, an additional megabyte of on-board RAM, and support for true analog output, Maple Native can easily handle extremely demanding tasks.  And unlike other advanced microcontroller platforms out there, Maple Native delivers all this while maintaining the Arduino-style libraries and programming environment you're used to.
</p>

<img style="width: 21%; margin-top: 10px; margin-left: 3%; margin-right: 3%; float: left;" title="maple_native_proto" src="http://www.leaflabs.net/wp-content/uploads/2010/02/maple_native_proto-157x300.png" alt="" />
<table style="border: none;" cellspacing="0" cellpadding="0" width="70%" align="right">
<tbody>
<tr>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Processor:</em></strong></td>
<td style="border: none;">32-bit ARM Cortex M3 at 72MHz (STM32F103ZE)</td>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Peripherals:</em></strong></td>
<td style="border: none;">2 I<sup>2</sup>Cs, 3 SPI, 3 USART, and 2 UART.</td>
</tr>
<tr>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Memory:</em></strong></td>
<td style="border: none;">512KB Flash and 64KB SRAM (on-chip), 1MB SRAM (external)</td>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>ADCs:</em></strong></td>
<td style="border: none;">21 (at 12-bit resolution)</td>
</tr>
<tr>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>DAC (analog output):</em></strong></td>
<td style="border: none;">2 channels at 12-bit resolution</td>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Dimensions:</em></strong></td>
<td style="border: none;">4" x 2.1"</td>
</tr>
<tr>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>I/O Pins:</em></strong></td>
<td style="border: none;">106 (of which 17 provide PWM at 16-bit resolution)</td>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Debugging:</em></strong></td>
<td style="border: none;">Serial wire and JTAG</td>
</tr>
<tr>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>FSMC:</em></strong></td>
<td style="border: none;">45-pins, connected to 1 MB SRAM chip; also broken out to headers</td>
<td style="border: medium none; text-align: center; width: 5%;"><strong><em>Power:</em></strong></td>
<td style="border: none;">Integrated LiPo battery charging, sleep, stop, and standby modes</td>
</tr>
<tr>
<td style="border: none; text-align: center;" colspan="4"><a href="http://leaflabs.com/docs/hardware/maple-native-beta.html">Check the docs!</a></td>
</tr>
</tbody>
</table>
</div>

<p>
<div style="clear: both;">
<h3><a name="Oak">Oak</a></h3>
Oak is built from the same Cortex M3 foundation as Maple but also boasts a 250k gate Xilinx Spartan 3E, making it the first product in its class to feature an on-board FPGA. This makes Oak a full featured processing platform suitable for robotics, machine vision, surveillance, gaming, and a host of other applications. For users who are unfamiliar with programming FPGAs, LeafLabs offers a wide library of functions that exploit the powerful FPGA architecture. These can be integrated into your project with minimal overhead and without having to get into the down and dirty of learning a hardware description language.
</div>

<div style="clear: both;">
<h3><a name="Willow">Willow</a></h3>
