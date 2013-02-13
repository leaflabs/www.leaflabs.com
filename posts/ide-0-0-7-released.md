Title: IDE 0.0.7 Released!
Date: 2010-10-04 05:17
Author: mbolivar
Category: Uncategorized

Well, it's a few days late, but the version 0.0.7 of the [Maple IDE][]
is finally out!  This release contains many bugfixes, and brings us much
closer to full Arduino compatibility.  New features include:

-   [micros()][] is implemented.
-   External interrupts ([attachInterrupt()][]/[detachInterrupt()][])
    are implemented (see the [external interrupts reference page][] for
    more information).
-   Initial ports of the [Wire][] and [LiquidCrystal][] (thanks,
    [AndyScott][]!) libraries (see the [libraries reference page][] for
    more information).
-   support for `PWM_OPEN_DRAIN` in [pinMode()][]`.`
    <p>
    </code>
-   [Improved reset on OS X][].
-   Libmaple support for enabling and disabling the SysTick timer via
    `systick_disable()` and `systick_resume()` in [`systick.h`][] (see
    Section 4.4 of the [STM32F10xx programming manual][] for more
    information about SysTick).  Paired with [SerialUSB.end()][], this
    means you can now use the Maple for timing-critical code  (more on
    this in an upcoming blog post!).

Barring any emergency bugfix releases, this is the last time our  IDE
release will be a fork of the standard [Arduino IDE][].  Working with
the Arduino code was an awesome way for us to get started, but we're now
well along on a fresh rewrite, which will be more stable, flexible, and
featureful than our current version.  The new version to be released as
0.1.0; expect it to have ports for the last [remaining][]
[unimplemented][] [Arduino][] [core][] [language][] [functionality][].

As always, feedback on the [forums][] is always welcome!

  [Maple IDE]: http://leaflabs.com/docs/maple-ide/
  [micros()]: http://arduino.cc/en/Reference/Micros "micros()"
  [attachInterrupt()]: http://arduino.cc/en/Reference/AttachInterrupt
    "attachInterrupt()"
  [detachInterrupt()]: http://arduino.cc/en/Reference/DetachInterrupt
    "http://arduino.cc/en/Reference/DetachInterrupt"
  [external interrupts reference page]: http://leaflabs.com/docs/maple-ide/external-interrupts/
    "external interrupts reference page"
  [Wire]: http://arduino.cc/en/Reference/Wire "Wire"
  [LiquidCrystal]: http://arduino.cc/en/Reference/LiquidCrystal
    "LiquidCrystal"
  [AndyScott]: http://github.com/AndyScott
  [libraries reference page]: http://leaflabs.com/docs/maple-ide/libraries/
    "libraries reference page"
  [pinMode()]: http://arduino.cc/en/Reference/PinMode
  [Improved reset on OS X]: http://github.com/leaflabs/libmaple/commit/bdb85a454917a6e875c77ae12f9fd67961aebfae
  [`systick.h`]: http://github.com/leaflabs/libmaple/blob/master/libmaple/systick.h
  [STM32F10xx programming manual]: http://www.st.com/stonline/products/literature/pm/15491.pdf
    "programming"
  [SerialUSB.end()]: http://github.com/leaflabs/libmaple/blob/master/wirish/usb_serial.h#L40
  [Arduino IDE]: http://arduino.cc/en/Main/Software
  [remaining]: http://arduino.cc/en/Reference/AnalogReference
  [unimplemented]: http://arduino.cc/en/Reference/Tone
  [Arduino]: http://arduino.cc/en/Reference/NoTone
  [core]: http://arduino.cc/en/Reference/PulseIn
  [language]: http://arduino.cc/en/Reference/Interrupts
  [functionality]: http://arduino.cc/en/Reference/NoInterrupts
  [forums]: http://forums.leaflabs.com/
