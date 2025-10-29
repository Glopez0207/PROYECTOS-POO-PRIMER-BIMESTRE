import RPi.GPIO as GPIO
import time
def control_led_board():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(22, GPIO.IN)
    while True:
        if GPIO.input(22):
           GPIO.output(12,False)
        else:
            GPIO.output(12,True)
control_led_board()

