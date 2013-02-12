Title: Maple IDE 0.0.5!
Date: 2010-06-11 16:35
Author: Bnewbold
Category: Uncategorized

<img class="aligncenter size-large wp-image-1038" title="Screen shot 2010-06-10 at 2.44.47 PM" src="http://leaflabs.com/wp-content/uploads/2010/06/Screen-shot-2010-06-10-at-2.44.47-PM-770x481.png" alt="" width="770" height="481" />

New Maple IDE release today, direct links below!

This is notable as our first Mac OSX 10.6 release (finally!), and hopefully the last version before a stable and consistent 0.1.0 release. Other changes include getting rid of "HardwareUsb" (use the already-instantiated "SerialUSB" instead), a much more robust reset scheme (including a DFU search period that should fix timing issues many people were having), and a "less blocking" Serial-over-USB implementation.

Note that for the first program upload with with this new release you may have to put your Maple in "perpetual bootloader mode" by holding the BUT button immediately <em>after</em> releasing the RESET button; you would only have to do this once. More details in the linked forum post linked at the bottom.
<ul>
	<li>Windows XP 32-bit: <a href="http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.5-windowsxp32.zip">http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.5-windowsxp32.zip</a></li>
	<li>Linux 32-bit: <a href="http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.5-linux32.tgz">http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.5-linux32.tgz</a></li>
	<li>Linux 64-bit: <a href="http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.5-linux64.tgz">http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.5-linux64.tgz</a></li>
	<li>Mac OSX 10.6 32-bit: <a href="http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.5-macosx-10_6.dmg">http://static.leaflabs.com/pub/leaflabs/maple-ide/maple-ide-0.0.5-macosx-10_6.dmg</a></li>
</ul>
We tested on all the computers we had around the office but there are tons of details and incompatibilities out there, please let us know in the forums if you have any problems! I'll kick things off with some known issues in <a href="http://forums.leaflabs.com/topic.php?id=51">this thread</a>.

Have a great weekend, and happy hacking!
