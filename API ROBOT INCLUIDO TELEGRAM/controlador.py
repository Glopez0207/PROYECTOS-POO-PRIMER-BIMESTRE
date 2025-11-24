import time
from modelo import RobotModel, RobotExploradorModel, RobotMedicoModel
from vista import RobotView


class RobotController:
    def __init__(self):
        self.view = RobotView()

        self.robot_inicial = RobotModel("Robot", "GEN-1", 18)

        self.explorador = RobotExploradorModel(
            "R-Explorer", "GEN-1", "Zona critica", 23, 25
        )

        self.medico = RobotMedicoModel(
            "MediBot", "GEN-2", "Diagnostico ambiental", 24, 4
        )


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
