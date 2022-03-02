import RPi.GPIO as gp
from time import sleep
 
gp.setmode(gp.BCM)
 
leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
gp.setup(leds, gp.OUT)
gp.setup(aux, gp.IN, pull_up_down = gp.PUD_UP)
 
#while True:
#    [gp.output(leds[i], gp.input(aux[i])) for i in range(8)]
 
 
gp.output(leds, 0)
gp.cleanup()
