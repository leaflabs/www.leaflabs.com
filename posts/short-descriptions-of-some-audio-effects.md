Title: Short Descriptions of Some Audio Effects
Date: 2010-08-19 21:53
Author: okie
Category: Uncategorized

This is a short list of descriptions of some audio effects that I put
together for my work with audio processing on Maple so that I could
easily look and come up with something in code. I left out some, like
distortion and tremolo, that are either very obvious to me or too
general (or have too many forms) to classify with a short description.

**Noise Gate**

Require signal level to reach a threshold before passing it. It's good
to have a lower threshold to turn it off than used to turn it on to
eliminate “chatter” or switching on and off during sound that's around
the threshold. Sometimes a hold-time before the signal can be switched
off is desirable.

**Octave-up**

Apply full-wave rectification and mix with original signal or FFT and
shift all the bins to the bin with twice the frequency.

**Octave-down**

Convert signal to square wave, count the period, stretch by a factor of
2, and mix. Add another square wave stretched by a factor of four to
create two octaves down. For a more natural sound, use the stretched
square waves to modulate the polarity of the original signal. Doing this
with the one octave down square wave produces frequencies at one half
and three halves ratios of the “fundamental frequency” of the input
signal. Octave-down effects are commonly used for kick drums to produce
a “heavier” sound.

**Phaser**

The electronic phasing effect is created by splitting an audio signal
into two paths. One path treats the signal with an all-pass filter,
which preserves the amplitude of the original signal and alters the
phase. The amount of change in phase depends on the frequency. When
signals from the two paths are mixed, the frequencies that are out of
phase will cancel each other out, creating a phaser's characteristic
notches. Changing the mix ratio changes the depth of the notches; the
deepest notches occur when the mix ratio is 50%. The phasors (not
phasers) in the output of the discrete Fourier transform could also be
rotated before the inverse transform is applied to achieve phasing.

**Chorus**

The chorus effect is produced by taking an audio signal and mixing it
with one or more delayed, pitch-modulated copies of itself. The pitch of
the added voices is typically modulated by an LFO, which makes the
overall effect similar to that of a flanger, except with longer delays
and without feedback.

**Flanging**

Flanging is an audio effect that occurs when two identical signals are
mixed together, but with one signal time-delayed by a small and
gradually changing amount, usually smaller than 20 milliseconds. This
produces a swept comb filter effect: peaks and notches are produced in
the resultant frequency spectrum, related to each other in a linear
harmonic series. Varying the time delay causes these to sweep up and
down the frequency spectrum. Part of the output signal is usually fed
back to the input, producing a resonance effect which further enhances
the intensity of the peaks and troughs. The phase of the fed-back signal
is sometimes inverted, producing another variation on the flanging
sound.

**Reverberation**

Feedback delay networks can be used to simulate or implement reverb. A
convolution reverb can also be used, which can be understood by the fact
the convolving the response of an environment to infinitely short
impulse with a signal transforms the signal to how it would be in that
environment. Gated reverb is an effect commonly applied to drums to make
them sound more “punchy”. It is strong reverb that is often gated by the
level of the original signal.

**Ring Modulation**

Ring modulation is achieved by multiplying two signals. Often one of the
signals is something simple like a sine-wave or another simple waveform.
The product is the sum and difference of and between the frequencies
present in each waveform. Can be used to make speech sound robotic.

**Vocoder**

A vocoder is an analysis/synthesis system, mostly used for speech. In
the encoder, the input is passed through a multi-band filter, each band
is passed through an envelope follower, and the control signals from the
envelope followers are communicated to the decoder. The decoder applies
these (amplitude) control signals to corresponding filters in the
(re)synthesizer.

**Comb Filter**

A comb filter adds a delayed version of a signal to itself, causing
constructive and destructive interference. The frequency response of a
comb filter consists of a series of regularly-spaced spikes, giving the
appearance of a comb.
