Title: Audio Looping with Maple Native
Date: 2011-11-16 12:14
Author: Poslathian
Category: Uncategorized

Recently, our friends over at [Open Music Labs][] created an awesome
little shield for Maple and Arduino they call the [Audio Codec
Shield][]. The Audio Codec Shield can pump 44k 16-bit audio samples per
second into and out of your Maple sketches. What happens to those
samples in a sketch is entirely up to you. The guys at Open Music Labs
really went above and beyond and created a great library and set of
examples to go along with the Codec Shield. In just a few seconds you
can load up an example for a delay effect, a flanger, a tremolo, a sine
generator, or an LFO. Overall, the shield is great!

By coincidence, we got one of these shields right around the same time
as the Maple Native Beta boards came in. These boards have a full 1MB of
external memory, so obviously we had to wire one up to an Audio Codec
Shield and see what we could do with it. We were able to change just a
few lines from the “fixed delay” example code and turn that 1MB of ram
into a full 11 seconds of audio buffer for a loop pedal! Check out the
video to see our little Maple Native Looper in action. Sorry for cheesy
guitar playing! Check out the [code][] to see how it works, and compare
it against the effect.

<center>
<object width="500" height="281"><param name="movie" value="http://www.youtube.com/v/SQVLaHIw_TY?version=3&#038;feature=oembed"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/SQVLaHIw_TY?version=3&#038;feature=oembed" type="application/x-shockwave-flash" width="500" height="281" allowscriptaccess="always" allowfullscreen="true"></embed></object>
</center>

Have you done anything fun with audio and a Maple? Let us know!

  [Open Music Labs]: http://openmusiclabs.com
  [Audio Codec Shield]: http://www.openmusiclabs.com/projects/audio-codec-shield/arduino-audio-codec-shield/
  [code]: https://github.com/leaflabs/projects/tree/master/audio-loopie
