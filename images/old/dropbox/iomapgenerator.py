import matplotlib.pyplot as p
import math

pwm_range = 2**16
adc_range = 4096
cycles = 2

iomap = [int(pwm_range*(abs(t-adc_range/2))*(0.5+0.5*math.cos(2*math.pi*cycles/adc_range*t)))/(adc_range/2) for t in range(adc_range)]

print iomap
p.plot(iomap)
p.show()
