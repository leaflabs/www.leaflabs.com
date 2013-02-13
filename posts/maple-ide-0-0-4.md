Title: Maple IDE 0.0.4
Date: 2010-06-02 14:43
Author: poslathian
Category: Uncategorized

We're working to improve the IDE, unkink the kinks, and support the
unsupported as quickly as possible and have been pushing a lot of new
builds. The current version is 0.0.4. In this version we have modified
(slightly) the reset-over-serial sequence that should do away with a lot
of the extraneous RXTX errors and perhaps allow you to reduce your
programDelay setting in the preferences. Most users report consistently
successful builds with programDelay set between 600 and 1200. We changed
the default setting to 1200, but if you have installed the ide before,
youll need to manually change this parameter from the file menu, since
your existing preferences take precedence.

We're close to having a Mac OSx build for both 64 and 32 bit machines,
the blocking issues now are testing and some modifications to the build
for arm-gcc. If you have arm-gcc working in Leapord or Snow Leapord, let
us know!

We've also been cleaning up error reporting, the examples repo, and the
serial port menu (linking ttyACMx with ttySx in linux is no longer
required). We've been crunching through our tickets and will continue to
release builds at a near-nightly pace.

In other news, we got proof of assembly on our next batch of Maples,
they should be here shortly. We're simultaneously excited and irked that
we ran out of stock so quickly last week, but we have way more on the
way! For those of you who hate paypal (we understand) or would rather
avoid international shipping, we're working on getting some distributor
options in place and we'll keep you posted. If you are a distributor,
drop us a line!

Thanks all for now. Let us know how its going and tell us about your
projects/plans!
