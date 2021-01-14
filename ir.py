import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
while 1:
    if(GPIO.input(8)==True):
        print('0')
    if(GPIO.input(8)==False):
        print('1')
