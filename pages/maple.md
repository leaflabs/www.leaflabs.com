Title: The Maple
Slug: devices/maple

<a href="http://www.flickr.com/photos/48069758@N08/4613181199/"><img class="size-medium wp-image-535" style="float: left; margin-right: 8px; border: 2px solid black;" title="maple-board" src="http://farm5.static.flickr.com/4041/4613181199_33a31ca4ab_m.jpg" alt="" width="190" height="190" /></a>Our Maple board consists of the essentials: a fast processor with lots of peripherals. At the center of Maple is a 72MHz ARM Cortex M3 chip, providing the increased computational power desired by more advanced users. In the past, ARM processors were notoriously unfriendly in non-professional environments due to proprietary tool chains and unfamiliar instruction sets. Because of this, they were conspicuously absent from classrooms and hobbyists' workbenches. LeafLabs aims to change this by providing an ARM tool-chain built from open source components and a programming environment that is intuitively easy to use. For those of us who love and are familiar with Arduino, Maple is offered in an Arduino-compatible format, complete with Arduino pin layouts and programming environment. In the future, a Cortex native version is available in order to take full advantage of this fantastic micro-controller.
<div class="box" style="float: right; width: 250px; margin: 10px;">
<ul class="specs">
<h3>Technical Specs</h3>
	<li>Microcontroller: STM32 F103RB</li>
	<li>Clock Speed: 72 MHz</li>
	<li>Operating Voltage: 3.3V</li>
	<li>Input Voltage (recommended): 3.0V-12V</li>
	<li>Digital I/O Pins: 39</li>
	<li>Analog Input Pins: 16</li>
	<li>Flash Memory: 128 KB</li>
	<li>SRAM: 20KB</li>
	<li>64 Channel nested vector interrupt handler (including external interrupt on GPIO's)</li>
	<li>Integrated SPI/I2C and 7 Channels of Direct Memory Access (DMA)</li>
	<li>Supplies up to 800mA @ 3.3v</li>
	<li>Support for low power and sleep modes (&lt;500uA)</li>
	<li>Dimensions: 2.05"x2.1"</li>
</ul>
</div>
<h3 style="margin-top: 20px;">Board Overview</h3>
The LeafLabs Maple is a microcontroller board based on the <a rel="external" href="http://www.st.com/internet/mcu/product/164487.jsp" target="_blank">STM32F103RB</a> microprocessor. The Maple runs at a maximum of 72 MHz, has 39 digital input/output pins, 16 analog inputs, native full speed USB, 3 USARTs (hardware serial ports), integrated SPI/I2C support, a power jack, and a reset button. Maple is programmable over USB via our provided DFU bootloader, no extra hardware required! Users can also program the onboard program flash via external JTAG interface. Maple offers security support for read/write protected addresses, as well as User and Handler processor modes. It has a real-time sysTick, useful for a real time OS or any timing senstitive applications. Four built-in 16-bit timers will help you here as well. Maple can be powered via USB, a wall adapter, or it can run off of a rechargeable LiPo battery (see below for more info). The Maple is compatible with shields designed for the Arduino Duemilanove or Diecimila.

<em>See the <a href="/docs/">Maple documentation</a> for more details</em>

Maple is a great way to get started with an advanced 32 bit-processor that, until now, has principally lived in the commercial domain. Take your projects to the next level with Maple's fast clock, sophisticated interrupt architecture, and loads of built-in peripherals.
<h3>Programming</h3>
<em>See also <a href="/docs/ide.html">Maple Development Environment documentation</a></em>

Maple can be programmed using an Arduino-style, sketch-based programming environment, which is open-source and can be downloaded online at our website. The Cortex-M3 on Maple comes pre-programmed with a boot-loader – allowing users to upload new code onto it using the USB interface (supported directly by the Cortex-M3), without the need for an external hardware programmer. You can also program the microcontroller directly with an external JTAG interface.
