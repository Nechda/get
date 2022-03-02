import RPi.GPIO as gp
from time import sleep
 
gp.setmode(gp.BCM)
gp.setup(14, gp.OUT)
gp.setup(15, gp.IN)
 
while True:
    gp.output(14, gp.input(15))
 
gp.output(14, 0)
