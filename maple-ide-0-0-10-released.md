Title: Maple IDE 0.0.10 Released
Date: 2011-05-23 15:52
Author: Mbolivar
Category: Uncategorized

That's right, the newest release of the Maple IDE is hot out of the
oven, and ready for you to [download][].

This feature-packed release includes a ton of new stuff; see the [0.0.10
Beta post][] for all the juicy details.

Finally, a quick note: there were a few last-minute tweaks we made to
the lowest-level layers of [libmaple][] which advanced users of the
0.0.10 Beta may want to take a look at; more after the jump.

<!--more-->

Now that the release is out, the public libmaple APIs are fixed. This
means that every [officially documented][] bit of functionality in
libmaple will be present for the foreseeable future, and any changes
which break compatibility with these APIs are bugs. However, we did make
a few minor changes in between the time the 0.0.10 beta came out and the
final release.

Again, these post-beta changes only affect the very lowest levels of the
libmaple, and unless you were messing around down there, they are
unlikely to affect you at all. Here's the list:

-   adc.h: adc\_init() no longer blindly assumes you want
    RCC\_ADCPRE\_PCLK\_DIV\_6; the caller is responsible for setting the
    prescaler now, which we do at init() time.
-   gpio.h: AFIORemapPeripheral was renamed afio\_remap\_peripheral, and
    several of its enumerators changed. The previous definition did not
    allow for all possible remaps.
    </p>
    <p>
-   <div>
    i2c.h: There were a few changes to struct i2c\_dev's members:

    </p>

    1.  "volatile uint8 state" became "volatile i2c\_state state"
    2.  "uint8 clk\_line" became "rcc\_clk\_id clk\_id"
    3.  "uint8 ev\_nvic\_line" became "nvic\_irq\_num ev\_nvic\_line"
    4.  "uint8 er\_nvic\_line" became "nvic\_irq\_num er\_nvic\_line"

    </p>
    <p>
    Additionally, i2c\_init() was made public.

    </div>
    </p>
    <p>
-   rcc.h:The various XXX\_prescaler\_divider enums used as arguments to
    rcc\_set\_prescaler() were badly named. They have been renamed as
    follows:

    </p>

    1.  adc\_prescaler\_divider became rcc\_adc\_divider
    2.  apb1\_prescaler\_divider became rcc\_apb1\_divider
    3.  apb2\_prescaler\_divider became rcc\_apb2\_divider
    4.  ahb\_prescaler\_divider became rcc\_ahb\_divider

    </p>
    <p>
-   <div>
    timer.h: timer\_reg\_map\_union became timer\_reg\_map.
    Additionally, various unbearably long names were shortened:

    </p>

    1.  timer\_enable\_interrupt() became timer\_enable\_irq()
    2.  timer\_disable\_interrupt() became timer\_disable\_irq()
    3.  timer\_cc\_get\_polarity() became timer\_cc\_get\_pol()
    4.  timer\_cc\_set\_polarity() became timer\_cc\_set\_pol()
    5.  timer\_trigger\_dma\_enable\_request() became
        timer\_dma\_enable\_trg\_req()
    6.  timer\_trigger\_dma\_disable\_request() became
        timer\_dma\_disable\_trg\_req()
    7.  timer\_dma\_enable\_request() became timer\_dma\_enable\_req()
    8.  timer\_dma\_disable\_request() became timer\_dma\_disable\_req()
    9.  timer\_get\_dma\_burst\_length() became
        timer\_dma\_get\_burst\_len()
    10. timer\_set\_dma\_burst\_length() became
        timer\_dma\_set\_burst\_len()
    11. timer\_get\_dma\_base\_address() became
        timer\_dma\_get\_base\_addr()
    12. timer\_dma\_base\_address became timer\_dma\_base\_addr
    13. timer\_set\_dma\_base\_address() became
        timer\_dma\_set\_base\_addr()

    </p>
    <p>
    </div>
    </p>
    <p>

</p>

  [download]: /docs/maple-ide-install.html
  [0.0.10 Beta post]: /2011/05/maple-ret6-edition-and-maple-ide-0-0-10-beta/
  [libmaple]: /docs/libmaple.html
  [officially documented]: /docs/libmaple/apis.html
