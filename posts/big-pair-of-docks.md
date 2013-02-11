Title: Big Pair of Docks
Date: 2010-05-10 18:00
Author: Bnewbold
Category: Uncategorized

I've been clickity clacking away on a new website and documentation; you
can see a draft of the documentation (via the great github pages
feature) [here][].

We've got a batch of boards back and want to get them on sale as soon as
possible! We had one last minor error which was placing 6v voltage
regulators and input capacitors instead of the spec'd 16v (for 18v
tolerance after a 2v diode drop). We decided to swap out the parts by
hand instead of shipping incorrect boards. The risk is that we would
damage the board while doing the solder rework, but we've been pretty
careful and will run tests before sending anything off.

The last hurdle before these boards go on sale is polishing up the new
bootloader: "newboot". We changed the way the DFU bootloader and
USB-Serial code interact; previously the bootloader configured serial
emulation during startup and left it around for usercode to take
advantage of, now the usercode will have to reconfigure the USB
peripheral. We made the change so the Maple would be more cross-platform
compatible, but it also cleans up our code and should make it clearer
how to program the device to act as alternative USB devices. One
downside is that uploading from the command line is a little trickier; a
special serial command has to be sent to initiate auto-reset.

People with rev1 Maple boards (with the "oldboot" bootloader) will have
a number of options. Very soon now we'll release a stable version of the
IDE compatible with the old bootloader that should work on most
platforms. If you would like to upgrade to the new bootloader and you
have a compatible JTAG device, you can ask us for the appropriate BIN
file (or just grab [the source][]and compile it yourself). Lastly, you
could ship us back the device and we'll reflash it for you... or if
you're in the Cambridge, MA area we can probably make a house call by
bike!

  [here]: http://leaflabs.github.com/maple-ide/build/shared/reference/
  [the source]: http://github.com/leaflabs/maple-bootloader/tree/newboot
