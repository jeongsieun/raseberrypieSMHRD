import RPi.GPIO as gp
gp.setmode(gp.BCM)

button = 21
gp.setup(button, gp.IN)
ledPin = 18
gp.setup(ledPin, gp.OUT)

while True:
    buttonState = gp.input(button)
    if buttonState == 1:
        gp.output(ledPin, gp.HIGH)
    elif buttonState == 0:
        gp.output(ledPin, gp.LOW)
    print(buttonState)
