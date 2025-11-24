import RPi.GPIO as GPIO
import time
import adafruit_dht
import board

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class RobotModel:
    def __init__(self, nombre, modelo, led_pin):
        self.nombre = nombre
        self.modelo = modelo
        self.led_pin = led_pin

        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.output(self.led_pin, False)

    def encender(self):
        GPIO.output(self.led_pin, True)

    def apagar(self):
        GPIO.output(self.led_pin, False)

    def estado(self):
        return "Robot:", self.nombre, "Modelo:", self.modelo


class RobotExploradorModel(RobotModel):
    def __init__(self, nombre, modelo, zona, led_pin, btn_pin):
        super().__init__(nombre, modelo, led_pin)   # LED exclusivo del explorador (23)
        self.zona = zona
        self.btn_pin = btn_pin

        GPIO.setup(self.btn_pin, GPIO.IN)

    def explorar(self):
        while True:
            if GPIO.input(self.btn_pin):
                GPIO.output(self.led_pin, False)
                print(self.nombre, "(", self.modelo, ")", "esperando pulso para explorar", self.zona)
            else:
                GPIO.output(self.led_pin, True)
                print(self.nombre, "(", self.modelo, ")", "Explorando", self.zona)
            time.sleep(0.5)


class RobotMedicoModel(RobotModel):
    def __init__(self, nombre, modelo, especialidad, led_pin, pin_dht):
        super().__init__(nombre, modelo, led_pin)   # LED exclusivo del medico (24)
        self.especialidad = especialidad
        self.pin_dht = pin_dht

        self.sensor = adafruit_dht.DHT11(getattr(board, f"D{self.pin_dht}"))

    def diagnosticar(self):
        humedad = self.sensor.humidity
        temperatura = self.sensor.temperature

        if humedad is not None and temperatura is not None:
            return temperatura, humedad
        else:
            return None
