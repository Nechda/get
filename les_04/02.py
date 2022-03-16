import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
gp.setup(dac, gp.OUT)

dec2bin = lambda x: [int(i) for i in bin(x)[2:].zfill(8)] # dec to bin

T = float(input("Enter total duration for the saw signal (in seconds): "))

try:
    while True:
        for value in range(0, 2**8):
            gp.output(dac, dec2bin(value))
            sleep(T / 2**8)
finally:
    gp.output(dac, 0)
    gp.cleanup()
