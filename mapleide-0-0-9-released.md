Title: MapleIDE 0.0.9 Released!
Date: 2010-12-16 01:32
Author: Mbolivar
Category: Uncategorized

Hey all,

[Maple IDE 0.0.9][] just came out. Here's a changelog:

-   Revamped [documentation][]
-   Ports for more Arduino core language functions: [interrupts()][],
    [noInterrupts()][]
-   Added single-byte "B10110011" style defines, for Arduino
    compatibility
-   New core language functions: [toggleLED()][], [togglePin()][],
    [isButtonPressed()][], [waitForButtonPress()][]
-   New [timer][] methods
-   [Servo][] library
-   A community-contributed library for [EEPROM emulation][] (thanks,
    [x893][]!)

</p>
Additionally, we've added support in [libmaple][] for the Maple Mini.

We're also releasing an alpha port of the WiShield library at:

[http://static.leaflabs.com/pub/leaflabs/labs/WiShield.zip][]

[That link will move once the port is more advanced]. It's not
feature-complete, and is still buggy, but is capable of connecting to an
access point and serving a web page.

With this release out, our immediate bug targets on the software front
are the [Windows upload issue][] and the [SerialUSB bugs on large reads
and writes][].  After those critical bugs are triaged, we'll release
them as an incremental IDE release before resuming our normal
development on the upcoming serial bootloader and IDE rewrite.

On the hardware front, we're finalizing Maple Mini, and moving forward
on Oak.  More news as it happens!

  [Maple IDE 0.0.9]: http://leaflabs.com/docs/maple-ide-install.html
  [documentation]: http://leaflabs.com/docs/
  [interrupts()]: http://leaflabs.com/docs/lang/api/interrupts.html
  [noInterrupts()]: http://leaflabs.com/docs/lang/api/nointerrupts.html
  [toggleLED()]: http://leaflabs.com/docs/lang/api/toggleled.html
  [togglePin()]: http://leaflabs.com/docs/lang/api/togglepin.html
  [isButtonPressed()]: http://leaflabs.com/docs/lang/api/isbuttonpressed.html
  [waitForButtonPress()]: http://leaflabs.com/docs/lang/api/waitforbuttonpress.html
  [timer]: http://leaflabs.com/docs/lang/api/hardwaretimer.html
  [Servo]: http://leaflabs.com/docs/libraries.html#servo
  [EEPROM emulation]: http://akb77.com/g/mcu/maple-eeprom-emulation-library/
  [x893]: http://forums.leaflabs.com/profile.php?id=259
  [libmaple]: http://github.com/leaflabs/libmaple
  [http://static.leaflabs.com/pub/leaflabs/labs/WiShield.zip]: http://static.leaflabs.com/pub/leaflabs/labs/WiShield.zip
  [Windows upload issue]: http://code.google.com/p/leaflabs/issues/detail?id=8
  [SerialUSB bugs on large reads and writes]: http://code.google.com/p/leaflabs/issues/detail?id=10
