Title: Serial-USB Passthrough
Date: 2010-07-18 10:20
Author: Bnewbold
Category: Uncategorized

While debugging our new SerialUSB implementation I needed to use the
regular Serial2 interface to track down ASSERT failures, but couldn't
find a spare FTDI chip around the lab. I've got one of [these][] super
slick little ones in the mail, but in the meanwhile I wrote this sketch
in about 2 seconds which turns a spare Maple into a Serial-USB
passthrough:

  void setup() {
    Serial2.begin(9600);
  }
  
  void loop() {
    if(SerialUSB.available()) {
      Serial2.write(SerialUSB.read());
    }
    if(Serial2.available()) {
      SerialUSB.write(Serial2.read());
    }
  }

There are a million better ways to do this but I love how easy this was!

  [these]: http://www.sparkfun.com/commerce/product_info.php?products_id=8551
