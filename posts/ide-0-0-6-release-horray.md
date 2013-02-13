Title: IDE 0.0.6 Release, Horray!
Date: 2010-07-22 22:59
Author: bnewbold
Category: Uncategorized

It's been a long week coming, but the latest/greatest version of the IDE
has been released; get it now from the [install][] page or the following
direct links. If you're upgrading, you can just back up your old IDE
directory and extract the archive to the same place.

-   Windows XP
    32-bit: [http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-windowsxp32.zip][]
-   Linux
    32-bit: [http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-linux32.tgz][]
-   Linux
    64-bit: [http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-linux64.tgz][]
-   Mac OSX 10.6
    32-bit: [http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-macosx-10_6.dmg][]

Most of the changes were in libmaple; the primary focus was on fixing
SerialUSB issues (blocking and autoreset), squashing bugs, and adding
interrupt support to the hardware timers.

**Fixed SerialUSB.print() blocking issue:**
Usercode would frequently not run when disconnected from a serial port
monitor; now it should at least run slowly. See [USB docs][] for more
details; in the long run we intend to add even more flexibility here.

**Changed USB reset scheme:**
Hopefully fixes some issues with auto-reset on Windows XP.

**init() called earlier (thanks xttocs!):**
This should help porting some libraries.

**New Makefile scheme for libmaple:**
Smarter, less magical, rules based Makefile system.

**Improved udev rule:**
Hopefully fixes some issues for Ubuntu 10.04 users.

**SerialN.end() and SerialN.flush() methods:**
By popular request!

**New Timer class for configuring interrupts with the hardware timers:**
Whole bunch of goodness! See the [docs][].

**More:**
Many documentation updates, new highlighted keywords, and examples for
[Serial passthrough][], the timers, SerialUSB, and [crude VGA][].

For a complete list of changes see these github changelogs for [the IDE][] and
[libmaple][].

Please post your successes, failures, comments, and condolences in [this forum
thread][], and have a productive weekend!

[install]: /docs/maple/install/
[http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-windowsxp32.zip]: http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-windowsxp32.zip
[http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-linux32.tgz]: http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-linux32.tgz
[http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-linux64.tgz]: http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-linux64.tgz
[http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-macosx-10_6.dmg]: http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.6-macosx-10_6.dmg
[USB docs]: /docs/maple/usb/
[docs]: /docs/maple/timers/
[Serial passthrough]: http://leaflabs.com/2010/07/serial-usb-passthrough/
[crude VGA]: http://www.flickr.com/photos/48069758@N08/4734657030/
[the IDE]: http://github.com/leaflabs/maple-ide/compare/0.0.5...v0.0.6
[libmaple]: http://github.com/leaflabs/libmaple/compare/v0.0.5...v0.0.6
[this forum thread]: http://forums.leaflabs.com/topic.php?id=106
