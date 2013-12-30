Title: Devices
Slug: devices

<br>
<div style="clear: both;">
<h2><a name="maple" href="/devices/maple/">Maple</a>
&nbsp;<span class="devicesubtitle">Arduino-style STM32 Microcontroller Board</span>
<span class="devicestatusproduction">Production</span>
</h2>
<hr>

The Maple was LeafLab's first product, released in 2009. It was one of the
first ARM Cortex-M3 microcontroller boards that was accessible to hobbyists and
engineers outside of the embedded industry. The design was modeled on the
Arduino boards, with a pin-out backwards compatible with most shields and a
programming environment based on the free software GCC toolchain and the
Processing/Wiring/Arduino user interface. LeafLabs wrote a new open source C
library (libmaple) for this board, having found the vendor supplied libraries
inadequate. 

In 2011 a small number of <a href="/docs/hardware/maple-ret6.html">"RET6 Edition"</a>
variant boards were produced,
which featured a newer STM32 microcontroller with enough RAM and non-volatile
flash memory to support lightweight interpreted language runtimes (eg, eLua)
and real-time operating systems. This variant is no longer in production.

A longer blurb is available <a href="/devices/maple/">here</a>. As of 2014, the
Maple board is still available from <a href="/distributors/">distributors</a>,
but no future hardware revisions are planned and the IDE will not be ported to
newer operating systems.

<br>
<a href="/devices/maple/"><img style="border: 2px solid black; float: left; margin-left: 0px; width: 190px;" src="/static/images/old/maple_top_photo.jpg" alt="maple gerber" /></a>

<br>
<ul style="float:right;margin-right:0px;width:250px;">
 <li>Dual <b>I2C</b> and <b>SPI</b> ports 
 </li><li>3 USART Serial ports
 </li><li>7-channel <b>DMA</b>
 </li><li>Low power and sleep modes 
 </li><li>Integrated LiPo Battery Charging
 </li><li>Dimensions: 2.05" x 2.1"
 </li><li>Extensive <a href="/docs/hardware/maple.html">documentation</a>
 </li><li><a href="https://github.com/leaflabs/maplemini">Design files</a> under
          <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>
</li></ul> 
<ul style="margin-left: 240px;"> 
 <li>STM32F103RB: a <b>32-bit</b> ARM Cortex-M3 microprocessor at <b>72Mhz</b> 
 </li><li><b>20KB</b> RAM and <b>128KB</b> Flash 
 </li><li>Dedicated <b>USB</b> port for programming and communications 
 </li><li>43 General Purpose pins 
 </li><li><b>15 Analog</b> inputs at 12-bit resolution 
 </li><li><b>15 PWM pins</b> at 16-bit resolution 
</li></ul> 
</div>

<br><br>
<div style="clear: both;">
<h2><a name="Maple-Mini"></a><a name="maplemini" href="/docs/hardware/maple-mini.html">Maple Mini</a>
&nbsp;<span class="devicesubtitle">Breadboard-able STM32 Microcontroller Board</span>
<span class="devicestatusproduction">Production</span>
</h2>
<hr>

Introduced in early 2011, the Maple Mini is a "breadboard-able" PCB for
applications where space is limited, or simply if a breadboard is the preferred
prototyping tool.  Smaller than a stick of gum, Maple Mini features a <a
href="http://www.st.com/internet/mcu/product/189782.jsp">smaller, 48-pin
STM32</a> with the same speed and memory as the <a href="#Maple">Maple</a>.
Maple Mini also has a complete silkscreen, making it uniquely detailed for a
board its size.

As of 2014, the Maple board is still available from <a
href="/distributors/">distributors</a>, and we continue to integrate the
off-the-shelf boards in new projects, but no future hardware revisions are
planned and the IDE will not be ported to newer operating systems.

<a href="/docs/hardware/maple-mini.html">
<img style="float: left; border: 2px black solid; margin-left: 0px; width: 200px;"
 src="/static/images/maple_mini_breadboard.jpg" alt="maple mini gerber" /></a>
<br>
<ul style="float:right;margin-right:0px;width:250px;">
 <li>Dual <b>I2C</b> and <b>SPI</b> ports 
 </li><li>3 USART Serial ports
 </li><li>7-channel <b>DMA</b> 
 </li><li>Low power and sleep modes 
 </li><li>Dimensions: 2.02" x 0.72"
 </li><li>Extensive <a href="/docs/hardware/maple-mini.html">documentation</a>
 </li><li><a href="https://github.com/leaflabs/maplemini">Design files</a> under
          <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>
</li></ul> 
<ul style="margin-left: 240px;"> 
 <li>STM32F103RCBT6: a <b>32-bit</b> ARM Cortex-M3 microprocessor at <b>72Mhz</b> 
 </li><li><b>20KB</b> RAM and <b>128KB</b> Flash 
 </li><li>Dedicated <b>USB</b> port for programming and communications 
 </li><li>34 General Purpose pins 
 </li><li><b>9 Analog</b> inputs at 12-bit resolution 
 </li><li><b>12 PWM pins</b> at 16-bit resolution 
</li></ul> 
</div>


<br><br>
<div style="clear: both;">
<h2><a name="maplenative" href="/docs/hardware/maple-native-beta.html">Maple Native</a>
&nbsp;<span class="devicesubtitle">Deluxe STM32 Microcontroller Board</span></a>
<span class="devicestatuscanceled">Canceled</span>
</h2>
<hr>

