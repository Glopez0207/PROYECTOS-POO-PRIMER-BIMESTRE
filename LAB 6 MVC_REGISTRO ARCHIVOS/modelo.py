import RPi.GPIO as GPIO
import time
import adafruit_dht
import board

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class Robot:
    def __init__(self, nombre, modelo, led_pin):
        self.nombre = nombre
        self.modelo = modelo
        self.led_pin = led_pin

        GPIO.setup(self.led_pin, GPIO.OUT)

    def encender(self):
        GPIO.output(self.led_pin, True)
        print(self.nombre, "(", self.modelo, ")", "esta encendido.")
        self.registrar_led("ENCENDIDO")

    def apagar(self):
        GPIO.output(self.led_pin, False)
        print(self.nombre, "(", self.modelo, ")", "esta apagado.")
        self.registrar_led("APAGADO")

    def registrar_led(self, estado):
        archivo = open("registro_led.txt", "a")
        archivo.write(self.nombre + " " + self.modelo + " estado LED: " + estado + "\n")
        archivo.close()


class RobotExplorador(Robot):
    def __init__(self, nombre, modelo, zona_exploracion, led_pin, btn_pin):
        super().__init__(nombre, modelo, led_pin)
        self.zona_exploracion = zona_exploracion
        self.btn_pin = btn_pin

        GPIO.setup(self.btn_pin, GPIO.IN)

    def ciclo_exploracion(self):
        if GPIO.input(self.btn_pin):
            GPIO.output(self.led_pin, False)
            print(self.nombre, "(", self.modelo, ")", "esperando pulso para explorar", self.zona_exploracion)
            self.registrar_boton("NO PULSADO")
        else:
            GPIO.output(self.led_pin, True)
            print(self.nombre, "(", self.modelo, ")", "explorando", self.zona_exploracion)
            self.registrar_boton("PULSADO")
        time.sleep(0.5)

    def registrar_boton(self, estado):
        archivo = open("registro_boton.txt", "a")
        archivo.write(self.nombre + " " + self.modelo + " estado boton: " + estado + "\n")
        archivo.close()


class RobotMedico(Robot):
    def __init__(self, nombre, modelo, actividad, led_pin, pin_dht):
        super().__init__(nombre, modelo, led_pin)
        self.actividad = actividad
        self.sensor = adafruit_dht.DHT11(board.D4)

    def diagnosticar(self):
        temperatura = self.sensor.temperature
        humedad = self.sensor.humidity

        if temperatura is not None and humedad is not None:
            print("Temp:", temperatura, "Humedad:", humedad)
            self.registrar_dht(temperatura, humedad)
        else:
            print("Leyendo...")

        time.sleep(2)

    def registrar_dht(self, temperatura, humedad):
        archivo = open("registro_dht11.txt", "a")
        archivo.write("Temp: " + str(temperatura) + " Humedad: " + str(humedad) + "\n")
        archivo.close()


