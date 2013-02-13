Title: Maple IDE 0.0.12
Date: 2011-09-14 06:23
Author: jessb
Category: Uncategorized
Slug: maple-ide-0-0-12

Maple IDE 0.0.12 is now available for your pleasure.

-   [Windows XP (32-bit)][]
-   [Linux (32-bit)][]
-   [Mac OS X Snow Leopard][]

Changelog
---------

### New Stuff

-   Support for [Maple Native Beta][]. The Native's SRAM chip is turned
    on and accessible by default.
-   Dynamic memory allocation working on all boards.
-   [FreeRTOS support.][]
-   [HardwareSPI:][] pin accessor functions nssPin(), mosiPin(),
    misoPin(), and sckPin() added.
-   Vastly improved documentation for the low-level [libmaple][]
    library.

### Bugfixes

-   [HardwareTimer::setPeriod()][] fixed (broken due to a typo in the
    last release).
-   Various fixes to low-level timer support in [timer.c][].
-   RAM builds working again on all boards. (RAM builds were broken on
    the RET6 boards, see the relevant forum thread [here.][]

### Miscellaneous

-   [stm32.h][] expanded (and its declarations are more respected
    elsewhere in the codebase). This makes libmaple more portable to
    more ST chips.
-   Optimized [EXTI][] and timer IRQ handlers.
-   [Git][] tags have gone back to "vX.Y.Z" naming conventions, so
    "v0.0.12-maintenance" isntead of "0.0.12-maintenance". This seems to
    be more common practice, and it's what we used to do. The old
    branches and tags will still be around, but we'll keep using the new
    conventions from now on.

### Command line toolchain

-   Library folders are added to the include path, so they can be
    included directly.
-   Documentation sources were removed and broken out into their own
    [repository.][]
-   New examples added, others improved.

### Deprecations

-   [usart.h][] rx\_buf field in struct usart\_dev is deprecated.<br>
    The pointer is accessible via the rb field, so rx\_buf is redundant.
    Having it at all implies that sizeof(struct usart\_dev) is not a
    compile-time constant, which is undesirable. It also makes it
    impossible to dynamically allocate or reassign the buffer used by
    the rb field. This field will be removed in the next release.
-   [stm32.h][] PCLK1, PCLK2, and NR\_INTERRUPTS are deprecated. Use
    STM32\_PCLK1, STM32\_PCLK2, and STM32\_NR\_INTERRUPTS, respectively,
    instead.

Give it a test drive and let us know how it goes!

  [Windows XP (32-bit)]: http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.12-windowsxp32.zip
  [Linux (32-bit)]: http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.12-linux32.tgz
  [Mac OS X Snow Leopard]: http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.12-macosx-10_6.dmg
  [Maple Native Beta]: http://leaflabs.com/docs/hardware/maple-native-beta.html
  [FreeRTOS support.]: https://github.com/leaflabs/libmaple/tree/master/libraries/FreeRTOS
  [HardwareSPI:]: http://leaflabs.com/docs/lang/api/hardwarespi.html#lang-hardwarespi
  [libmaple]: http://leaflabs.com/docs/libmaple.html
  [HardwareTimer::setPeriod()]: http://leaflabs.com/docs/lang/api/hardwaretimer.html#lang-hardwaretimer
  [timer.c]: http://leaflabs.com/docs/libmaple/api/timer.html
  [here.]: http://forums.leaflabs.com/topic.php?id=867#post-5251
  [stm32.h]: http://leaflabs.com/docs/libmaple/api/stm32.html
  [EXTI]: http://leaflabs.com/docs/external-interrupts.html?highlight=exti
  [Git]: https://github.com/leaflabs
  [repository.]: https://github.com/leaflabs/leaflabs-docs
  [usart.h]: http://leaflabs.com/docs/libmaple/api/usart.html
