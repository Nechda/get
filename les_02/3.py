import RPi.GPIO as gp
from time import sleep
 
gp.setmode(gp.BCM)
 
leds = [21, 20, 16, 12, 7, 8, 25, 24]
gp.setup(leds, gp.OUT)
 
for i in range(3):
    for pin in leds:
        gp.output(pin, 1)
        sleep(0.2)
        gp.output(pin, 0)
 
gp.output(leds, 0)
gp.cleanup()
