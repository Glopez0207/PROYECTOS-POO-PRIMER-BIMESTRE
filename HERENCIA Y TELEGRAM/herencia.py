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

    def apagar(self):
        GPIO.output(self.led_pin, False)
        print(self.nombre, "(", self.modelo, ")", "esta apagado.")

    def estado(self):
        print("Robot:", self.nombre, "Modelo:", self.modelo)


class RobotExplorador(Robot):
    def __init__(self, nombre, modelo, zona_exploracion, led_pin, btn_pin):
        super().__init__(nombre, modelo, led_pin)
        self.zona_exploracion = zona_exploracion
        self.btn_pin = btn_pin

        GPIO.setup(self.btn_pin, GPIO.IN)

    def explorar(self):
        print("\nPresiona el boton para iniciar exploracion...")

        while True:
            if GPIO.input(self.btn_pin):   
                GPIO.output(self.led_pin, False)
                print(self.nombre, "(", self.modelo, ")", "robot esta esperando pulso para explorar la zona", self.zona_exploracion)
            else:
                GPIO.output(self.led_pin, True)
                print(self.nombre, "(", self.modelo, ")", "Explorando zona", self.zona_exploracion)
            time.sleep(0.5)





class RobotMedico(Robot):
    def __init__(self, nombre, modelo, especialidad, led_pin, pin_dht):
        super().__init__(nombre, modelo, led_pin)
        self.especialidad = especialidad
        self.pin_dht = pin_dht
        
        self.sensor = adafruit_dht.DHT11(getattr(board, f"D{self.pin_dht}"))

    def diagnosticar(self):
        print(self.nombre, "(", self.modelo, ")", "realizando especialidad:", self.especialidad)
        humedad = self.sensor.humidity
        temperatura = self.sensor.temperature
        if humedad is not None and temperatura is not None:
            print("Temperatura:", temperatura, "C  |  Humedad:", humedad, "%")
        else:
            print("Error al leer el sensor DHT11")



robot_inicial = Robot("Robot", "GEN-1", led_pin=18)

robot_inicial.encender()
time.sleep(5)

robot_inicial.apagar()

print("\nEsperando para iniciar robot explorador...")
time.sleep(3)

print("\n--- INICIO DEL ROBOT EXPLORADOR ---\n")

explorador = RobotExplorador("R-Explorer", "GEN-1", "Zona critica", 18, 25)

print("\n--- INICIO DEL ROBOT MEDICO ---\n")

medico = RobotMedico("MediBot", "GEN-2", "Diagnostico ambiental", 18, 4)
medico.encender()
medico.estado()

medico.diagnosticar()
time.sleep(3)
medico.diagnosticar()
time.sleep(3)
medico.diagnosticar()
time.sleep(3)

explorador.encender()
explorador.estado()
explorador.explorar()




