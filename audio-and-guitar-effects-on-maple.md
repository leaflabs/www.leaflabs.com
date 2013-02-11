Title: Audio and Guitar effects on Maple!
Date: 2010-07-24 09:46
Author: Okie
Category: Uncategorized

Real-time audio processing is an example of an application where Maple
really shines in comparison to Arduino. Maple has 12-bit ADCs with
sample rates up to 1MSPS and PWM fast enough to clear \~11.8 bits of
resolution (log2(72MHz/20kHz)=11.8) at a frequency twice the [Nyquist
frequency][] of the upper end of the bandwidth of the human ear (20kHz).
And there's a lot of clock cycles to do all kinds of really awesome
stuff to the signal (e.g. echo, distortion, octave, harmony,
equalization, flange, phaser, fuzz, ring modulation, and complete new
imagined effects)! I drew up a schematic and layout in [EAGLE][] and
etched a PCB with two 1/8" audio jacks, an adjustable preamp, input and
output filters, and some potentiometers. Here's a photo of the assembled
shield and the schematic:

[![][]][] [![][1]][]

</p>

Note: The potentiometer knobs aren't on the schematic; I hand wired them
afterwards.

</p>

Here are the EAGLE schematic and board layout files for this board:
[audioshieldproto-r2-v1.sch][] [audioshieldproto-r2-v1.brd][]

</p>
This can also be breadboarded with some increase in noise, but it's not
that bad for guitar. I made a similar board awhile ago that had no input
filter, and it was a lot of fun, but I wanted to lower the noise floor
of the system, which ends up sounding like a hiss in the background. To
do this, I needed an input filter. Why? What happens is that the signal
going into the ADC pin contains component frequencies above half the
sampling rate of the ADC that get aliased back into the audible range.
So any noise (environmental, digital transition, etc.) that contains
frequencies above half the sample rate that's around make the output
noisier. The purpose of the analog input filter is to filter them out
before they are digitized. This is what what the input filter looks
like:

[![][2]][]

</p>

The filter is an [active filter][] of the [Sallen-Key topology][]. I
used AD8452 op-amps that I got from [Digi-Key][], which is one of the
few op-amps suitable for 3.3V single supply operation. Another good
op-amp for this, which I'll probably go with on the next version of this
board, is the [LM324][], which is a quad op-amp (four in a package).
This will make it easier and cheaper to build a higher order input
filter. I modeled the filter I built on this board with [LTSpice][] and
this is what the frequency response looks like:

</p>

[![][3]][]Here's a link to the LTSpice schematic for the filter:
[sallen-keyinputlowpassfilter.asc][]

</p>

So what does it sound like? I'm obsessed with audio effects, but I don't
play guitar. I tried to play guitar for these recordings. Here's a photo
of the setup:

</p>

[![][4]][]

</p>

To record the effect, I simply connected the output to my computer
instead of headphones or a guitar amplifier.

</p>

Here's an mp3 of the guitar just being passed through with no effect:

</p>

[audioshieldproto-passcleanguitar.mp3][]

</p>

This is where the knob that varies the mix between clean and the effect
is turned about half-way up: [][]

</p>

[audioshieldproto-halfeffectguitar.mp3][]

</p>

Here's full effect:

</p>

[audioshieldproto-fulleffectguitar.mp3][]

</p>

These are with a sine and triangle wave input instead of a guitar and I
turned the knob up and then down:

</p>

[audioshieldproto-sinewave-turningknob.mp3][]

</p>

[audioshieldproto-trianglewave-turningknob.mp3][]

</p>

I generated the sine and triangle waves with a signal generator app I
downloaded onto an iPod Touch:[][5]

</p>

<a href="http://leaflabs.com/wp-content/uploads/2010/07/mapleaudioshieldipodlaptop.jpg">

</a>[![][6]][5]

</p>

Notice the noise on all of these recordings. There are four main sources
of this, which will be eliminated with more work. As mentioned, a higher
input filter will rid of some noise. The code for the effect causes low
amplitude signals are mapped to high amplitudes, which is another source
of noise. This can be remedied by using a slightly different transfer
function for the effect. A third source is from sampling an unbuffered
10k potentiometer. High-speed measurements made with the ADC require
lower input impedances to achieve low noise. The reading of the
potentiometer is being coupled to the input signal in the sketch for
this effect by multiplying the reading by the input to derive the
output. Most "control parameters" should probably be measured at a lower
sample rate, and simply varying the mix of effect vs. no-effect is so
common that it may should be a function that's done completely in
analog.

</p>

