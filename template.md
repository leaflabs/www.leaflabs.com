Title: Blog Template Post!
Date: 2000-01-01 12:12
Author: staff
Slug: blog-template-post
Status: draft

This is a template file useful to copy for new blog posts. It demonstrates some
Markdown syntax features like Linking to an [external site](http://eff.org) or
an [internal page](/about/) or using HTML style 
<a href="http://daringfireball.net/projects/markdown/syntax">links</a>. There
is also a sort of [obnoxious][] footnote style for links (see bottom of source
for link definition.

You can **bold stuff** or *italicize it*. Put stuff<sup>up</sup> there or
down<sub>here</sub>.

- make
- a list
- of items

or

<ol>
 <li>use HTML
 <li>lists
 <ul>
   <li>intead
   <li>for complicated
   <li>stuff
 </ol>
 <li>sweet
</ol>

**Bold:** list of

**Punchy:** items you want to pull out, like features

Embed an image HTML style:

<center>
<img src="/static/images/old/2011/08/maple-c112-295x300.png">
<br>With an optional caption...
</center>

Or markdown style:

<center>
![weird image][]
</center>

Having a long line of <a
href="mailto:you@internet.com">HTML</a> which
results in a tag spanning two lines is bad, so do it 
<a href="mailto:you@internet.com">like this</a>
or even in a contrived way <a href="mailto:you@internet.com">like this
</a> instead.

Some command line mojo:

    :::text
    $ tree notes/
    notes/
    ├── dac.txt
    ├── dma-stm32f1.txt
    ├── exti.txt
    ├── fsmc.txt
    ├── interrupts.txt
    ├── pin-definitions.txt
    ├── portable.txt
    ├── stm32.txt
    ├── timers.txt
    ├── usb.txt
    └── vga.txt

Some libmaple code:

    :::c++
    // Blinks the built-in LED

    #include <wirish/wirish.h>

    void setup() {
        pinMode(BOARD_LED_PIN, OUTPUT);
    }

    void loop() {
        togglePin(BOARD_LED_PIN);
        delay(100);
    }

    __attribute__((constructor)) void premain() {
        init();
    }

    int main(void) {
        setup();

        while (true) {
            loop();
        }
        return 0;
    }

Inline YouTube video example:

<center>
<object width="500" height="281"><param name="movie" value="http://www.youtube.com/v/SQVLaHIw_TY?version=3&#038;feature=oembed"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/SQVLaHIw_TY?version=3&#038;feature=oembed" type="application/x-shockwave-flash" width="500" height="281" allowscriptaccess="always" allowfullscreen="true"></embed></object>
</center>

<!-- comments like this WILL end up in the output HTML source -->

  [weird image]: /static/images/distributors/200px-Sparkfun_logo.png
  [obnoxious]: http://www.urbandictionary.com/define.php?term=obnoxious

