Title: Maple RET6 Edition and Maple IDE 0.0.10 Beta
Date: 2011-05-12 19:52
Author: Mbolivar
Category: Uncategorized

Some great pieces of news:
<ul>
<li><a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/maple-ide-install.html">Maple IDE 0.0.10 Beta is out!</a></li>
<li><a href="/store">Headerless Maples and the Maple RET6 Edition are on sale!</a></li>
</ul>

One of our goals with <a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/libmaple.html">libmaple</a> and the Maple IDE is to support ST's rather extensive line of 32 bit Cortex M3 processors. Towards this end, and with the community's input, libmaple has been completely refactored over the past few months. This work is finally ready for <a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/maple-ide-install.html">a beta release</a>!

To demonstrate libmaple's newfound flexibility, we have also decided to put a new board on sale, the <a href="http://leaflabs.com/devices/">Maple RET6 Edition</a>. This more powerful processor has over 3 times the RAM and 4 times the Flash memory than the processor on the Maple. Thanks to the refactor effort, we were able to easily add support for this new chip into the Maple IDE. We are only making a limited number of these Maple RET6 Edition boards, so <a href="http://leaflabs.com/store">go buy one!</a> More info after the jump.
<!--more-->

The Maple is based around the STM32F103RBT6 ("RBT6") processor. This processor is what gives Maple 20KB RAM, 128KB Flash, and all the great peripherals you are (by now) used to using. There is another chip, however, that will likely one day take the RBT6's place: the STM32F103RET6 ("RET6"). The RET6 has over 3 times the RAM (64KB), 4 times the Flash memory (512KB), and many additional peripherals (like DACs!) not present on the RBT6. 

We haven't yet made a new Maple board based around the RET6.  However, the RET6 is completely pin compatible with the older RBT6, so we have produced a limited run of boards where in place of the RBT6, we have substituted the RET6 processor.  The accompanying IDE 0.0.10 beta release includes support for this new Maple RET6 Edition.

But that's not all that's new, not by a long shot.  A lot has happened since 0.0.9 came out.  The most important change is the bottom-up <a href='http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/libmaple.html'>refactoring and documentation</a> of the low-level <a href='https://github.com/leaflabs/libmaple/'>libmaple</a> library.  However, there have been a variety of other changes; a detailed changelog follows.

Try it out and let us know how it goes:

<ul>
<li><a href="http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.10beta-linux32.tgz">Linux 32-bit</a></li>
<li><a href="http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.10beta-macosx-10_6.dmg">OS X Snow Leopard</a></li>
<li><a href="http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.10beta-windowsxp32.zip">Windows XP (32-bit)</a></li>
</ul>

If you have any problems, let us know in the <a href="http://forums.leaflabs.com">forum</a>.  Once we've finished a <a href="http://wiki.leaflabs.com/index.php?title=Blocking_Changes">few more odds and ends</a>, well put the official release out there.

<h2>Changelog</h2>

<h3>Maple IDE</h3>
<ul>
<li>Support for Maple RET6 Edition</li>
<li>Various keyword highlighting additions to reflect changes to libmaple.</li>
</ul>

<h3>Wirish</h3>

