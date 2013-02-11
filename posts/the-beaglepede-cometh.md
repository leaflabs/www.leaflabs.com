Title: The Beaglepede Cometh.
Date: 2010-07-18 20:58
Author: Hadley
Category: Projects

This weekend Barry and I found ourselves in a Dollar Tree store-- one of
the greatest places known to man.

</p>

We picked ourselves up some toys to play with, all for a dollar:

</p>

<div id="_mcePaste" style="text-align: center;">
</p>

[caption id="attachment\_1089" align="aligncenter" width="270" caption="
That plush guy had the face of a beagle, but the body of a centipede,
perfect for segmented lighting! You can also see our prototype, and the
weird kaleidoscope plastic things we used in his
back."][![][]][][/caption]

<p>
</div>
</p>

<div id="_mcePaste" style="text-align: left;">
We named that friendly fellow the Beaglepede, after the obvious
portmanteau, and decided to actualize his inner nature: warm and
glowing. So we took those weird disco lanterns and a few LEDs  and made
the little guy shine.

</div>
</p>
<p>
<center>
</p>

<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="480" height="385" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><param name="src" value="http://www.youtube.com/v/Qq-2YjmYIY8&amp;hl=en_US&amp;fs=1"></param><param name="allowfullscreen" value="true"></param><embed type="application/x-shockwave-flash" width="480" height="385" src="http://www.youtube.com/v/Qq-2YjmYIY8&amp;hl=en_US&amp;fs=1" allowscriptaccess="always" allowfullscreen="true">
</embed></object>

<div id="_mcePaste" style="text-align: left;">
</center>
</p>

<p>
The code we used can be found down below. Basically it reads from a
button, which changes the state between off and glowing each LED in
sequence. The circuit is similarly simple, the diagram also can be found
below.

</div>
</p>

<div id="_mcePaste" style="text-align: left;">
What I think is particularly cool about this project, is that the most
expensive parts(barring the maple), were the LEDs, and the most
eye-catching parts were essentially found. It's also a fairly simple and
quick project (an evening for two people) that pretty much anyone can
make, but it's still fun and exciting to finish.

</div>
</p>

<div id="_mcePaste" style="text-align: left;">
So, onward to dollar stores and thrift stores alike! Deconstruct and
reconstruct your own Shellyesque army of franken-hacks! Godspeed and
good luck!

</div>
</p>
Continue for code and schematic...

<div style="text-align: left;">
<!--more-->

</div>
</p>

Here's the code:

</p>

<p>
~~~~ {.code style="text-align: left; width:600px;"}
//Code for Mr. Blinkie, AKA the psychedelic beaglepede//July 17 2010//Written by Hadley Piperint state = 0;     // we declare these here so they can be accessed globally, int button = 0;    // meaning in different functions.void wave(){        // this is the function that controlls the light  int i;  int j;            // counter variables          //we put the LED's sequentially in pins 5-9 for looping convenience  for (i = 5; i< 10; i++){ // i counts the LED pin    if (digitalRead(button) == HIGH){  //check for button press      state = 0;      break;    }   if (state == 0) break; //check if button was pressed during inner loop     for (j = 0; j<=50050; j+=350){ //loop to fade each LED on     analogWrite(i,j); //set pin i to pwm duty cycle j      delay(1); //small aesthetic delay      if (digitalRead(button) == HIGH){ //another check for button press        state = 0;        break;      }    }    delay(100); //let the light stay on for a bit    for (j = 50050; j>=0; j-=350){ //loop to fade each LED off      analogWrite(i,j); //set pin i to pwm duty cycle j      delay(1); //small aesthetic delay, again      if (digitalRead(button) == HIGH){ //last check for button press        state = 0;        break;      }    }    delay(100); //third aesthetic delay  }}void setup(){  pinMode(5, PWM);  //set the LED pins to PWM  pinMode(6, PWM);  pinMode(7, PWM);  pinMode(8, PWM);  pinMode(9, PWM);  pinMode(button, INPUT); //set button pin to input}void loop(){  if (state == 0 ){       //turn all LED's off in resting state    analogWrite(5, 000);    analogWrite(6, 000);    analogWrite(7, 000);    analogWrite(8, 000);    analogWrite(9, 000);    if (digitalRead(button) == HIGH){ //check to see if button was pressed      state = 1;      delay(500);      SerialUSB.println("I am the Great BEAGLEPEDE!!"); //a sign of things to come    }  }  if (state == 1){ //if the button is in state 1, call the wave function    wave();    if (digitalRead(button) == HIGH){ //check for button press and reset to state 0      state = 0;      delay(500);    }  }}
~~~~

</p>

And here's the schematic:

</p>

<div class="mceTemp" style="text-align: left;">
[![][1]][]
:   Ignore the letters on the right... they're not related to the
    diagram.

</div>
</p>

I'm excited to have the beaglepede around because I think he's going to
be a cool visualizer...there's lots of things you can do with a row of
LEDs!

</p>

[caption id="attachment\_1091" align="aligncenter" width="214"
caption="Bye bye, Beaglepede."][![][2]][][/caption]

</p>

</p>

  []: http://leaflabs.com/wp-content/uploads/2010/07/100_0119-450x600.jpg
    "100_0119"
  [![][]]: http://leaflabs.com/2010/07/the-beaglepede-cometh/100_0119/
  [1]: http://leaflabs.com/wp-content/uploads/2010/07/100_0146-450x600.jpg
    "100_0146"
  [![][1]]: http://leaflabs.com/2010/07/the-beaglepede-cometh/100_0146/
  [2]: http://leaflabs.com/wp-content/uploads/2010/07/100_0143-214x300.jpg
    "100_0143"
  [![][2]]: http://leaflabs.com/2010/07/the-beaglepede-cometh/100_0143/
