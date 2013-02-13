Title: We're teaming up with Wiring!
Date: 2011-11-03 15:14
Author: mbolivar
Category: News

Good news, everyone! LeafLabs and [Wiring][] are teaming up to make a
single IDE and libraries that will work on all of our boards!

For those who might not know about Wiring: it's an awesome open source
hardware and software project, the very first to port the Processing
environment to work with microcontrollers. Wiring was started by
Hernando Barragán of the Universidad de los Andes in Colombia, and is
headed up by him and a team of volunteers. We think Wiring is fantastic,
and we've been talking with them for a while about how we might work
together.

Well, those talks are turning into reality.  Now that Wiring is finished
with their [their 1.0 release][], we're ready to work together to move
the [Maple IDE][] over to Wiring's. This means that, in the future,
you'll be programming Maple from the Wiring IDE.

![][]

As many of you know, there are approximately twenty million Wiring IDE
forks, clones, and sister projects out there. It's like the old story
goes: Processing begat Wiring's IDE, Wiring's begat Arduino's, and
Arduino's begat LeafLabs', etc.

That's crazy! Open source history is full of examples where too much
forking drives everybody nuts, makes for a ton of wasted effort,
confusing user experiences, etc. etc. So, instead of adding to the
confusion, we're glad to be putting our efforts towards the mature,
well-tested, and continually-evolving Wiring IDE.

Well, you say, that's all motherhood and the flag, but what about the
libraries I use to program my Maple? What's going to happen to those? Am
I going to have to throw everything away? Oh noes! It's gonna be another
[Py3K][] or [Perl 6][]! Run away!

Relax. We don't want that to happen either. We're still going to
continue developing [libmaple][] on our own, and all of us at Wiring and
LeafLabs are committed to maintaining compatibility with previous
releases whenever it's possible.

However, we're not going to lie to you. The existing code was developed
for different architectures, and it's not going to be possible to
achieve 100% compatibility. We'd be selling snake oil if we told you
anything different. We're not trying to turn Maple into Wiring. Instead,
we're lovingly crafting a subset of both of our libraries that will work
the same on both of our boards.  Since "subset of both of our libraries"
is an unappetizing mouthful, we're calling it the *Wiring Framework* for
short. If you find some random code on the internet that uses only
features from the Wiring Framework, you'll know it works on both Maple
and Wiring. However, if you want to use Maple- or Wiring-specific
features, those will all still be there.

We hope you're as excited about this as we are! While it's still early
days, we'll be sure to keep you posted as things progress.

  [Wiring]: http://wiring.org.co/
  [their 1.0 release]: http://wiring.org.co/download/
  [Maple IDE]: http://leaflabs.com/docs/ide.html
  []: http://leaflabs.com/wp-content/uploads/2011/10/verify1.jpg "Wiring IDE"
  [Py3K]: http://wiki.python.org/moin/Python2orPython3
  [Perl 6]: http://dev.perl.org/perl6/
  [libmaple]: http://leaflabs.com/docs/libmaple.html
