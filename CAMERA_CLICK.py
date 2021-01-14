from picamera import PiCamera
from time import sleep

camera = PiCamera()
sleep(1)
camera.start_preview()
print("Clicking picture")
camera.capture('/home/pi/Desktop/image.jpg')
sleep(5)
camera.stop_preview()
camera.close()
