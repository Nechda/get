import RPi.GPIO as gp
from time import sleep
 
 
gp.setmode(gp.BCM)
 
dac = [26, 19, 13, 6, 5, 11, 9, 10]
gp.setup(dac, gp.OUT)
 
x = 110
number = [ x // 2 ** (7 - i) % 2 for i in range(8) ]
 
gp.output(dac, number)
sleep(5)
gp.output(dac, 0)
gp.cleanup()