<ul>
<li><a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/libs/servo.html">Servo library</a>
<ul>
<li>Servo::attach() made more flexible.  It now optionally takes a minimum and maximum target angle, with negative values allowed.  This allows, for example, making the midpoint of the pulse width interval correspond to 0 degrees, and the minimum and maximum correspond to -90 and 90 degrees, respectively.  This is a backwards-compatible and Arduino-compatible change.</li>
<li>Servo::attached() bugfix</li>
<li>Servo::write() now only takes an angle (large values are not treated as pulse widths).  This breaks compatibility with the previous release and an undocumented Arduino misfeature.</li>
<li>New method: Servo::attachedPin()</li>
</ul>
</li>
<li><a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/libraries.html#id2">LiquidCrystal</a> library: speed optimizations; should run significantly faster now.
</li>
<li><a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/shiftout.html">shiftOut()</a>: Exposed and documented.
</li>
<li><a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/serialusb.html">SerialUSB</a>: increased reliability, but there's still work to do here.
</li>
<li><a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/disabledebugports.html">disableDebugPorts()</a> and <a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/enabledebugports.html">enableDebugPorts()</a>: used respectively to disable and enable the built-in Cortex M3 <a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/jtag.html">JTAG</a> and Serial Wire Debug hardware peripherals.  This increases the number of available GPIOs on the Maple by five (up to 44!).
</li>
<li>A variety of board-specific values were introduced; see <a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/board-values.html">associated documentation</a>; also see Examples > Maple > InteractiveTest for example usage.
</li>
<li>Maple RET6 Edition support</li>
<li><p>Bug fixes when printing 64-bit integer types and doubles.</p>
        <p>Our Print implementation was borrowed from Arduino, where long is the largest integral type.  On the STM32, however, a long occupies 4 bytes, while a long long occupies 8.  Thus, eight byte integers were not printed correctly.  This issue has been fixed.</p>
        <p>The previous implementation also behaved very badly where doubles with large absolute value were concerned.  For example, numeric_limits&lt;double&gt;::max() (which is approximately 1.7 * 10^38) was printing as -1.21474836472147483647!  We've changed the behavior so that these sorts of values print as "&lt;large double&gt;" and "-&lt;large double&gt;".  This will cause host-PC side parsers to crash or report errors, rather than silently process incorrect values.</p>
    </li>
    <li><p><a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/hardwaretimer.html">HardwareTimer</a>: Changes were made which break compatibility with 0.0.9.  In particular, because of changes made to the low-level timer library, the timer_dev_num type and the getTimer() function no longer exist.  Be very careful when converting old timer code that used either one of these, as, for example, <tt>TIMER1</tt> means something very different now than it did in 0.0.9.</p>
        <p>Many other methods were also deprecated; however, their functionality has been taken over by other ones.  The HardwareTimer interface is still not finished, and should be considered experimental until further notice.</p>
    </li>
    <li><a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/hardwarespi.html#lang-hardwarespi">HardwareSPI</a>: Slave mode support!  Additionally, some old functions were deprecated, with better ones taking over their functionality.
    </li>
</ul>

<h3>libmaple Proper</h3>

<ul>
    <li><a href="https://github.com/leaflabs/libmaple">libmaple</a> has been completely refactored.  Its interfaces are now <a href="http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/libmaple/apis.html">officially documented</a> (though the best documentation is still currently in the source code) and stable.  Any future changes which break backwards compatibility will go through a deprecation period first.
    </li>

    <li><em>New</em>: Support for the following peripherals and processor features:

        <ul>
            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/i2c.h">i2c.h</a> Inter-Integrated Circuit (I2C)</li>

            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/dma.h">dma.h</a> Direct Memory Access (DMA) (initial implementation by Michael Hope)</li>

            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/dac.h">dac.h</a> Digital-to-Analog converter (DAC)</li>

            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/iwdg.h">iwdg.h</a> Independent watchdog (IWDG) (initial implementation by Michael Hope)</li>

            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/bkp.h">bkp.h</a> Backup registers (BKP)</li>

            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/pwr.h">pwr.h</a> Power domain (PWR)</li>

            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/fsmc.h">fsmc.h</a> Flexible Static Memory Controller (FSMC)</li>

            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/scb.h">scb.h</a> System Control Block (SCB)</li>

            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/bitband.h">bitband.h</a> better interface for functionality previously in util.h</li>

            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/stm32.h">stm32.h</a> future basis for MCU-specific configuration</li>

            <li><a href="https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/delay.h">delay.h</a> base delay_us() implementation, pulled from Wirish.</li>
        </ul>
    </li>

    <li>Other changes:
