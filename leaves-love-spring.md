Title: Leaves Love Spring!
Date: 2010-04-26 23:59
Author: Bnewbold
Category: Uncategorized

We've been bursting forth with code and hardware as the weather
improves but have neglected to share them with you despite many emails
and conversations; thanks for all your interest!

[![maple rev3][]][]

</p>

On the top of our stack is the next batch of Maple boards, rev3. We've
got a small production batch back for testing and will have boards for
sale as soon as the full run comes back from assembly. We're toiling
away on stable versions of our bootloader, low level library, and
arduino-based IDE to be released at the same time as these boards go on
sale; you can track our development on [github][] and we look forward to
your comments and critique as once the dust settles. We've also got
a [shiny new website][] and fancy documentation in the pipeline.

We spent a whole day this past week testing the Maple rev3. The biggest
fixed issue is noise, both crosstalk between headers and digital noise
from the USB bus. The USB noise is still [detectable][], while the
crosstalk has virtually disappeared on most pins. We're collecting hard
numbers on our actual ADC (analog voltage measurement) precision and
accuracy; in theory we could get 12-bit resolution over the 0-3.3v range
but most development boards have trouble meeting the full potential of
their parts. We'll report back once we're more confident of our test
setup and peripheral configuration, but it looks pretty reasonable.

![test-prog-shot][]

As part of the testing process I wrote up an interactive testing
program which acts as a console over one of the USART serial ports and
has commands to read in GPIO status, spit out servo-compatible PWM
sweeps, dump data over the USB connection, etc. We're thinking of
including this as the default program on the rev3 Maples, what do you
think? Should we make the interface over USB instead of USART? You can
look at what we have now [here][]. In the future we're excited to see if
we can port more complete environments like [eLua][] or
[python-on-a-chip][].

[caption id="attachment\_245" align="aligncenter" width="300"
caption="Breadboarding PWM audio with the Maple"][![Breadboarding PWM
audio with the Maple][]][][/caption]

One use for high resolution ADC sampling is real time audio work! With
the right low pass filter (which can be just a couple resistors and
capacitors) the high speed PWM ports on the Maple can pump out
reasonable audio-frequency waveforms. Okie has been working on a basic
audio shield with nice active filters and other goodies.

[![Basic Audio Shield Prototype][]][]

</p>

Of course a dedicated DAC could give much higher audio fidelity, and
many microcontrollers can implement basic audio synthesis. We're
experimenting with some more computationally intensive frequency domain
effects and are planning on building a more fancy professional grade
audio shield for the Maple Native... the delux version of the Maple with
a larger header configuration and more features, which we're now
prototyping. Jess has been using an open source tool ([Kicad][]) to do
the design and layout for the Maple Native and she'll be posting about
that experience soon.

There's more going on; check out our [flicker stream][] for more photos
of testing, a [MIDI/IR theramin][], [wifi routers][], and a
[ghost][detectable] from our past soon to be reincarnated.

  [maple rev3]: http://blogs.leaflabs.com/wp-content/uploads/img_4044-Modified-300x207.jpg
    "maple rev3"
  [![maple rev3][]]: http://www.flickr.com/photos/48069758@N08/4556644616/
  [github]: http://github.com/leaflabs/
  [shiny new website]: http://www.flickr.com/photos/48069758@N08/4556431364/
  [detectable]: http://www.flickr.com/photos/48069758@N08/4555765513/
  [test-prog-shot]: http://blogs.leaflabs.com/wp-content/uploads/test-prog-shot.png
    "test-prog-shot"
  [here]: http://gist.github.com/380091
  [eLua]: http://www.eluaproject.net/
  [python-on-a-chip]: http://code.google.com/p/python-on-a-chip/
  [Breadboarding PWM audio with the Maple]: http://blogs.leaflabs.com/wp-content/uploads/audio_board-300x225.jpg
    "audio_breadboard"
  [![Breadboarding PWM audio with the Maple][]]: http://www.flickr.com/photos/48069758@N08/4519889527/
  [Basic Audio Shield Prototype]: http://blogs.leaflabs.com/wp-content/uploads/img_4043-Modified-300x224.jpg
    "Basic Audio Shield Prototype"
  [![Basic Audio Shield Prototype][]]: http://www.flickr.com/photos/48069758@N08/4556644630/
  [Kicad]: http://kicad.sourceforge.net/wiki/index.php/Main_Page
  [flicker stream]: http://www.flickr.com/photos/48069758@N08/
  [MIDI/IR theramin]: http://www.flickr.com/photos/48069758@N08/4515845564/
  [wifi routers]: http://www.flickr.com/photos/48069758@N08/4555765533/
