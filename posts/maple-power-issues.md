Title: Maple Power Issues
Date: 2011-08-12 13:27
Author: jessb
Category: Uncategorized

In the past couple of months we've been contacted by a few users who
have had problems with the power circuitry on Maple, which has led to
the discovery of a couple of issues we wanted to make sure everybody was
aware of.

First, this has been corrected in the docs and errata for awhile but we
didn't have a blog post about it: although the silkscreen on Maple,
Maple RET6, and Maple Mini indicates that you should be able to power
the board at up to 18V, this is incorrect. The voltage regulators are
rated only up to 16V; our tests indicate that they start behaving
incorrectly at anything about 12V, even at low current loads, so this is
recommended as the maximum voltage input for the board.

In addition, while the maximum continuous output current for the board
is 250mA, if you are powering the board off higher voltages the amount
off current it can supply goes down, due to the regulators needing to
dissipate the extra power. So if you are powering the board off 12V, the
max current is about 40mA at room temperature. In general (again, at
room temperature) the max power dissipation (PD) for the chip is about
.37W, and output current = PD/(Vin-Vout). For exact max current
calculations, consult the data sheet [here][] (PDF warning).

Last, and probably most serious, we've found that on several batches of
Maples, one of the conditioning capacitors used was not up to the proper
voltage rating. (Please note that this effects only Maples and RET6s,
not Maple Mini.) The capacitor C11 should have been rated to 16V;
instead, it's only rated to 6V. This is a particularly devious problem
since capacitors can be over-voltaged for a long time before failing. If
you power your board exclusively from sources less than 6V (for example,
USB is fine), you're probably okay. But if you routinely power your
board from greater than 6V, you risk eventually blowing this cap and
shorting the board. This likely won't happen immediately -- we've been
testing boards continuously at 12V for over a week now with no ill
effects -- but in general, "it ought not to be attempted."

Probably the easiest fix for this problem is to simply remove C11, and
in fact, for the foreseeable future we will be shipping Maples with C11
taken off. This picture indicates the appropriate capacitor to be
removed with a yellow X:

![Maple with C11 indicated][]

C11 is in the upper left quadrant of the board, the bottom in a column
of six passives right to the left of the power selection header. If you
need to power your board at over 6V and don't have the ability to remove
the capacitor yourself, please get in touch with us and we will work
something out.

We truly apologize for any trouble or confusion this may have caused!
Obviously, if these issues have caused catastrophic board failure for
anybody, we are more than happy to replace or refund your board. Please
feel free to contact us with any questions or concerns at
info@leaflabs.com.

  [here]: http://ww1.microchip.com/downloads/en/DeviceDoc/22049a.pdf
  [Maple with C11 indicated]: http://leaflabs.com/wp-content/uploads/2011/08/maple-c112-295x300.png "maple-c11"
