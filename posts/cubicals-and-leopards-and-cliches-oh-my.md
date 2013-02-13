Title: Cubicles and Leopards and Cliches, Oh My!
Date: 2010-05-30 14:00
Author: bnewbold
Category: Uncategorized

What a week! We've finished finals, shipped out Maples all over the
world, moved into a new office space, saw tons of gadgets, and lived to
blog about it.

First off, it sounds like some people are having trouble getting the IDE
working with their new boards. We've put board sales on hold until we
fix some issues and will be posting progress and snapshot releases in
the forums over the next couple days. Once things are smooth we'll put
our remaining 15 boards on sale; another batch of 250 are just finishing
assembly and should be on their way to us any day, hopefully there won't
be any gaps in  availability!

Second, good news for those with a rev1 board and an FTDI chip! We've
successfuly flashed the newer (rev3) bootloader over the ST hardware
serial bootloader by applying voltage straight to the appropriate pin on
the  microcontroller. It's easier than it sounds, check out [this forum
post][] for directions and a photo. If you have trouble we'd be happy to
reflash your  board if you pay for half the shipping (we can make a
house call in the Boston, MA area!).

Another hanging chad is Mac OSX support for the IDE. The blocking issue
right now is the tangled heirarchy of [cross compiling a cross
compiler][] that will run on both 32bit and 64bit versions of Snow
Leopard and actually generate properly linked binaries for the Maple...
we've spent a lot of time playing with [fat binaries][] and have had
tons of partial success using automated build scripts, but it's going to
take one more all-nighter to cook up the right magic make sauce.

<img class="aligncenter size-large wp-image-996" title="IMG_4098" src="/static/images/old/2010/05/IMG_4098-770x513.jpg" alt="" width="770" height="513" />

Maker Faire was last weekend and I had a great time running around the
Bay Area checking out open hardware genetics hardware ([OpenPCR][]), a
sweet [DIY Liquid Nitrogen rig][], [quadrotor drones][], and [libre
yachts][]. Lots and lots of great projects out there, i'm really excited
to see what kind of real time audio effects can be pulled off with a
Maple, and to do some crazy helo tricks with all the processing done
with an on-board Oak.

<img class="aligncenter size-large wp-image-997" title="techcity" src="/static/images/old/2010/05/techcity-770x513.jpg" alt="" width="770" height="513" />

And finally, look at that hansome fellow in the snazzy new office space!
We're the first tenants in an awesome new tech incubation/business/work
space in Cambridge called [Technology City][]. We've finally got room
for all our electrical equipment and won't have to pull cat hair out of
our USB ports or explain our solder paste rig to a skeptical landlord
ever again! If you or anybody you know is looking for office or desk
space in the Central Square area have them shoot us an email, we're
hoping to fill the building with other like minded groups. There's even
a nice conference room where we can host community events and meetups!

  [this forum post]: http://forums.leaflabs.com/topic.php?id=32#post-126
  [cross compiling a cross compiler]: http://en.wikipedia.org/wiki/Cross_compiler#Canadian_Cross
  [fat binaries]: http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man1/lipo.1.html%20
  []: /static/images/old/2010/05/IMG_4098-770x513.jpg
    "IMG_4098"
  [OpenPCR]: http://www.flickr.com/photos/48069758@N08/4647944209/
  [DIY Liquid Nitrogen rig]: http://www.flickr.com/photos/48069758@N08/4647944205/
  [quadrotor drones]: http://www.flickr.com/photos/48069758@N08/4647963653/
  [libre yachts]: http://www.instructables.com/id/The-Free-Yacht-Saga/
  [1]: /static/images/old/2010/05/techcity-770x513.jpg
    "techcity"
  [Technology City]: http://www.technologycity.net
