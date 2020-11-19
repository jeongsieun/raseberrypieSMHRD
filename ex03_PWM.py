import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)

led_pin = 18
gp.setup(led_pin, gp.OUT)

p = gp.PWM(led_pin, 500)
p.start(0)

i = 0
while True:
    
    p.ChangeDutyCycle(i)
    i += 1
    time.sleep(0.05)
    if i == 100:
        while True:
            p.ChangeDutyCycle(i)
            i -= 1
            time.sleep(0.05)
            if i ==0:
                break
    
    #for i in range(0, 101, 1):
     #   p.ChangeDutyCycle(i)
      #  time.sleep(0.05)

    #for j in range(100, -1, -1):
     #   p.ChangeDutyCycle(j)
      #  ime.sleep(0.05)
