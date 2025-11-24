import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




class Robot:
    def __init__(self, nombre, modelo, led_pin):
        self.nombre = nombre
        self.modelo = modelo
        self.led = led_pin

        GPIO.setup(self.led, GPIO.OUT)
        GPIO.output(self.led, 0)

    def encender(self):
        GPIO.output(self.led, 1)
        return self.nombre, "encendido"

    def apagar(self):
        GPIO.output(self.led, 0)
        return self.nombre, "apagado"

    def estado(self):
        return "Robot:", self.nombre, "Modelo:", self.modelo


class RobotExplorador(Robot):
    def __init__(self, nombre, modelo, zona, led_pin, btn_pin):
        super().__init__(nombre, modelo, led_pin)
        self.zona = zona
        self.btn = btn_pin
        GPIO.setup(self.btn, GPIO.IN)

        self.explorando = False

    def iniciar_exploracion(self):
        self.explorando = True
        return self.nombre, "explorando zona:", self.zona

    def detener_exploracion(self):
        self.explorando = False
        GPIO.output(self.led, 0)
        return self.nombre, "exploracin detenida"

    def loop_explorar(self):
        while self.explorando:
            if GPIO.input(self.btn):  
                GPIO.output(self.led, 0)
                print(self.nombre, "ROBOT ENCENDIDO:ESPERA PULSO PARA EXPLORAR", self.zona)
            else:
                GPIO.output(self.led, 1)
                print("EXPLORANDO")

            time.sleep(0.5)




explorador = RobotExplorador("R-Explorer", "XJ-9", "Zona critica", 18, 25)





def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print("Recibido:", command)
    
    if "on robot" in command:
        r = explorador.encender()
        telegram_bot.sendMessage(chat_id, " ".join(map(str, r)))

    if "off robot" in command:
        r = explorador.apagar()
        telegram_bot.sendMessage(chat_id, " ".join(map(str, r)))

    
    if "estado" in command:
        r = explorador.estado()
        telegram_bot.sendMessage(chat_id, " ".join(map(str, r)))

    if "explorar" in command:
        r = explorador.iniciar_exploracion()
        telegram_bot.sendMessage(chat_id, " ".join(map(str, r)))
        explorador.loop_explorar()

    
    if "detener" in command:
        r = explorador.detener_exploracion()
        telegram_bot.sendMessage(chat_id, " ".join(map(str, r)))


telegram_bot = telepot.Bot("8374308621:AAEhpi0U1A4AkZPxQVzqObSXiuni6vHdzqA")

MessageLoop(telegram_bot, action).run_as_thread()

print("Bot funcionando...")

while True:
    time.sleep(10)
