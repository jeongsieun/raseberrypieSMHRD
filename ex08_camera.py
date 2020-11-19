import picamera as pc
import time

camera = pc.PiCamera()
camera.start_preview()
time.sleep(5)

camera.capture("image.jpg")
camera.stop_preview()
camera.close()
