import RPi.GPIO as GPIO
import time



def led_on(pin, modo):
    GPIO.setwarnings(False)
    GPIO.setmode(modo)
    GPIO.setup(pin, GPIO.OUT)
    while True:
            GPIO.output(pin, True)
            time.sleep(1)
            GPIO.output(pin, False)
            time.sleep(1)
led_on(18, GPIO.BCM)
 
 