The Maple Native featured hardware similar to the <a href="#maple">Maple's</a>,
but was designed to fully exploit the powerful STM32F103 line. With twice as
many pins, an additional megabyte of on-board RAM, and support for true analog
output, the Maple Native design can easily handle extremely demanding tasks.

A <a href="/2011/09/maple-native-arriveth/">beta run</a> of Maple Native boards
was sold in Fall 2011, and support was added
to libmaple and the Maple IDE. Many design lessons were learned, and following
the release of even more powerful STM32 chips, work on the Maple Native stopped
and LeafLabs began designing a new "Maple II" board from scratch.

Design files and <a href="/docs/hardware/maple-native-beta.html">documentation</a>
for the Maple Native Beta boards are, of course, still available.

<a href="/docs/hardware/maple-native-beta.html">
<img style="float: left; border: 2px black solid; margin-left: 25px; width: 150px;"
 src="/static/images/devices/maple_native_photo_150.jpg" alt="maple native" /></a>
<br>
<br>
<br>
<ul style="float:right;margin-right:0px;width:250px;">
 <li>2x <b>I2C</b>, 3x <b>SPI</b> ports 
 </li><li>5 U(S)ART Serial ports
 </li><li>12-channel <b>DMA</b> 
 </li><li>High-density FSMC Pinout
 </li><li>Low power and sleep modes 
 </li><li>Integrated LiPo Battery Charging
 </li><li>Dimensions: 4" x 2.1"
 </li><li>Extensive <a href="/docs/hardware/maple-native-beta.html">documentation</a>
 </li><li><a href="https://github.com/leaflabs/maplenative">Design files</a> under
          <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>
</li></ul> 
<ul style="margin-left: 240px;"> 
 <li>STM32F103ZET6: a <b>32-bit</b> ARM Cortex-M3 microprocessor at <b>72Mhz</b> 
 </li><li><b>64KB + 1MB</b> RAM and <b>512KB</b> Flash 
 </li><li>Dedicated <b>USB</b> port for programming and communications 
 </li><li>106 General Purpose pins 
 </li><li><b>21 Analog</b> inputs at 12-bit resolution 
 </li><li><b>2 DAC </b> outputs at 12-bit resolution 
 </li><li><b>17 PWM pins</b> at 16-bit resolution 
</li></ul> 
</div>


<div style="clear: both;">
<br><br>
<h2><a name="other" >Other Past Projects</a>
<span class="devicestatuscanceled">Canceled</span>
</h2>
<hr>

A ground-up redesign of the Maple product line began in 2011, starting with the <b>Maple
II</b>. The Maple II was move to the Cortex-M4 series of
STM32 microcontrollers (<a
href="http://www.st.com/web/catalog/mmc/FM141/SC1169/SS1577/LN11/PF252148">STM32F407ZE</a>),
which feature floating-point acceleration as well as additional peripherals and
significant RAM and flash memory increases. We left behind the Arduino shield
pin headers and added a medium-density connector for expansion, switched to a
secondary <a href="http://www.blacksphere.co.nz/main/blackmagic">Black Magic
Probe</a> style port for programming and debugging (using a secondary WizNet
microcontroller), and began work on fresh IDE using the Wiring 1.0 codebase.
The Maple II hardware was prototyped (<a
href="https://github.com/leaflabs/Maple-II">design files available</a>), but we
found it economically unfeasible to undertake another large productization and
manufacturing effort.

For those looking for contemporary (circa late 2013) ARM microcontroller
development platforms, the <a href="http://armstrap.org">Armstrap</a>, <a
href="http://www.pjrc.com/store/teensy3.html">Teensie 3.0</a> (most mature),
and <a href="http://mchck.org">MCHCK</a> projects are compelling, and of course
STmicro, TI, and Freescale sell very low-cost development boards for Cortex-M4F
microcontrollers.

The <b>Oak</b> product line planned to combine microcontrollers with low-end
FPGAs. An STM32 Cortex-M3 would be attached to a 250k gate Xilinx Spartan 3E.
Oak would be a full featured processing platform suitable for robotics, machine
vision, surveillance, gaming, and a host of other applications. For users who
are unfamiliar with programming FPGAs, LeafLabs would offer a library of
pre-compiled FPGA cores (with C interface libraries) to implement common tasks
which could be achieved with the microcontroller on it's own. A <a
href="https://github.com/leaflabs/oak">hardware design</a> was prototyped in
2012 and had basic functionality, but no integrated development environment was
implemented. Cypress Semiconductor now sells a "programmable SoC" line of chips
which those interested in this sort of device might want to look at.

<b>Willow</b> was intented to be a high-performance ARM microprocessor plus
FPGA board with applications in real-time machine vision, algorithm
acceleration, and robotic motion control. Early research with the NVidia Tegra
line of processors was promising, but the industry has moved forward
significantly in recent years (eg, see the Xilinx Zynq and comparable Altera
chipsets) and it is unlikely this project will be pursued. The <a
href="http://parallella.org">Parallela</a> project builds a compelling board for
folks interested in this field.

</div>

<br>
<div style="clear: both;">
<h2><a name="future">Future Devices</a>
<span class="devicestatusdev">In Development<span style="font-weight: normal;">&#8253;</span></span>
</h2>
<hr>

LeafLabs continues to work extensively in the open hardware digital electronics
space, particularly leveraging FPGA programmable logic. We intend to release
several projects in 2014, and may yet return to sling the occasional atom in
addition to plain old bits and bytes.

</div>

<br>
