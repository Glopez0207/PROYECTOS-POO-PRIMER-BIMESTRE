import time
from modelo import Robot, RobotExplorador, RobotMedico
from vista import mostrar_titulo

def ejecutar_robot_inicial():
    robot_inicial = Robot("Robot", "GEN-1", 18)
    robot_inicial.encender()
    time.sleep(10)
    robot_inicial.apagar()


def ejecutar_robot_explorador():
    mostrar_titulo("ROBOT EXPLORADOR")
    explorador = RobotExplorador("R-Explorer", "GEN-1", "Zona critica", 18, 25)

    for i in range(10):
        explorador.ciclo_exploracion()


def ejecutar_robot_medico():
    mostrar_titulo("ROBOT MEDICO")
    medico = RobotMedico("MediBot", "GEN-2", "Diagnostico ambiental", 18, 4)
    medico.encender()

    for i in range(20):
        medico.diagnosticar()

