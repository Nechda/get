import RPi.GPIO as gp
from time import sleep
from math import isclose

def safe_input(msg):
    value = input(msg)
    if value == 'q':
        return (False, -1)
    
    try:
        value_f = float(value)
        if not value_f.is_integer():
            print("Input value should be an integer")
            return (True, -1)

        value = int(value)
        if value < 0:
            print("Input value should be gain then zero")
            return (True, -1)
    except ValueError:
        print("Input value should be a number")
        return (True, -1)
    
    if value >= 2**8:
        print("8 bit DAC can represent value only in range [0, 255]")
        return (True, -1)
    
    return (True, value)

gp.setmode(gp.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
gp.setup(dac, gp.OUT)

dec2bin = lambda x: [int(i) for i in bin(x)[2:].zfill(8)] # dec to bin
c2v = lambda x: "{:.4f}".format(x / 2**8 * 3.3) # code to voltage

try:
    running = True
    while running:
        running, value = safe_input('Enter number in a range [0, 255]: ')
        if value == -1:
            continue
        print("Expected voltage on DAC = " + c2v(value) + ' V')
        gp.output(dac, dec2bin(value))
finally:
    gp.output(dac, 0)
    gp.cleanup()