The final source of noise is really more of a systematic distortion. You
might notice the non-gaussian sounding clicks/pops/ticks etc. This is
likely due to timing irregularities in the sketch's execution. While
Maple is running the sketch, it gets interrupted a lot. For example,
regular systick interrupts trigger the system timer to increment when
using millis(), regular USB interrupts provide the SerialUSB
functionality. An improved version of an audio application might remedy
this by using DMA and timer features of the stm32. On the sampling side,
this might include configuring the ADC's to run in DMA mode, where they
record samples into a buffer for you automatically without requiring any
attention from the processor. You can then read from that buffer safe in
the knowledge that the samples were captured at highly regular intervals
(plus you save on processor time). On the output side, ideally we should
be adjusting the PWM value at consistent intervals as well. To do this,
we could configure a timer interrupt at high priority to guarantee an
output event at fixed intervals such as 1/44000 of a second. These more
advanced features are partially supported by the library in 0.0.6, and
documentation is on the way. Check out [the app notes from ST][] for
more information on stuff that can be done to get the most out of the
ADC systems onboard the stm32.

</p>

Here's the sketch for the effect:

</p>

<p>
~~~~ {.code style="width: 600px; height: 500px; overflow: auto;"}
// Octave-ish/Harmonizer-ish Audio/Guitar Effect// for handmade prototype audio effects Maple shield// by okie and the leaf blowers#define AIN 18#define AOUT 6#define POT 16int knob = 0;int signalin = 0;int signalout = 0;int iomap[] = {256, 259, 262, 265, 268, 271, 274, 277, 281, 284, 287, 290, 293,296, 299, 302, 305, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342,345, 348, 351, 353, 356, 359, 362, 365, 368, 371, 373, 376, 379, 382, 384, 387,390, 392, 395, 398, 400, 403, 405, 408, 411, 413, 415, 418, 420, 423, 425, 427,430, 432, 434, 437, 439, 441, 443, 445, 447, 449, 451, 453, 455, 457, 459, 461,463, 465, 467, 468, 470, 472, 473, 475, 477, 478, 480, 481, 483, 484, 486, 487,488, 490, 491, 492, 493, 494, 495, 497, 498, 499, 500, 500, 501, 502, 503, 504,505, 505, 506, 507, 507, 508, 508, 509, 509, 510, 510, 510, 511, 511, 511, 511,511, 511, 511, 512, 511, 511, 511, 511, 511, 511, 511, 510, 510, 510, 509, 509,508, 508, 507, 507, 506, 505, 505, 504, 503, 502, 501, 500, 500, 499, 498, 497,495, 494, 493, 492, 491, 490, 488, 487, 486, 484, 483, 481, 480, 478, 477, 475,473, 472, 470, 468, 467, 465, 463, 461, 459, 457, 455, 453, 451, 449, 447, 445,443, 441, 439, 437, 434, 432, 430, 427, 425, 423, 420, 418, 415, 413, 411, 408,405, 403, 400, 398, 395, 392, 390, 387, 384, 382, 379, 376, 373, 371, 368, 365,362, 359, 356, 353, 351, 348, 345, 342, 339, 336, 333, 330, 327, 324, 321, 318,315, 312, 309, 305, 302, 299, 296, 293, 290, 287, 284, 281, 277, 274, 271, 268,265, 262, 259, 256, 252, 249, 246, 243, 240, 237, 234, 230, 227, 224, 221, 218,215, 212, 209, 206, 202, 199, 196, 193, 190, 187, 184, 181, 178, 175, 172, 169,166, 163, 160, 158, 155, 152, 149, 146, 143, 140, 138, 135, 132, 129, 127, 124,121, 119, 116, 113, 111, 108, 106, 103, 100, 98, 96, 93, 91, 88, 86, 84, 81,79, 77, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 43, 41,39, 38, 36, 34, 33, 31, 30, 28, 27, 25, 24, 23, 21, 20, 19, 18, 17, 16, 14, 13,12, 11, 11, 10, 9, 8, 7, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 11,11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 27, 28, 30, 31, 33, 34, 36,38, 39, 41, 43, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74,77, 79, 81, 84, 86, 88, 91, 93, 96, 98, 100, 103, 106, 108, 111, 113, 116, 119,121, 124, 127, 129, 132, 135, 138, 140, 143, 146, 149, 152, 155, 158, 160, 163,166, 169, 172, 175, 178, 181, 184, 187, 190, 193, 196, 199, 202, 206, 209, 212,215, 218, 221, 224, 227, 230, 234, 237, 240, 243, 246, 249, 252, 255, 259, 262,265, 268, 271, 274, 277, 281, 284, 287, 290, 293, 296, 299, 302, 305, 309, 312,315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 353, 356, 359,362, 365, 368, 371, 373, 376, 379, 382, 384, 387, 390, 392, 395, 398, 400, 403,405, 408, 411, 413, 415, 418, 420, 423, 425, 427, 430, 432, 434, 437, 439, 441,443, 445, 447, 449, 451, 453, 455, 457, 459, 461, 463, 465, 467, 468, 470, 472,473, 475, 477, 478, 480, 481, 483, 484, 486, 487, 488, 490, 491, 492, 493, 494,495, 497, 498, 499, 500, 500, 501, 502, 503, 504, 505, 505, 506, 507, 507, 508,508, 509, 509, 510, 510, 510, 511, 511, 511, 511, 511, 511, 511, 512, 511, 511,511, 511, 511, 511, 511, 510, 510, 510, 509, 509, 508, 508, 507, 507, 506, 505,505, 504, 503, 502, 501, 500, 500, 499, 498, 497, 495, 494, 493, 492, 491, 490,488, 487, 486, 484, 483, 481, 480, 478, 477, 475, 473, 472, 470, 468, 467, 465,463, 461, 459, 457, 455, 453, 451, 449, 447, 445, 443, 441, 439, 437, 434, 432,430, 427, 425, 423, 420, 418, 415, 413, 411, 408, 405, 403, 400, 398, 395, 392,390, 387, 384, 382, 379, 376, 373, 371, 368, 365, 362, 359, 356, 353, 351, 348,345, 342, 339, 336, 333, 330, 327, 324, 321, 318, 315, 312, 309, 305, 302, 299,296, 293, 290, 287, 284, 281, 277, 274, 271, 268, 265, 262, 259, 256, 252, 249,246, 243, 240, 237, 234, 230, 227, 224, 221, 218, 215, 212, 209, 206, 202, 199,196, 193, 190, 187, 184, 181, 178, 175, 172, 169, 166, 163, 160, 158, 155, 152,149, 146, 143, 140, 138, 135, 132, 129, 127, 124, 121, 119, 116, 113, 111, 108,106, 103, 100, 98, 96, 93, 91, 88, 86, 84, 81, 79, 77, 74, 72, 70, 68, 66, 64,62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 43, 41, 39, 38, 36, 34, 33, 31, 30, 28,27, 25, 24, 23, 21, 20, 19, 18, 17, 16, 14, 13, 12, 11, 11, 10, 9, 8, 7, 6, 6,5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 11, 11, 12, 13, 14, 16, 17, 18,19, 20, 21, 23, 24, 25, 27, 28, 30, 31, 33, 34, 36, 38, 39, 41, 43, 44, 46, 48,50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 77, 79, 81, 84, 86, 88, 91,93, 96, 98, 100, 103, 106, 108, 111, 113, 116, 119, 121, 124, 127, 129, 132,135, 138, 140, 143, 146, 149, 152, 155, 158, 160, 163, 166, 169, 172, 175, 178,181, 184, 187, 190, 193, 196, 199, 202, 206, 209, 212, 215, 218, 221, 224, 227,230, 234, 237, 240, 243, 246, 249, 252, 255, 259, 262, 265, 268, 271, 274, 277,281, 284, 287, 290, 293, 296, 299, 302, 305, 309, 312, 315, 318, 321, 324, 327,330, 333, 336, 339, 342, 345, 348, 351, 353, 356, 359, 362, 365, 368, 371, 373,376, 379, 382, 384, 387, 390, 392, 395, 398, 400, 403, 405, 408, 411, 413, 415,418, 420, 423, 425, 427, 430, 432, 434, 437, 439, 441, 443, 445, 447, 449, 451,453, 455, 457, 459, 461, 463, 465, 467, 468, 470, 472, 473, 475, 477, 478, 480,481, 483, 484, 486, 487, 488, 490, 491, 492, 493, 494, 495, 497, 498, 499, 500,500, 501, 502, 503, 504, 505, 505, 506, 507, 507, 508, 508, 509, 509, 510, 510,510, 511, 511, 511, 511, 511, 511, 511, 512, 511, 511, 511, 511, 511, 511, 511,510, 510, 510, 509, 509, 508, 508, 507, 507, 506, 505, 505, 504, 503, 502, 501,500, 500, 499, 498, 497, 495, 494, 493, 492, 491, 490, 488, 487, 486, 484, 483,481, 480, 478, 477, 475, 473, 472, 470, 468, 467, 465, 463, 461, 459, 457, 455,453, 451, 449, 447, 445, 443, 441, 439, 437, 434, 432, 430, 427, 425, 423, 420,418, 415, 413, 411, 408, 405, 403, 400, 398, 395, 392, 390, 387, 384, 382, 379,376, 373, 371, 368, 365, 362, 359, 356, 353, 351, 348, 345, 342, 339, 336, 333,330, 327, 324, 321, 318, 315, 312, 309, 305, 302, 299, 296, 293, 290, 287, 284,281, 277, 274, 271, 268, 265, 262, 259, 256, 252, 249, 246, 243, 240, 237, 234,230, 227, 224, 221, 218, 215, 212, 209, 206, 202, 199, 196, 193, 190, 187, 184,181, 178, 175, 172, 169, 166, 163, 160, 158, 155, 152, 149, 146, 143, 140, 138,135, 132, 129, 127, 124, 121, 119, 116, 113, 111, 108, 106, 103, 100, 98, 96,93, 91, 88, 86, 84, 81, 79, 77, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52,50, 48, 46, 44, 43, 41, 39, 38, 36, 34, 33, 31, 30, 28, 27, 25, 24, 23, 21, 20,19, 18, 17, 16, 14, 13, 12, 11, 11, 10, 9, 8, 7, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1,1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4,5, 6, 6, 7, 8, 9, 10, 11, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25,27, 28, 30, 31, 33, 34, 36, 38, 39, 41, 43, 44, 46, 48, 50, 52, 54, 56, 58, 60,62, 64, 66, 68, 70, 72, 74, 77, 79, 81, 84, 86, 88, 91, 93, 96, 98, 100, 103,106, 108, 111, 113, 116, 119, 121, 124, 127, 129, 132, 135, 138, 140, 143, 146,149, 152, 155, 158, 160, 163, 166, 169, 172, 175, 178, 181, 184, 187, 190, 193,196, 199, 202, 206, 209, 212, 215, 218, 221, 224, 227, 230, 234, 237, 240, 243,246, 249, 252, 255, 259, 262, 265, 268, 271, 274, 277, 281, 284, 287, 290, 293,296, 299, 302, 305, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342,345, 348, 351, 353, 356, 359, 362, 365, 368, 371, 373, 376, 379, 382, 384, 387,390, 392, 395, 398, 400, 403, 405, 408, 411, 413, 415, 418, 420, 423, 425, 427,430, 432, 434, 437, 439, 441, 443, 445, 447, 449, 451, 453, 455, 457, 459, 461,463, 465, 467, 468, 470, 472, 473, 475, 477, 478, 480, 481, 483, 484, 486, 487,488, 490, 491, 492, 493, 494, 495, 497, 498, 499, 500, 500, 501, 502, 503, 504,505, 505, 506, 507, 507, 508, 508, 509, 509, 510, 510, 510, 511, 511, 511, 511,511, 511, 511, 512, 511, 511, 511, 511, 511, 511, 511, 510, 510, 510, 509, 509,508, 508, 507, 507, 506, 505, 505, 504, 503, 502, 501, 500, 500, 499, 498, 497,495, 494, 493, 492, 491, 490, 488, 487, 486, 484, 483, 481, 480, 478, 477, 475,473, 472, 470, 468, 467, 465, 463, 461, 459, 457, 455, 453, 451, 449, 447, 445,443, 441, 439, 437, 434, 432, 430, 427, 425, 423, 420, 418, 415, 413, 411, 408,405, 403, 400, 398, 395, 392, 390, 387, 384, 382, 379, 376, 373, 371, 368, 365,362, 359, 356, 353, 351, 348, 345, 342, 339, 336, 333, 330, 327, 324, 321, 318,315, 312, 309, 305, 302, 299, 296, 293, 290, 287, 284, 281, 277, 274, 271, 268,265, 262, 259, 255, 252, 249, 246, 243, 240, 237, 234, 230, 227, 224, 221, 218,215, 212, 209, 206, 202, 199, 196, 193, 190, 187, 184, 181, 178, 175, 172, 169,166, 163, 160, 158, 155, 152, 149, 146, 143, 140, 138, 135, 132, 129, 127, 124,121, 119, 116, 113, 111, 108, 106, 103, 100, 98, 96, 93, 91, 88, 86, 84, 81,79, 77, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 43, 41,39, 38, 36, 34, 33, 31, 30, 28, 27, 25, 24, 23, 21, 20, 19, 18, 17, 16, 14, 13,12, 11, 11, 10, 9, 8, 7, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 11,11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 27, 28, 30, 31, 33, 34, 36,38, 39, 41, 43, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74,77, 79, 81, 84, 86, 88, 91, 93, 96, 98, 100, 103, 106, 108, 111, 113, 116, 119,121, 124, 127, 129, 132, 135, 138, 140, 143, 146, 149, 152, 155, 158, 160, 163,166, 169, 172, 175, 178, 181, 184, 187, 190, 193, 196, 199, 202, 206, 209, 212,215, 218, 221, 224, 227, 230, 234, 237, 240, 243, 246, 249, 252, 255, 259, 262,265, 268, 271, 274, 277, 281, 284, 287, 290, 293, 296, 299, 302, 305, 309, 312,315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 353, 356, 359,362, 365, 368, 371, 373, 376, 379, 382, 384, 387, 390, 392, 395, 398, 400, 403,405, 408, 411, 413, 415, 418, 420, 423, 425, 427, 430, 432, 434, 437, 439, 441,443, 445, 447, 449, 451, 453, 455, 457, 459, 461, 463, 465, 467, 468, 470, 472,473, 475, 477, 478, 480, 481, 483, 484, 486, 487, 488, 490, 491, 492, 493, 494,495, 497, 498, 499, 500, 500, 501, 502, 503, 504, 505, 505, 506, 507, 507, 508,508, 509, 509, 510, 510, 510, 511, 511, 511, 511, 511, 511, 511, 512, 511, 511,511, 511, 511, 511, 511, 510, 510, 510, 509, 509, 508, 508, 507, 507, 506, 505,505, 504, 503, 502, 501, 500, 500, 499, 498, 497, 495, 494, 493, 492, 491, 490,488, 487, 486, 484, 483, 481, 480, 478, 477, 475, 473, 472, 470, 468, 467, 465,463, 461, 459, 457, 455, 453, 451, 449, 447, 445, 443, 441, 439, 437, 434, 432,430, 427, 425, 423, 420, 418, 415, 413, 411, 408, 405, 403, 400, 398, 395, 392,390, 387, 384, 382, 379, 376, 373, 371, 368, 365, 362, 359, 356, 353, 351, 348,345, 342, 339, 336, 333, 330, 327, 324, 321, 318, 315, 312, 309, 305, 302, 299,296, 293, 290, 287, 284, 281, 277, 274, 271, 268, 265, 262, 259, 255, 252, 249,246, 243, 240, 237, 234, 230, 227, 224, 221, 218, 215, 212, 209, 206, 202, 199,196, 193, 190, 187, 184, 181, 178, 175, 172, 169, 166, 163, 160, 158, 155, 152,149, 146, 143, 140, 138, 135, 132, 129, 127, 124, 121, 119, 116, 113, 111, 108,106, 103, 100, 98, 96, 93, 91, 88, 86, 84, 81, 79, 77, 74, 72, 70, 68, 66, 64,62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 43, 41, 39, 38, 36, 34, 33, 31, 30, 28,27, 25, 24, 23, 21, 20, 19, 18, 17, 16, 14, 13, 12, 11, 11, 10, 9, 8, 7, 6, 6,5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 11, 11, 12, 13, 14, 16, 17, 18,19, 20, 21, 23, 24, 25, 27, 28, 30, 31, 33, 34, 36, 38, 39, 41, 43, 44, 46, 48,50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 77, 79, 81, 84, 86, 88, 91,93, 96, 98, 100, 103, 106, 108, 111, 113, 116, 119, 121, 124, 127, 129, 132,135, 138, 140, 143, 146, 149, 152, 155, 158, 160, 163, 166, 169, 172, 175, 178,181, 184, 187, 190, 193, 196, 199, 202, 206, 209, 212, 215, 218, 221, 224, 227,230, 234, 237, 240, 243, 246, 249, 252, 255, 259, 262, 265, 268, 271, 274, 277,281, 284, 287, 290, 293, 296, 299, 302, 305, 309, 312, 315, 318, 321, 324, 327,330, 333, 336, 339, 342, 345, 348, 351, 353, 356, 359, 362, 365, 368, 371, 373,376, 379, 382, 384, 387, 390, 392, 395, 398, 400, 403, 405, 408, 411, 413, 415,418, 420, 423, 425, 427, 430, 432, 434, 437, 439, 441, 443, 445, 447, 449, 451,453, 455, 457, 459, 461, 463, 465, 467, 468, 470, 472, 473, 475, 477, 478, 480,481, 483, 484, 486, 487, 488, 490, 491, 492, 493, 494, 495, 497, 498, 499, 500,500, 501, 502, 503, 504, 505, 505, 506, 507, 507, 508, 508, 509, 509, 510, 510,510, 511, 511, 511, 511, 511, 511, 511, 512, 511, 511, 511, 511, 511, 511, 511,510, 510, 510, 509, 509, 508, 508, 507, 507, 506, 505, 505, 504, 503, 502, 501,500, 500, 499, 498, 497, 495, 494, 493, 492, 491, 490, 488, 487, 486, 484, 483,481, 480, 478, 477, 475, 473, 472, 470, 468, 467, 465, 463, 461, 459, 457, 455,453, 451, 449, 447, 445, 443, 441, 439, 437, 434, 432, 430, 427, 425, 423, 420,418, 415, 413, 411, 408, 405, 403, 400, 398, 395, 392, 390, 387, 384, 382, 379,376, 373, 371, 368, 365, 362, 359, 356, 353, 351, 348, 345, 342, 339, 336, 333,330, 327, 324, 321, 318, 315, 312, 309, 305, 302, 299, 296, 293, 290, 287, 284,281, 277, 274, 271, 268, 265, 262, 259, 256, 252, 249, 246, 243, 240, 237, 234,230, 227, 224, 221, 218, 215, 212, 209, 206, 202, 199, 196, 193, 190, 187, 184,181, 178, 175, 172, 169, 166, 163, 160, 158, 155, 152, 149, 146, 143, 140, 138,135, 132, 129, 127, 124, 121, 119, 116, 113, 111, 108, 106, 103, 100, 98, 96,93, 91, 88, 86, 84, 81, 79, 77, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52,50, 48, 46, 44, 43, 41, 39, 38, 36, 34, 33, 31, 30, 28, 27, 25, 24, 23, 21, 20,19, 18, 17, 16, 14, 13, 12, 11, 11, 10, 9, 8, 7, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1,1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4,5, 6, 6, 7, 8, 9, 10, 11, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25,27, 28, 30, 31, 33, 34, 36, 38, 39, 41, 43, 44, 46, 48, 50, 52, 54, 56, 58, 60,62, 64, 66, 68, 70, 72, 74, 77, 79, 81, 84, 86, 88, 91, 93, 96, 98, 100, 103,106, 108, 111, 113, 116, 119, 121, 124, 127, 129, 132, 135, 138, 140, 143, 146,149, 152, 155, 158, 160, 163, 166, 169, 172, 175, 178, 181, 184, 187, 190, 193,196, 199, 202, 206, 209, 212, 215, 218, 221, 224, 227, 230, 234, 237, 240, 243,246, 249, 252, 255, 259, 262, 265, 268, 271, 274, 277, 281, 284, 287, 290, 293,296, 299, 302, 305, 309, 312, 315, 318, 321, 324, 327, 330, 333, 336, 339, 342,345, 348, 351, 353, 356, 359, 362, 365, 368, 371, 373, 376, 379, 382, 384, 387,390, 392, 395, 398, 400, 403, 405, 408, 411, 413, 415, 418, 420, 423, 425, 427,430, 432, 434, 437, 439, 441, 443, 445, 447, 449, 451, 453, 455, 457, 459, 461,463, 465, 467, 468, 470, 472, 473, 475, 477, 478, 480, 481, 483, 484, 486, 487,488, 490, 491, 492, 493, 494, 495, 497, 498, 499, 500, 500, 501, 502, 503, 504,505, 505, 506, 507, 507, 508, 508, 509, 509, 510, 510, 510, 511, 511, 511, 511,511, 511, 511, 512, 511, 511, 511, 511, 511, 511, 511, 510, 510, 510, 509, 509,508, 508, 507, 507, 506, 505, 505, 504, 503, 502, 501, 500, 500, 499, 498, 497,495, 494, 493, 492, 491, 490, 488, 487, 486, 484, 483, 481, 480, 478, 477, 475,473, 472, 470, 468, 467, 465, 463, 461, 459, 457, 455, 453, 451, 449, 447, 445,443, 441, 439, 437, 434, 432, 430, 427, 425, 423, 420, 418, 415, 413, 411, 408,405, 403, 400, 398, 395, 392, 390, 387, 384, 382, 379, 376, 373, 371, 368, 365,362, 359, 356, 353, 351, 348, 345, 342, 339, 336, 333, 330, 327, 324, 321, 318,315, 312, 309, 305, 302, 299, 296, 293, 290, 287, 284, 281, 277, 274, 271, 268,265, 262, 259, 255, 252, 249, 246, 243, 240, 237, 234, 230, 227, 224, 221, 218,215, 212, 209, 206, 202, 199, 196, 193, 190, 187, 184, 181, 178, 175, 172, 169,166, 163, 160, 158, 155, 152, 149, 146, 143, 140, 138, 135, 132, 129, 127, 124,121, 119, 116, 113, 111, 108, 106, 103, 100, 98, 96, 93, 91, 88, 86, 84, 81,79, 77, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 43, 41,39, 38, 36, 34, 33, 31, 30, 28, 27, 25, 24, 23, 21, 20, 19, 18, 17, 16, 14, 13,12, 11, 11, 10, 9, 8, 7, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 11,11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 27, 28, 30, 31, 33, 34, 36,38, 39, 41, 43, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74,77, 79, 81, 84, 86, 88, 91, 93, 96, 98, 100, 103, 106, 108, 111, 113, 116, 119,121, 124, 127, 129, 132, 135, 138, 140, 143, 146, 149, 152, 155, 158, 160, 163,166, 169, 172, 175, 178, 181, 184, 187, 190, 193, 196, 199, 202, 206, 209, 212,215, 218, 221, 224, 227, 230, 234, 237, 240, 243, 246, 249, 252, 255, 259, 262,265, 268, 271, 274, 277, 281, 284, 287, 290, 293, 296, 299, 302, 305, 309, 312,315, 318, 321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 353, 356, 359,362, 365, 368, 371, 373, 376, 379, 382, 384, 387, 390, 392, 395, 398, 400, 403,405, 408, 411, 413, 415, 418, 420, 423, 425, 427, 430, 432, 434, 437, 439, 441,443, 445, 447, 449, 451, 453, 455, 457, 459, 461, 463, 465, 467, 468, 470, 472,473, 475, 477, 478, 480, 481, 483, 484, 486, 487, 488, 490, 491, 492, 493, 494,495, 497, 498, 499, 500, 500, 501, 502, 503, 504, 505, 505, 506, 507, 507, 508,508, 509, 509, 510, 510, 510, 511, 511, 511, 511, 511, 511, 511, 512, 511, 511,511, 511, 511, 511, 511, 510, 510, 510, 509, 509, 508, 508, 507, 507, 506, 505,505, 504, 503, 502, 501, 500, 500, 499, 498, 497, 495, 494, 493, 492, 491, 490,488, 487, 486, 484, 483, 481, 480, 478, 477, 475, 473, 472, 470, 468, 467, 465,463, 461, 459, 457, 455, 453, 451, 449, 447, 445, 443, 441, 439, 437, 434, 432,430, 427, 425, 423, 420, 418, 415, 413, 411, 408, 405, 403, 400, 398, 395, 392,390, 387, 384, 382, 379, 376, 373, 371, 368, 365, 362, 359, 356, 353, 351, 348,345, 342, 339, 336, 333, 330, 327, 324, 321, 318, 315, 312, 309, 305, 302, 299,296, 293, 290, 287, 284, 281, 277, 274, 271, 268, 265, 262, 259, 256, 252, 249,246, 243, 240, 237, 234, 230, 227, 224, 221, 218, 215, 212, 209, 206, 202, 199,196, 193, 190, 187, 184, 181, 178, 175, 172, 169, 166, 163, 160, 158, 155, 152,149, 146, 143, 140, 138, 135, 132, 129, 127, 124, 121, 119, 116, 113, 111, 108,106, 103, 100, 98, 96, 93, 91, 88, 86, 84, 81, 79, 77, 74, 72, 70, 68, 66, 64,62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 43, 41, 39, 38, 36, 34, 33, 31, 30, 28,27, 25, 24, 23, 21, 20, 19, 18, 17, 16, 14, 13, 12, 11, 11, 10, 9, 8, 7, 6, 6,5, 4, 4, 3, 3, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 11, 11, 12, 13, 14, 16, 17, 18,19, 20, 21, 23, 24, 25, 27, 28, 30, 31, 33, 34, 36, 38, 39, 41, 43, 44, 46, 48,50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 77, 79, 81, 84, 86, 88, 91,93, 96, 98, 100, 103, 106, 108, 111, 113, 116, 119, 121, 124, 127, 129, 132,135, 138, 140, 143, 146, 149, 152, 155, 158, 160, 163, 166, 169, 172, 175, 178,181, 184, 187, 190, 193, 196, 199, 202, 206, 209, 212, 215, 218, 221, 224, 227,230, 234, 237, 240, 243, 246, 249, 252};void setup() {  pinMode(AIN, INPUT_ANALOG);  pinMode(AOUT, PWM);  pinMode(POT, INPUT_ANALOG);  // make PWM frequency at least greater than two times the upper end of the  // signal bandwidth (signal bandwidth: ~20-20000Hz)  timers_set_reload(1, 0x0200);}void loop() {  signalin = analogRead(AIN);  knob = analogRead(POT);  // output: mix raw input and the input mapped to a sine wave stored in iomap  // where the mix is weighted by the knob   // also:   //   - scale raw input term by 8 to convert 12-bit ADC reading to 9-bit PWM  //   - iomap already scales the signal by 8, but scale by 8 again because its  //     shape is natually louder than raw signal   //   - scale both terms by the range of the knob reading, 4096   //   - divide by 2 because two full scale signals are summed  signalout = (signalin*knob/8 + iomap[signalin]*(4096-knob)/4)/4096/2;  pwmWrite(AOUT,signalout);}
~~~~

