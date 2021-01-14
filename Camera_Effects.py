from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
i=1
sleep(1)
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    print(i)
    i=i+1
    sleep(0.1)
camera.stop_preview()
camera.close()
