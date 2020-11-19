#set up
import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
#gp.setmode(gp.BOARD)
led_pin = 18
gp.setup(18, gp.OUT)

#logic
try:
    while(True):
        gp.output(led_pin, gp.HIGH)    #SHIFT+TAB
        time.sleep(1)
        gp.output(led_pin, gp.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    gp.cleanup()
