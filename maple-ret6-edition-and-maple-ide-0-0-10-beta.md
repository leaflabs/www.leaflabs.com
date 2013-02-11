Title: Maple RET6 Edition and Maple IDE 0.0.10 Beta
Date: 2011-05-12 19:52
Author: Mbolivar
Category: Uncategorized

Some great pieces of news:

-   [Maple IDE 0.0.10 Beta is out!][]
-   [Headerless Maples and the Maple RET6 Edition are on sale!][]

</p>

One of our goals with [libmaple][] and the Maple IDE is to support ST's
rather extensive line of 32 bit Cortex M3 processors. Towards this end,
and with the community's input, libmaple has been completely refactored
over the past few months. This work is finally ready for [a beta
release][Maple IDE 0.0.10 Beta is out!]!

To demonstrate libmaple's newfound flexibility, we have also decided to
put a new board on sale, the [Maple RET6 Edition][]. This more powerful
processor has over 3 times the RAM and 4 times the Flash memory than the
processor on the Maple. Thanks to the refactor effort, we were able to
easily add support for this new chip into the Maple IDE. We are only
making a limited number of these Maple RET6 Edition boards, so [go buy
one!][] More info after the jump.

<!--more-->

The Maple is based around the STM32F103RBT6 ("RBT6") processor. This
processor is what gives Maple 20KB RAM, 128KB Flash, and all the great
peripherals you are (by now) used to using. There is another chip,
however, that will likely one day take the RBT6's place: the
STM32F103RET6 ("RET6"). The RET6 has over 3 times the RAM (64KB), 4
times the Flash memory (512KB), and many additional peripherals (like
DACs!) not present on the RBT6.

We haven't yet made a new Maple board based around the RET6. However,
the RET6 is completely pin compatible with the older RBT6, so we have
produced a limited run of boards where in place of the RBT6, we have
substituted the RET6 processor. The accompanying IDE 0.0.10 beta release
includes support for this new Maple RET6 Edition.

But that's not all that's new, not by a long shot. A lot has happened
since 0.0.9 came out. The most important change is the bottom-up
[refactoring and documentation][libmaple] of the low-level [libmaple][1]
library. However, there have been a variety of other changes; a detailed
changelog follows.

Try it out and let us know how it goes:

-   [Linux 32-bit][]
-   [OS X Snow Leopard][]
-   [Windows XP (32-bit)][]

</p>

If you have any problems, let us know in the [forum][]. Once we've
finished a [few more odds and ends][], well put the official release out
there.

Changelog
---------

</p>

### Maple IDE

</p>

-   Support for Maple RET6 Edition
-   Various keyword highlighting additions to reflect changes to
    libmaple.

</p>

### Wirish

</p>

-   [Servo library][]

    </p>

    -   Servo::attach() made more flexible. It now optionally takes a
        minimum and maximum target angle, with negative values allowed.
        This allows, for example, making the midpoint of the pulse width
        interval correspond to 0 degrees, and the minimum and maximum
        correspond to -90 and 90 degrees, respectively. This is a
        backwards-compatible and Arduino-compatible change.
    -   Servo::attached() bugfix
    -   Servo::write() now only takes an angle (large values are not
        treated as pulse widths). This breaks compatibility with the
        previous release and an undocumented Arduino misfeature.
    -   New method: Servo::attachedPin()

    </p>
    <p>
-   [LiquidCrystal][] library: speed optimizations; should run
    significantly faster now.
    </p>
    <p>
-   [shiftOut()][]: Exposed and documented.
    </p>
    <p>
-   [SerialUSB][]: increased reliability, but there's still work to do
    here.
    </p>
    <p>
-   [disableDebugPorts()][] and [enableDebugPorts()][]: used
    respectively to disable and enable the built-in Cortex M3 [JTAG][]
    and Serial Wire Debug hardware peripherals. This increases the
    number of available GPIOs on the Maple by five (up to 44!).
    </p>
    <p>
-   A variety of board-specific values were introduced; see [associated
    documentation][]; also see Examples \> Maple \> InteractiveTest for
    example usage.
    </p>
    <p>
-   Maple RET6 Edition support
-   Bug fixes when printing 64-bit integer types and doubles.

    </p>

    Our Print implementation was borrowed from Arduino, where long is
    the largest integral type. On the STM32, however, a long occupies 4
    bytes, while a long long occupies 8. Thus, eight byte integers were
    not printed correctly. This issue has been fixed.

    </p>

    The previous implementation also behaved very badly where doubles
    with large absolute value were concerned. For example,
    numeric\_limits\<double\>::max() (which is approximately 1.7 \*
    10\^38) was printing as -1.21474836472147483647! We've changed the
    behavior so that these sorts of values print as "\<large double\>"
    and "-\<large double\>". This will cause host-PC side parsers to
    crash or report errors, rather than silently process incorrect
    values.

    </p>
    <p>
