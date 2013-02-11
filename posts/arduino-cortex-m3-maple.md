Title: Arduino + Cortex M3 = Maple
Date: 2009-07-15 20:58
Author: Poslathian
Category: Uncategorized

In the depths of the sparkfun.com product pages Occam sez: "Exactly ...
someone should port the Arduino firmware and environment to a 32-bit
ARM, preferably one of the new

Cortex-M3 variants. Can anyone say ARMDuino? It would be killer,
especially on these very fast ARM processors..."

Yes. We agree. Totally.

Armed with a cozy basement and some bad techno, arduino+arm+ development
environment is pretty much here. Were stitching the pieces together on a
project were calling Maple, the first in a line of dev boards that we've
designed to shut up those little voices in our heads that keep saying
"Wouldn't it be great if you could sketch hardware projects out in an
arduino/processing/wiring style environment that do a lot more than
blink some lights and run some motors? Audio? Video? Machine Learning?
or maybe just...WAY MORE BLINKY LIGHTS.

The Arduino ships with a 16MHz Atmega chip that just doesn't cut it for
these types of applications. The 72MHz ARM Cortex M3 chips look pretty
rad, but you really have to get your hands dirty to use them. That 5x
boost in proc speed is worth it though - say hello to audio applications
on Arduino. To be fair, I recall playing some awesome Lucas Arts games
on an old Pentium I 90MHz machine - strip out the DOS overhead, and let
there be an Arduino arcade console. We've made the Maple pinouts and dev
library fully arduino compatible so all your old projects and libraries
should play nice on the new hardware. Thanks to ST's incarnation of the
Cortex M3, Maple supports ACTUAL USB communication, not just
serial-over-usb via an ftdi chip. Accelerometer based mouse? USB audio
fx processor? A controller for your big 3d printer/latte art plotter
project? It turns out you can throw a lot more data over a USB pipe than
the old 5600 baud serial line.

Of course, Maple is just the first step. To truly get real processing
power where in belongs - on top of a pile of other electronics sitting
on your workbench - we give you Oak. Oak is essentially the Maple with a
Spartan 3e FPGA next door with some extra memory (256MB) and a blue
tooth chip. Were building a fully fledged library of HW blocks that let
the fpga grab frames from a video camera, drive your monitor or TV,
crunch some numbers in parallel for some audio processing and even do
some simple object tracking from real time video. Of course, for the
verilog-vhdl savvy, everything is open source, go nuts. But we think
FPGA's are just great, and they need to get out more. Wed love to give
FPGA development that sketch-book feel of arduino hacking.

Farther on down the line will be Willow. We're thinking of using an ARM
Cortex A8 for this board. Think Arduino - at 1 GHz. Well be throwing a
much larger 1.5M gate fpga on Willow, and are dreaming of the first
"Linux on Willow!" posts around the internet. All our boards are small
and designed to run on-board of your next robotics project, mounted
inside of a guitar pedal case,

or whatever nifty portable electronic widget you can think of.

Most of the expansion modules will be blue-tooth ready, bringing all the
cabling and wiring on your next project to a bare minimum. Of course all
those great arduino XBee and motor controller shields are still
compatible.

Did I mention everything is open source?

Let us know what you think.
