Title: Maple Prototype
Date: 2009-08-16 18:23
Author: Okie
Category: Uncategorized

![mapleproto][] This is the Maple prototype, our first version of an
Arduino-compatible board with an STM32 ARM Cortex-M3 processor. We're
chomping at the bits to release it as soon as we tie up a couple loose
ends to make it what we think it should be. We've ported all the Arduino
language and are modifying the Arduino environment so that everything
works how it should. Notice that Maple does not have an FTDI chip, so
serial communication works through a USB Virtual COM Port that's
implemented on the STM32, so it may even be *slightly* easier to setup
than Arduino boards because FTDI drivers aren't required, and the
drivers for the Virtual COM Port are probably already on your Mac or
Linux machine; for Windows, you'll just use the driver that we include
with the software download.

We're also extending the Arduino language to allow users to do things
with the STM32 that the Atmega chips cannot do such as easy setting up
of different types of USB devices (HID for crazy mouses, mass storage,
or full speed USB 2.0 data transfer)  and other communication protocols
(USART, SPI, I2C, I2S, CAN), providing higher bandwidth capabilities.

To allow people an opportunity to experiment with the performance
benefits of Maple, we're designing a couple shields to stack on. The one
I'm most excited about is the audio shield. I love programming real-time
audio synthesis and effects processing algorithms and have experimented
with these things on Arduino. Audio processing is one thing that can
quickly lead to hitting the limitations of the Arduino AVR processors. I
like to simulate real-time audio effects processing with MATLAB (though
I'm starting to move to Python) by importing an audio file and writing
an algorithm that slides a buffer through the audio data as if it were
being captured in real-time from a guitar or something. It's
disappointing to create a cool effect that takes too much processing or
memory to implement on the embedded hardware you're using, so I can't
wait to allow people more flexibility here and for other things. Another
shield we might do is an OLED display with a little trackball or
joystick. I haven't seen an OLED display shield at a reasonable cost.
We're open to suggestions!

  [mapleproto]: http://blogs.leaflabs.com/wp-content/uploads/mapleproto.jpg
    "mapleproto"
