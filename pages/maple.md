Title: The Maple Microcontroller Board
Slug: devices/maple

<a href="http://www.flickr.com/photos/48069758@N08/4613181199/"><img class="size-medium wp-image-535" style="float: left; margin-right: 8px; border: 2px solid black;" title="maple-board" src="/static/images/old/maple_top_photo.jpg" alt="" width="190" height="190" /></a>Our Maple board consists of the essentials: a fast processor with lots of peripherals. At the center of the Maple is a 72MHz ARM Cortex M3 chip, providing the increased computational power desired by more advanced users. In 2008, when development on the Maple began, ARM processors were notoriously unfriendly in non-professional environments due to proprietary tool chains and unfamiliar instruction sets. Because of this, they were conspicuously absent from classrooms and hobbyists' workbenches. With the Maple LeafLabs aimed to change this by providing an ARM tool-chain built from open source components and a programming environment that is intuitively easy to use. For those who love and are familiar with Arduino, the Maple is offered in an Arduino-compatible format, complete with Arduino pin layouts and programming environment. 

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
<br>
<h3 style="margin-top: 20px;">Board Overview</h3>

<em>See the <a href="/docs/hardware/maple.html">Maple Hardware</a> documentation for more details</em>

The LeafLabs Maple is a microcontroller board based on the <a rel="external" href="http://www.st.com/internet/mcu/product/164487.jsp" target="_blank">STM32F103RB</a> microprocessor. The Maple runs at a maximum of 72 MHz, has 39 digital input/output pins, 16 analog inputs, native full speed USB, 3 USARTs (hardware serial ports), integrated SPI/I2C support, a power jack, and a reset button. The Maple is programmable over USB via our provided DFU bootloader, no extra hardware required! Users can also program the onboard program flash via external JTAG interface. The Maple offers security support for read/write protected addresses, as well as User and Handler processor modes. It has a real-time sysTick, useful for a real time OS or any timing senstitive applications. Four built-in 16-bit timers will help you here as well. The Maple can be powered via USB, a wall adapter, or it can run off of a rechargeable LiPo battery (see below for more info). The Maple is compatible with shields designed for the Arduino Duemilanove or Diecimila.

The Maple is a great way to get started with an advanced 32 bit-processor that has principally lived in the commercial domain. Take your projects to the next level with the Maple's fast clock, sophisticated interrupt architecture, and loads of built-in peripherals.

<h3>Programming</h3>

<em>See also <a href="/docs/ide.html">Maple IDE</a> and <a
href="/docs/libmaple.html">libmaple</a> documentation</em>

The Maple can be programmed using our Arduino-style, sketch-based programming environment, which is open-source and can be downloaded from our website. The Cortex-M3 on the Maple comes pre-programmed with a boot-loader – allowing users to upload new code to it using the USB interface (supported directly by the Cortex-M3), without the need for an external hardware programmer. You can also program the microcontroller directly with an external JTAG interface.
