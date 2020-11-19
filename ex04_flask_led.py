#set up
import RPi.GPIO as gp

gp.setmode(gp.BCM)
#gp.setmode(gp.BOARD)
led_pin = 18
gp.setup(18, gp.OUT)

#logic

def led18on():
    gp.output(led_pin, gp.HIGH)    #SHIFT+TAB
def led18off():
    gp.output(led_pin, gp.LOW)
