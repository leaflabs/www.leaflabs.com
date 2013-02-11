Title: Wizzin through the Ether... net
Date: 2011-10-18 12:12
Author: Cospan
Category: Projects

We got our hands on a few [WIZ820io][]s:

[![][]][]

</p>
This nifty little beast lets you connect to your [Maple][] to the
network. With one [SPI][] and three digital [IO][]s, you have the whole
Internet in your hands.

So what's this good for?

Sometimes, when you're working on a project, you'll need a user
interface. If you are the only person interfacing with your project, you
can throw together a simple [serial][] protocol, where you type a
command in the form of a character and then read back a character
response. For more elaborate projects, you might find that you want to
send longer commands to your device, read back more comprehensive
results, or simply present a more beautiful interface. We wanted
programmers to be able to generate interfaces that would be simple to
use and easily extendable. To that end, we've ported and expanded two of
Wiznet's sample projects – a [telnet interface][] and a [web server][] –
for the [Maple IDE][] and [command line toolchain][].

The telnet interface offers a great balance between control and
flexibility. Here's a screenshot of a telnet session with a [Maple
Mini][]:

[![][1]][]

</p>
Maybe the command line isn't your thing. Well, web servers are always
cool, with their buttons and text boxes. Here's an example web server
(note: originally a different name was on top, but the legal department
advised against it):

[![][2]][]

</p>
Here's what happens when you press "search":

[![][3]][]

</p>
There are many ways in which this design can be expanded, and it's a fun
way to get into HTML. The user input is not just limited to reading
text. You can also use forms with check boxes, radio buttons or combo
boxes.

Want to try this out for yourself? The [wizEthernet][] wiki page will
help you get started. We're looking forward to seeing all the beautiful
websites everyone cooks up with this!

Here's our Maple Mini web server:

[![][4]][]

</p>

  [WIZ820io]: http://www.wiznet.co.kr/Sub_Modules/kr/product/Product_Detail.asp?cate1=5&cate2=42&cate3=0&pid=1160
  []: http://www.wiznettechnology.com/Admin_Root/UpLoad_Files/ProductImgs/Dtl_1161_20110919151726.jpg
    "El dios de la internet"
  [![][]]: http://www.wiznettechnology.com/Sub_Modules/en/product/Product_Detail.asp?cate1=&cate2=&cate3=&pid=1161
  [Maple]: http://leaflabs.com/docs/hardware/maple.html
  [SPI]: http://leaflabs.com/docs/spi.html
  [IO]: http://leaflabs.com/docs/gpio.html
  [serial]: http://leaflabs.com/docs/lang/api/serialusb.html#lang-serialusb
  [telnet interface]: http://www.wiznet.co.kr/UpLoad_Files/ReferenceFiles/W5200_Telnet_AN_v1.0_en.pdf
  [web server]: http://www.wiznet.co.kr/UpLoad_Files/ReferenceFiles/W5200_TCP_AN_v1.0_en.pdf
  [Maple IDE]: http://leaflabs.com/docs/ide.html
  [command line toolchain]: http://leaflabs.com/docs/unix-toolchain.html
  [Maple Mini]: http://leaflabs.com/docs/hardware/maple-mini.html
  [1]: http://leaflabs.com/wp-content/uploads/2011/10/telnet_session.png
    "telnet_session"
  [![][1]]: http://leaflabs.com/2011/10/wizzin-through-the-ether-net/telnet_session/
  [2]: http://leaflabs.com/wp-content/uploads/2011/10/maple_search_start4-770x451.png
    "maple_search_start"
  [![][2]]: http://leaflabs.com/2011/10/wizzin-through-the-ether-net/maple_search_start-5/
  [3]: http://leaflabs.com/wp-content/uploads/2011/10/maple_search_result4-770x451.png
    "maple_search_result"
  [![][3]]: http://leaflabs.com/2011/10/wizzin-through-the-ether-net/maple_search_result-5/
  [wizEthernet]: http://wiki.leaflabs.com/index.php?title=WizEthernet
    "wizEthernet Wiki"
  [4]: http://leaflabs.com/wp-content/uploads/2011/10/wizEthernet-770x575.jpg
    "wizEthernet"
  [![][4]]: http://leaflabs.com/2011/10/wizzin-through-the-ether-net/wizethernet/
