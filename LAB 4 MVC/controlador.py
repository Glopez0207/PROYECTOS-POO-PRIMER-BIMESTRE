import time
import telepot
from telepot.loop import MessageLoop

from modelo import RobotModel, RobotExploradorModel, RobotMedicoModel
from vista import RobotView

class RobotController:
    def __init__(self, token_telegram=None):
        self.view = RobotView()

        self.robot_inicial = RobotModel("Robot", "GEN-1", 18)

        self.explorador = RobotExploradorModel(
            "R-Explorer", "GEN-1", "Zona critica", 23, 25
        )

        self.medico = RobotMedicoModel(
            "MediBot", "GEN-2", "Diagnostico ambiental", 24, 4
        )

        # ? TELEGRAM INTEGRADO DENTRO DEL CONTROLADOR
        if token_telegram is not None:
            self.bot = telepot.Bot(token_telegram)
            MessageLoop(self.bot, self.manejar_telegram).run_as_thread()
            print("BOT TELEGRAM ACTIVO")

        self.ultimo_estado_boton = 0

    # ? MTODOS ORIGINALES
    def encender_robot_inicial(self):
        self.robot_inicial.encender()
        self.view.mostrar(self.robot_inicial.nombre, "encendido")

    def apagar_robot_inicial(self):
        self.robot_inicial.apagar()
        self.view.mostrar(self.robot_inicial.nombre, "apagado")

    def diagnosticar_medico(self):
        datos = self.medico.diagnosticar()
        if datos is not None:
            t, h = datos
            self.view.mostrar("Temperatura:", t, "Humedad:", h)
        else:
            self.view.mostrar("Error al leer sensor DHT11")

    def explorar_robot(self):
        self.view.mostrar("Iniciando exploracion...")
        self.explorador.explorar()

    # ? MTODO TELEGRAM DENTRO DEL CONTROLADOR
    def manejar_telegram(self, msg):
     chat_id = msg['chat']['id']
     comando = msg['text'].lower()

    if comando == 'on':
        self.robot_inicial.encender()
        self.bot.sendMessage(chat_id, "LED encendido")
        self.registrar_log("LED encendido desde Telegram")

    elif comando == 'off':
        self.robot_inicial.apagar()
        self.bot.sendMessage(chat_id, "LED apagado")
        self.registrar_log("LED APAGADO desde Telegram")

    elif comando == 'status':
        self.bot.sendMessage(chat_id, f"Estado: {self.robot_inicial.estado()}")

    elif comando == 'pulse':
        estado = self.explorador.leer_boton()

        if estado == 1 and self.ultimo_estado_boton == 0:
            self.bot.sendMessage(chat_id, "Pulso detectado")
            self.robot_inicial.encender()
            self.registrar_log("Pulso fsico detectado")

        elif estado == 0 and self.ultimo_estado_boton == 1:
            self.bot.sendMessage(chat_id, "Botn liberado")
            self.robot_inicial.apagar()
            self.registrar_log("Botn fsico liberado")

        self.ultimo_estado_boton = estado

    elif comando == 'dht':
        t, h = self.medico.leer_dht()
        if t is None or h is None:
            self.bot.sendMessage(chat_id, "Error al leer DHT11")
            self.registrar_log("Error al leer DHT11 desde Telegram (comando: dht)")
        else:
            mensaje = "Temperatura: " + str(t) + " C  Humedad: " + str(h) + " %"
            self.bot.sendMessage(chat_id, mensaje)
            self.registrar_log("Lectura DHT11 desde Telegram -> " + mensaje)

    elif comando == '/log':
        contenido = self.obtener_ultimo_log(20)
        if contenido is None or contenido.strip() == "":
            self.bot.sendMessage(chat_id, "Historial vaco.")
        else:
            self.bot.sendMessage(chat_id, "?? LTIMAS ACCIONES:\n" + contenido)
        self.registrar_log("Historial solicitado desde Telegram (comando: /log)")

    else:
        self.bot.sendMessage(chat_id, "Comandos vlidos: on, off, status, pulse, dht, /log")

       

    
        
