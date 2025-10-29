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


def led_on_board(pin, modo):
    GPIO.setwarnings(False)
    GPIO.setmode(modo)
    GPIO.setup(pin, GPIO.OUT)
    while True:
            GPIO.output(pin, True)
            time.sleep(1)
            GPIO.output(pin, False)
            time.sleep(1)


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






