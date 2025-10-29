import RPi.GPIO as GPIO
import time
def control_led_bcm():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(25, GPIO.IN)
    while True:
        if GPIO.input(25):
           GPIO.output(18,False)
        else:
            GPIO.output(18,True)
control_led_bcm()

