import RPi.GPIO as gp
from time import sleep

def safe_input(msg):
    value = input(msg)
    if value == 'q':
        return (False, -1)
    
    try:
        value_f = float(value)

        if value_f > 100.0 and value_f < 0:
            print("Input value should be in range [0, 100]")
            return (True, -1)

        return (True, value_f)
    except ValueError:
        print("Input value should be a number")
        return (True, -1)
    
    return (True, -1)

gp.setmode(gp.BCM)
gp.setup(22, gp.OUT)
p = gp.PWM(22, 1000)

c2v = lambda x: "{:.4f}".format(x / 100.0 * 3.3) # code to voltage

p.start(0)

try:
    running = True
    while running:
        running, d = safe_input("Введите скважность (0-100): ")
        if d == -1:
            continue
        print("Expected voltage = " + c2v(d) + " V")
        p.start(d)
finally:
    p.stop()
    gp.cleanup()
