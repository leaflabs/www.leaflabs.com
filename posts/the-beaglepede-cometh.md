Title: The Beaglepede Cometh.
Date: 2010-07-18 20:58
Author: Hadley
Category: Projects

<p style="text-align: left;">This weekend Barry and I found ourselves in a Dollar Tree store-- one of the greatest places known to man.</p>
<p style="text-align: left;">We picked ourselves up some toys to play with, all for a dollar:</p>

<div id="_mcePaste" style="text-align: center;">

[caption id="attachment_1089" align="aligncenter" width="270" caption=" That plush guy had the face of a beagle, but the body of a centipede, perfect for segmented lighting! You can also see our prototype, and the weird kaleidoscope plastic things we used in his back."]<a rel="attachment wp-att-1089" href="http://leaflabs.com/2010/07/the-beaglepede-cometh/100_0119/"><img class="size-large wp-image-1089 " title="100_0119" src="http://leaflabs.com/wp-content/uploads/2010/07/100_0119-450x600.jpg" alt="" width="270" height="360" /></a>[/caption]

</div>
<div id="_mcePaste" style="text-align: left;">We named that friendly fellow the Beaglepede, after the obvious portmanteau, and decided to actualize his inner nature: warm and glowing. So we took those weird disco lanterns and a few LEDs  and made the little guy shine.</div>
<center>
<p><object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="480" height="385" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="allowFullScreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="src" value="http://www.youtube.com/v/Qq-2YjmYIY8&amp;hl=en_US&amp;fs=1" /><param name="allowfullscreen" value="true" /><embed type="application/x-shockwave-flash" width="480" height="385" src="http://www.youtube.com/v/Qq-2YjmYIY8&amp;hl=en_US&amp;fs=1" allowscriptaccess="always" allowfullscreen="true"> </embed></object>
<div id="_mcePaste" style="text-align: left;"></center>
<p>
The code we used can be found down below. Basically it reads from a button, which changes the state between off and glowing each LED in sequence. The circuit is similarly simple, the diagram also can be found below.</div>
<div id="_mcePaste" style="text-align: left;">What I think is particularly cool about this project, is that the most expensive parts(barring the maple), were the LEDs, and the most eye-catching parts were essentially found. It's also a fairly simple and quick project (an evening for two people) that pretty much anyone can make, but it's still fun and exciting to finish.</div>
<div id="_mcePaste" style="text-align: left;">So, onward to dollar stores and thrift stores alike! Deconstruct and reconstruct your own Shellyesque army of franken-hacks! Godspeed and good luck!</div>
Continue for code and schematic...
<div style="text-align: left;"><!--more--></div>
<p style="text-align: left;">Here's the code:</p>

<pre class="code" style="text-align: left; width:600px;"><span style="color: #7e7e7e;">//Code for Mr. Blinkie, AKA the psychedelic beaglepede</span>
<span style="color: #7e7e7e;">//July 17 2010</span>
<span style="color: #7e7e7e;">//Written by Hadley Piper</span>

<span style="color: #cc6600;">int</span> state = 0;     <span style="color: #7e7e7e;">// we declare these here so they can be accessed globally, </span>
<span style="color: #cc6600;">int</span> button = 0;    <span style="color: #7e7e7e;">// meaning in different functions.</span>

