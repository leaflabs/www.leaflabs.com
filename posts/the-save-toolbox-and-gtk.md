Title: The S.A.V.E. Toolbox and GTK+
Date: 2009-06-09 01:34
Author: Bbradlyn
Category: Uncategorized

Today we started our first software endeavor - the Signal Analysis and
Visualization Engine (S.A.V.E.) Toolbox. It will allow the user to
compose complex systems in terms of nodes - either pre-packaged or
hand-coded in a C-like language - which execute various functions on
their inputs and feed the outputs to connected nodes. The user may write
or select various input functions, and graph outputs in an
oscilloscope-style x-y plot. Additionally, the S.A.V.E. toolbox will
also be able to parse the functions represented by these node nets into
Verilog. At the end of the day, we want the S.A.V.E. toolbox to be the
principal interface between the end-user and the FPGA on the Leaf
boards.

Today we began to plan out how to implement the GUI front-end of the
toolbox. We're using the [GTK+ toolkit][], an object-oriented extension
of standard C made for GUI design. Despite how impressed I am with the
library of features contained in GTK+, I'm a little dissatisfied with
its object-oriented nature. At the core, I'd have to say I'm pretty
utilitarian, and object-oriented program seems to
sacrifice efficiency  for gains in... well... I haven't yet seen what
you really gain. I guess you could say you gain some level of
generality, but i think its too much. Anything you'd *need* to do with
classes, objects, and inheritance  (and I'd say there aren't too many
things) you could always do manually with structs in standard C. The
object-oriented paradigm, however, engenders the idea that *everything*
should be implemented with classes and objects. Thus, much as we did
today, you end up spending most of your time deciding which classes each
functions should live in, and designing initializer after initializer
after initializer. I suppose in the end I'll just have to suck it up
though, because I sure as hell don't want to redo all the hard work that
GTK+ has taken care of for me.

  [GTK+ toolkit]: http://www.gtk.org
