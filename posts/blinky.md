Title: Blinky!!
Date: 2009-12-28 18:13
Author: poslathian
Category: Uncategorized

Happy Holidays Everyone!

We have gotten reports that Maple's are being delivered and several
users have successfully gotten Blinky style programs running from the
IDE. This is great news! Here is a short update.

We are currently working on a getting started guide, detailing how
to build/install the IDE and use it to program Maple. This being the
Holiday weekend, the timing could have been better, but we hope to have
this tutorial up late Tuesday evening. After a bit of turbulence with a
broken repository, we have migrated the latest changes to the library
into the IDE and it builds successfully on linux and windows.
Unfortunately, there remains an issue on mac OSX involving dfu-util, the
program used to load new firmware onto the STM32.

Support for using Serial.print() to write to the UART ports is complete,
however this function does not mirror the data to the USB port (which
acts as a virtual serial port on the host machine). This functionality
exists, but hasn't been integrated into the library yet.

We are working to integrate the various dependencies of the IDE into
simple installers on windows and linux, hopefully this will be completed
in the next few days. For now, however, the IDE can be built manually
from the repository at leaflabs.googlecode.com, following the standard
instructions on arduino.cc (for building the IDE). In addition, the IDE
depends on dfu-util, which can be obtained through most package
repositories for linux or from openmoko.org.

Thank you for your patience and support, we hope you enjoy getting
started with your new Maple. Please do check on the website later this
week for further updates about installers and the getting started guide.
We look forward to your feedback!
