import RPi.GPIO as GPIO
import time

class ControlLedBCM:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def parpadea(self):
        while True:
            GPIO.output(self.pin, True)
            time.sleep(1)
            GPIO.output(self.pin, False)
            time.sleep(1)

class ControlbotonBCM:
    def __init__(self, pin_led, pin_boton):
        self.pin_led = pin_led
        self.pin_boton = pin_boton
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_led, GPIO.OUT)
        GPIO.setup(self.pin_boton, GPIO.IN)

    def controlarboton(self):
        while True:
            if GPIO.input(self.pin_boton):
                GPIO.output(self.pin_led, False)
            else:
                GPIO.output(self.pin_led, True)
            time.sleep(0.1)

