import RPi.GPIO as gp
from time import sleep
 
gp.setmode(gp.BCM)
gp.setup(14, gp.OUT)
 
for i in range(5):
    gp.output(14, 1)
    sleep(0.5)
    gp.output(14, 0)
    sleep(0.5)