<span style="color: #cc6600;">void</span> wave(){        <span style="color: #7e7e7e;">// this is the function that controlls the light</span>
  <span style="color: #cc6600;">int</span> i;
  <span style="color: #cc6600;">int</span> j;            <span style="color: #7e7e7e;">// counter variables</span>
          <span style="color: #7e7e7e;">//we put the LED's sequentially in pins 5-9 for looping convenience</span>
  <span style="color: #cc6600;">for</span> (i = 5; i&lt; 10; i++){ <span style="color: #7e7e7e;">// i counts the LED pin</span>
    <span style="color: #cc6600;">if</span> (<span style="color: #cc6600;">digitalRead</span>(button) == <span style="color: #006699;">HIGH</span>){  <span style="color: #7e7e7e;">//check for button press</span>
      state = 0;
      <span style="color: #cc6600;">break</span>;
    }
   <span style="color: #cc6600;">if</span> (state == 0) <span style="color: #cc6600;">break</span>; <span style="color: #7e7e7e;">//check if button was pressed during inner loop</span>
     <span style="color: #cc6600;">for</span> (j = 0; j&lt;=50050; j+=350){ <span style="color: #7e7e7e;">//loop to fade each LED on</span>
     <span style="color: #cc6600;">analogWrite</span>(i,j); <span style="color: #7e7e7e;">//set pin i to pwm duty cycle j</span>
      <span style="color: #cc6600;">delay</span>(1); <span style="color: #7e7e7e;">//small aesthetic delay</span>
      <span style="color: #cc6600;">if</span> (<span style="color: #cc6600;">digitalRead</span>(button) == <span style="color: #006699;">HIGH</span>){ <span style="color: #7e7e7e;">//another check for button press</span>
        state = 0;
        <span style="color: #cc6600;">break</span>;
      }
    }
    <span style="color: #cc6600;">delay</span>(100); <span style="color: #7e7e7e;">//let the light stay on for a bit</span>
    <span style="color: #cc6600;">for</span> (j = 50050; j&gt;=0; j-=350){ <span style="color: #7e7e7e;">//loop to fade each LED off</span>
      <span style="color: #cc6600;">analogWrite</span>(i,j); <span style="color: #7e7e7e;">//set pin i to pwm duty cycle j</span>
      <span style="color: #cc6600;">delay</span>(1); <span style="color: #7e7e7e;">//small aesthetic delay, again</span>
      <span style="color: #cc6600;">if</span> (<span style="color: #cc6600;">digitalRead</span>(button) == <span style="color: #006699;">HIGH</span>){ <span style="color: #7e7e7e;">//last check for button press</span>
        state = 0;
        <span style="color: #cc6600;">break</span>;
      }
    }
    <span style="color: #cc6600;">delay</span>(100); <span style="color: #7e7e7e;">//third aesthetic delay</span>
  }
}

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><strong>setup</strong></span>(){
  <span style="color: #cc6600;">pinMode</span>(5, PWM);  <span style="color: #7e7e7e;">//set the LED pins to PWM</span>
  <span style="color: #cc6600;">pinMode</span>(6, PWM);
  <span style="color: #cc6600;">pinMode</span>(7, PWM);
  <span style="color: #cc6600;">pinMode</span>(8, PWM);
  <span style="color: #cc6600;">pinMode</span>(9, PWM);
  <span style="color: #cc6600;">pinMode</span>(button, <span style="color: #006699;">INPUT</span>); <span style="color: #7e7e7e;">//set button pin to input</span>
}

<span style="color: #cc6600;">void</span> <span style="color: #cc6600;"><strong>loop</strong></span>(){
  <span style="color: #cc6600;">if</span> (state == 0 ){       <span style="color: #7e7e7e;">//turn all LED's off in resting state</span>
    <span style="color: #cc6600;">analogWrite</span>(5, 000);
    <span style="color: #cc6600;">analogWrite</span>(6, 000);
    <span style="color: #cc6600;">analogWrite</span>(7, 000);
    <span style="color: #cc6600;">analogWrite</span>(8, 000);
    <span style="color: #cc6600;">analogWrite</span>(9, 000);
    <span style="color: #cc6600;">if</span> (<span style="color: #cc6600;">digitalRead</span>(button) == <span style="color: #006699;">HIGH</span>){ <span style="color: #7e7e7e;">//check to see if button was pressed</span>
      state = 1;
      <span style="color: #cc6600;">delay</span>(500);
      SerialUSB.<span style="color: #cc6600;">println</span>(<span style="color: #006699;">"I am the Great BEAGLEPEDE!!"</span>); <span style="color: #7e7e7e;">//a sign of things to come</span>
    }
  }
  <span style="color: #cc6600;">if</span> (state == 1){ <span style="color: #7e7e7e;">//if the button is in state 1, call the wave function</span>
    wave();
    <span style="color: #cc6600;">if</span> (<span style="color: #cc6600;">digitalRead</span>(button) == <span style="color: #006699;">HIGH</span>){ <span style="color: #7e7e7e;">//check for button press and reset to state 0</span>
      state = 0;
      <span style="color: #cc6600;">delay</span>(500);
    }
  }
}</pre>
<p style="text-align: left;">And here's the schematic:</p>

<div class="mceTemp" style="text-align: left;"><dl id="attachment_1090" class="wp-caption alignnone" style="width: 460px;"> <dt class="wp-caption-dt"><a rel="attachment wp-att-1090" href="http://leaflabs.com/2010/07/the-beaglepede-cometh/100_0146/"><img class="size-large wp-image-1090" title="100_0146" src="http://leaflabs.com/wp-content/uploads/2010/07/100_0146-450x600.jpg" alt="" width="450" height="600" /></a></dt> <dd class="wp-caption-dd">Ignore the letters on the right... they're not related to the diagram.</dd> </dl></div>
<p style="text-align: left;">I'm excited to have the beaglepede around because I think he's going to be a cool visualizer...there's lots of things you can do with a row of LEDs!</p>


[caption id="attachment_1091" align="aligncenter" width="214" caption="Bye bye, Beaglepede."]<a rel="attachment wp-att-1091" href="http://leaflabs.com/2010/07/the-beaglepede-cometh/100_0143/"><img class="size-medium wp-image-1091" title="100_0143" src="http://leaflabs.com/wp-content/uploads/2010/07/100_0143-214x300.jpg" alt="" width="214" height="300" /></a>[/caption]
<p style="text-align: center;"></p>
<p style="text-align: center;"></p>
