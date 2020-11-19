from flask import Flask
import ex04_flask_led as led
import ex06_select as se

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/led/on")
def led_on():
    led.led18on()
    return "LED ON"

@app.route("/led/off")
def led_off():
    led.led18off()
    return "LED OFF"

@app.route("/select")
def sel():
    return se.slt()

if __name__=="__main__":
    app.run(host="192.168.0.99")