</p>
This sketch is just a quick, easy way to do what it does. Many
optimizations can be made for memory, speed, and using timers to make
readings and output to PWM would reduce distortion. The main function of
this code is to map every possible input value to a different output,
which is a really simple concept that can create a slew of neat effects,
many which are very common. Here's a neat webpage about it:
[http://web.inter.nl.net/hcc/davies/apmicro.html][]

The mapping being done by my sketch is stored in the array called
"iomap". I computed this array with a simple Python script. Here's a
graph of the map and the script:

[![][7]][]

</p>

Python script: [iomapgenerator.py][]

</p>

The horizontal axis is input and the vertical axis is output. I think
the behavior of this mapping is interesting. A very low amplitude sine
wave is simply amplified but as the amplitude becomes larger, it gets
transformed into sine waves with frequencies that are octaves above it.

</p>

We're interested in your comments and ideas! And if you're interested in
continued development on a shield for this stuff, let us know.

</p>

  [Nyquist frequency]: http://en.wikipedia.org/wiki/Nyquist_frequency
    "Nyquist frequency"
  [EAGLE]: http://www.cadsoftusa.com/
  []: http://leaflabs.com/wp-content/uploads/2010/07/maplebesideaudioshieldproto-300x198.jpg
    "maplebesideaudioshieldproto"
  [![][]]: http://leaflabs.com/wp-content/uploads/2010/07/maplebesideaudioshieldproto.jpg
  [1]: http://leaflabs.com/wp-content/uploads/2010/07/audioshieldproto-r2-v1-schematic-300x201.png
    "audioshieldproto-r2-v1-schematic"
  [![][1]]: http://leaflabs.com/wp-content/uploads/2010/07/audioshieldproto-r2-v1-schematic.pdf
  [audioshieldproto-r2-v1.sch]: http://dl.dropbox.com/u/42394/audioshieldproto-r2-v1.sch
  [audioshieldproto-r2-v1.brd]: http://dl.dropbox.com/u/42394/audioshieldproto-r2-v1.brd
  [2]: http://leaflabs.com/wp-content/uploads/2010/07/400px-Sallen-Key_Lowpass_General.svg_.png
    "400px-Sallen-Key_Lowpass_General.svg"
  [![][2]]: http://leaflabs.com/wp-content/uploads/2010/07/400px-Sallen-Key_Lowpass_General.svg_.png
  [active filter]: http://en.wikipedia.org/wiki/Active_filter
  [Sallen-Key topology]: http://en.wikipedia.org/wiki/Sallen%E2%80%93Key_topology
  [Digi-Key]: http://www.digikey.com/
  [LM324]: http://www.national.com/pf/LM/LM324.html
  [LTSpice]: http://www.linear.com/designtools/software/ltspice.jsp
  [3]: http://leaflabs.com/wp-content/uploads/2010/07/mapleaudioshieldinputfilterfreqresponse-770x390.png
    "mapleaudioshieldinputfilterfreqresponse"
  [![][3]]: http://leaflabs.com/wp-content/uploads/2010/07/mapleaudioshieldinputfilterfreqresponse.png
  [sallen-keyinputlowpassfilter.asc]: http://dl.dropbox.com/u/42394/sallen-keyinputlowpassfilter.asc
  [4]: http://leaflabs.com/wp-content/uploads/2010/07/mapleaudioshieldguitarheadphones-300x198.jpg
    "mapleaudioshieldguitarheadphones"
  [![][4]]: http://leaflabs.com/wp-content/uploads/2010/07/mapleaudioshieldguitarheadphones.jpg
  [audioshieldproto-passcleanguitar.mp3]: http://leaflabs.com/wp-content/uploads/2010/07/audioshieldproto-passcleanguitar.mp3
  []: http://leaflabs.com/wp-content/uploads/2010/07/audioshieldproto-halfeffectguitar.mp3
  [audioshieldproto-fulleffectguitar.mp3]: http://leaflabs.com/wp-content/uploads/2010/07/audioshieldproto-fulleffectguitar.mp3
  [audioshieldproto-sinewave-turningknob.mp3]: ../wp-content/uploads/2010/07/audioshieldproto-sinewave-turningknob.mp3
  [audioshieldproto-trianglewave-turningknob.mp3]: http://leaflabs.com/wp-content/uploads/2010/07/audioshieldproto-trianglewave-turningknob.mp3
  [5]: http://leaflabs.com/wp-content/uploads/2010/07/mapleaudioshieldipodlaptop.jpg
  [6]: http://leaflabs.com/wp-content/uploads/2010/07/mapleaudioshieldipodlaptop-397x600.jpg
    "mapleaudioshieldipodlaptop"
  [the app notes from ST]: http://www.st.com/mcu/familiesdocs-110.html
  [http://web.inter.nl.net/hcc/davies/apmicro.html]: http://web.inter.nl.net/hcc/davies/apmicro.html
  [7]: http://leaflabs.com/wp-content/uploads/2010/07/iomap-770x584.png
    "iomap"
  [![][7]]: http://leaflabs.com/wp-content/uploads/2010/07/iomap.png
  [iomapgenerator.py]: http://dl.dropbox.com/u/42394/iomapgenerator.py