-   [HardwareTimer][]: Changes were made which break compatibility with
    0.0.9. In particular, because of changes made to the low-level timer
    library, the timer\_dev\_num type and the getTimer() function no
    longer exist. Be very careful when converting old timer code that
    used either one of these, as, for example, `TIMER1` means something
    very different now than it did in 0.0.9.

    </p>

    Many other methods were also deprecated; however, their
    functionality has been taken over by other ones. The HardwareTimer
    interface is still not finished, and should be considered
    experimental until further notice.

    </p>
    <p>
-   [HardwareSPI][]: Slave mode support! Additionally, some old
    functions were deprecated, with better ones taking over their
    functionality.
    </p>
    <p>

</p>

### libmaple Proper

</p>

-   [libmaple][2] has been completely refactored. Its interfaces are now
    [officially documented][] (though the best documentation is still
    currently in the source code) and stable. Any future changes which
    break backwards compatibility will go through a deprecation period
    first.
    </p>
    <p>
-   *New*: Support for the following peripherals and processor features:

    </p>

    -   [i2c.h][] Inter-Integrated Circuit (I2C)
    -   [dma.h][] Direct Memory Access (DMA) (initial implementation by
        Michael Hope)
    -   [dac.h][] Digital-to-Analog converter (DAC)
    -   [iwdg.h][] Independent watchdog (IWDG) (initial implementation
        by Michael Hope)
    -   [bkp.h][] Backup registers (BKP)
    -   [pwr.h][] Power domain (PWR)
    -   [fsmc.h][] Flexible Static Memory Controller (FSMC)
    -   [scb.h][] System Control Block (SCB)
    -   [bitband.h][] better interface for functionality previously in
        util.h
    -   [stm32.h][] future basis for MCU-specific configuration
    -   [delay.h][] base delay\_us() implementation, pulled from Wirish.

    </p>
    <p>
-   Other changes:

    </p>

    -   [ring\_buffer.h][]: the previous implementation had many
        problems, and was rewritten. Thanks to Michael Hope ([nzmichaelh
        on GitHub][]) for the initial rewrite.
    -   [systick.h][] systick\_resume() renamed systick\_enable()
    -   [util.h][] register read/write macros (\_\_read(), \_\_write(),
        etc.) were removed.

    </p>
    <p>

</p>

### Other

</p>

[Unix toolchain][] compiler output: more debug symbols; map file
generation.

  [Maple IDE 0.0.10 Beta is out!]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/maple-ide-install.html
  [Headerless Maples and the Maple RET6 Edition are on sale!]: /store
  [libmaple]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/libmaple.html
  [Maple RET6 Edition]: http://leaflabs.com/devices/
  [go buy one!]: http://leaflabs.com/store
  [1]: https://github.com/leaflabs/libmaple/
  [Linux 32-bit]: http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.10beta-linux32.tgz
  [OS X Snow Leopard]: http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.10beta-macosx-10_6.dmg
  [Windows XP (32-bit)]: http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.10beta-windowsxp32.zip
  [forum]: http://forums.leaflabs.com
  [few more odds and ends]: http://wiki.leaflabs.com/index.php?title=Blocking_Changes
  [Servo library]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/libs/servo.html
  [LiquidCrystal]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/libraries.html#id2
  [shiftOut()]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/shiftout.html
  [SerialUSB]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/serialusb.html
  [disableDebugPorts()]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/disabledebugports.html
  [enableDebugPorts()]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/enabledebugports.html
  [JTAG]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/jtag.html
  [associated documentation]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/board-values.html
  [HardwareTimer]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/hardwaretimer.html
  [HardwareSPI]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/lang/api/hardwarespi.html#lang-hardwarespi
  [2]: https://github.com/leaflabs/libmaple
  [officially documented]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/libmaple/apis.html
  [i2c.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/i2c.h
  [dma.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/dma.h
  [dac.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/dac.h
  [iwdg.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/iwdg.h
  [bkp.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/bkp.h
  [pwr.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/pwr.h
  [fsmc.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/fsmc.h
  [scb.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/scb.h
  [bitband.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/bitband.h
  [stm32.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/stm32.h
  [delay.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/delay.h
  [ring\_buffer.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/ring_buffer.h
  [nzmichaelh on GitHub]: https://github.com/nzmichaelh
  [systick.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/systick.h
  [util.h]: https://github.com/leaflabs/libmaple/blob/0.0.10beta/libmaple/util.h
  [Unix toolchain]: http://static.leaflabs.com/pub/leaflabs/maple-docs/0.0.10beta/unix-toolchain.html
