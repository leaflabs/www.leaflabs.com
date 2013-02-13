Title: Maple on Mac OS X!
Date: 2010-01-13 22:12
Author: Bbradlyn
Category: Uncategorized

<center>
<img src="http://blogs.leaflabs.com/wp-content/uploads/maplepic-1024x640.jpg" width="700px;">
</center>

With revision 115, the maple IDE works on OS X 10.5, provided you use an
external power source (due to the dfu problems mentioned above. To build
it, make sure you have developer tools installed. There is an external
dependency on two GNU libraries, gmp and mpfr. These can be obtained
through macports.

First, go to [http://www.macports.org/][] and follow the installation
instructions. Then open a terminal and type

    sudo port install mpfr

This should install libgmp and libmpfr. Next, check out the code
repository at [http://code.google.com/p/leaflabs][]

open up a terminal, change to the directory

    leaflabs/trunk/maple/build/macosx

and then run appbuild.sh

this will create the application for you and place it into the work
directory ready for use.

To flash code, first set the board to maple, and make sure your maple is
powered externally or via battery. The first time you try to flash,
things will hang up at "Claiming USB DFU Interface...". When this
happens, unplug the usb cable and plug it back in. When you next click
upload, everything should work. Ive got mine sitting here blinking right
now.

Additionally, the serial monitor works under mac. It should set itself
up automatically, but if not, once your code is running go to the
tools-\>serial port menu and select something like
"/dev/tty.usbmodem411".

Hope this works for you all. A pre-built app should be available on the
website shortly.

Unfortunately, it seems that there are problems getting libmpfr to play
nicely with Snow Leopard (OS X 10.6). We're currently looking into this,
and will let you know when we have  a fix.

  [http://www.macports.org/]: http://www.macports.org/ "http://www.macports.org/"
  [http://code.google.com/p/leaflabs]: http://code.google.com/p/leaflabs "http://code.google.com/p/leaflabs"
