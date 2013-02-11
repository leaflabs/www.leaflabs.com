Title: libmaple: new include style on the way
Date: 2012-07-02 13:58
Author: Mbolivar
Category: Uncategorized

As noted in a previous post about [libmaple's support for new STM32
series][], there are some [deprecations][] coming. This blog post is a
heads-up about the most important one: libmaple's getting a new include
style. (We're working on making these changes unintrusive to MapleIDE
users; read on after the jump for the details). To help you migrate your
code, the old style will still work for *exactly one more* libmaple
release: it will work in v0.0.13, but will break *immediately after
that*.

So what's changing? In short, you'll need to include Wirish headers
(like wirish.h) like this:

`#include <wirish/wirish.h> // new style, works with libmaple from GitHub`

</code>

</p>
instead of like this:

`#include "wirish.h" // OLD style, now deprecated`

</p>
You'll need to include libmaple headers (like i2c.h) like this:

`#include <libmaple/i2c.h> // new style, works with libmaple from GitHub`

</code>

</p>
instead of like this:

`#include "i2c.h" // OLD style, now deprecated`

</code>

</p>
Details (including why the changes are necessary) after the
jump.<!--more-->

First off, **we don't expect many problems for IDE users**, since:

1.  [Maple IDE][]automatically includes wirish.h for all IDE code. As
    you can see from the [v0.0.12 wirish.h][], it's a mother of a header
    which pulls in almost everything the library has to offer. Because
    of that, most code written for Maple IDE doesn't need any extra
    includes. Usually, you'll only need extra includes for the low-level
    header files for libmaple proper (the C layer that lies underneath
    the Wiring/Arduino compatibility code). If you don't use these
    low-level libraries, your code will likely not need to change. If
    you *are* using those low-level interfaces, we expect that a change
    in include style probably won't trip you up ;).
2.  [Libraries][] you use from the IDE's drop-down menus insert their
    `#include` lines automatically. This means new code using libraries
    will use the new style by default. Old code will need to change to
    e.g. `#include <Servo/Servo.h>`. If this seems like a big problem to
    you, **please let us know**. We can always special-case libraries
    within the IDE so you can just include them as e.g.
    `#include "Servo.h`" if that seems like a good idea.

</p>
The new style came about for a couple of reasons:

-   It's pretty standard usage for libraries
-   It allows different header files with the same file name

</p>
The second of these is what made it worth the pain of forcing people to
migrate their code.

For example, we've got a variety of `foo.h` in libmaple now -- the main
`<libmaple/foo.h>` header, and the series-specific `<series/foo.h>`
headers in [`libmaple/stm32f1/include/`][] and
[`libmaple/stm32f2/include/`][]. This infrastructure is necessary to
make it possible to compile libmaple for multiple STM32 series (it's a
standard C trick we're borrowing from the Linux kernel, which has e.g.
the portable [\<linux/atomic.h\>][], which in turn includes a
per-architecture `<asm/atomic.h>`).

For another example, consider the [Wiring][] or [Arduino][] SPI
libraries: they're included as plain "SPI.h", which conflicts with
libmaple's [spi.h][] on case-insensitive filesystems (like those that
come with OS X and Windows). The include style change makes it possible
to have both headers available at the same time. We get questions about
the SPI library periodically from users porting Wiring or Arduino code
to Maple:  `#include "SPI.h" `works, so people naturally expect the
library to be present. But then the code mysteriously fails to compile,
and confusion reigns. Having this new include style will help people
figure out what's wrong sooner.

If you're curious about this or any of the other upcoming changes, we
encourage you to try out the new libmaple using the [command-line
toolchain][] (an IDE pre-release with the new library is still a ways
off, unfortunately). Any and all feedback is welcome; make your voice
heard on the forum, via email, etc.

  [libmaple's support for new STM32 series]: http://leaflabs.com/2012/06/major-update-experimental-stm32f2-and-f1-value-line-in-libmaple-master/
  [deprecations]: http://en.wikipedia.org/wiki/Deprecation
  [Maple IDE]: http://leaflabs.com/docs/ide.html
  [v0.0.12 wirish.h]: https://github.com/leaflabs/libmaple/blob/v0.0.12/wirish/wirish.h#L33
  [Libraries]: http://leaflabs.com/docs/libraries.html
  [`libmaple/stm32f1/include/`]: https://github.com/leaflabs/libmaple/tree/master/libmaple/stm32f1/include/
  [`libmaple/stm32f2/include/`]: https://github.com/leaflabs/libmaple/tree/master/libmaple/stm32f2/include/
  [\<linux/atomic.h\>]: http://lxr.linux.no/#linux+v3.4.4/include/linux/atomic.h
  [Wiring]: http://wiring.org.co/reference/libraries/SPI/index.html
  [Arduino]: http://arduino.cc/en/Reference/SPI
  [spi.h]: http://leaflabs.com/docs/libmaple/api/spi.html
  [command-line toolchain]: http://leaflabs.com/docs/unix-toolchain.html
