Title: KYE-cad? KEY-cad? kay-EYE-cad?
Date: 2010-06-10 01:00
Author: Jessb
Category: Uncategorized

<!--         @page { margin: 0.79in }        P { margin-bottom: 0.08in } -->So
way back when, after we announced that Maple was moving to a four-layer
design, several of you suggested that we give [KiCad][] a try. KiCad is
open source under GPL, and (unlike the free version of Eagle) plays
nicely with four-layer designs, which are both, you know, pretty good
things, so we decided to give it a whirl for the design of Maple
Native^[[1]][]^.

Overall, it went pretty well – the software is reasonably intuitive and
I didn't encounter any huge blocking issues. The assorted “getting
started” resources out there are pretty comprehensive. Obviously there
are glitches and idiosyncrasies that take some getting used to. KiCad
seems to have a large user community which was invaluable for dealing
with problems beyond the level of the readily available documentation,
but I found it to be pretty scattered which can make ferreting out
solutions difficult.

One of my biggest annoyances was the way KiCad handles via connectivity
to zones. If you're trying to connect a trace to a power plane on
another layer, you can't simply place a via to the power plane. Before
doing a zone fill on the power plane, you must go in and manually
connect all the vias on the power plane layer to one another, and then
to the zone fill, which essentially “covers” all the traces you just
drew. It's not a huge time sink, but I can't think of any reason it's a
good idea to do it this way, and it took me a long time to figure out
that yes, this is actually the way it's supposed to work.

Hotkeys also gave me some grief. I'm running KiCad in an Ubuntu VM on a
Mac (complete with silly little Mac chiclet keyboard and mouse) so a lot
of the hotkeys didn't work properly out of the box, and nobody seems to
be able to get editing the hotkeys config file to work properly. Even
lacking certain hotkeys routing was still reasonably painless, however,
which is pretty impressive. The “hug traces” function is nice.

Setting drill sizes was also sort of obnoxious. There doesn't appear to
be a way to select a via and find out and/or edit what its drill size
is. You can only choose to set it to default or alt, which means you can
only have two possible drill sizes for vias, maybe...? And changing the
default drill size seems to go back and change all the vias you've
already placed, maybe...? To be honest by this point in the design
process I had routing-brain a little too badly to figure out the
software and ended up just editing the .drl file by hand which of course
was a wee bit buggy. I'll have to better figure out how KiCad handles
drill sizes before we spin the next prototype, so if anyone has any
tricks they want to share, please do.

So what about you guys? KiCad users, weigh in!

*<a name="foot1"></a>[1]: We're getting a lot of inquiries about
timeline for Maple Native, so I just want to reiterate: we're chugging
away as fast as we can, but we don't feel comfortable committing to a
release date just yet. We've got a prototype in our hot little hands,
and right now we're at the “basic functionality” stage of testing. One
major item still on the to-do list is bringing up the FSMC bus for the
memory chip, and then, you know, fixing the myriad problems with the
board design that will undoubtedly come up during testing. Extrapolate
from that as you will.*

  [KiCad]: http://kicad.sourceforge.net/wiki/index.php/Main_Page
  [[1]]: #foot1
