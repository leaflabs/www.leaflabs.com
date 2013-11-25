Title: Cool Tool: RunSnakeRun
Date: 2013-11-24
Slug: cool-tool-runsnakerun
Author: bnewbold 

<center>
<img src="/static/images/posts/20130628_runsnakerun_protobuf_tool.png"
     style="border: 1px solid black;">
</center>

One of my favorite python development tools is <a
href="http://www.vrplumber.com/programming/runsnakerun/">RunSnakeRun</a>, which
is a GUI for visualizing profiling information. I usually use it to track down
what's making a script run slow: the tool draws nexted blocks with a surface
area roughly proportional to the time spent in a given function. In the above
screenshot I learned that the python library for Google's
<a href="https://en.wikipedia.org/wiki/Protocol_Buffers">Protocol Buffers</a>
serialization format were the bottle neck for an experiment we were doing. We
were sort of expecting networking or disk I/O to be the bottleneck, but with
these libraries it was the CPU. The compiled C libraries are much faster!

The Python interpreter actually has the profiling code built in ("cProfile"),
and runsnakerun is just a GUI for analysing the dump files. The commands I
usually use to capture a dump and then visualize with runsnakerun are something
like:

    :::text
    $ python -m cProfile -o ./dump.profile myscript.py --script-option blah
    $ # run to completion or Ctrl-C, then
    $ runsnakerun ./dump.profile

You can get install runsnakerun from the debian package repos (probably ubuntu
also); details and installation instructions for other operating systems are
avalable from the
<a href="http://www.vrplumber.com/programming/runsnakerun/">website</a>.

