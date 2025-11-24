from controlador import RobotController
import time

controller = RobotController()

controller.encender_robot_inicial()
time.sleep(5)

controller.apagar_robot_inicial()
time.sleep(3)

controller.view.titulo("ROBOT MEDICO")

controller.diagnosticar_medico()
time.sleep(3)
controller.diagnosticar_medico()
time.sleep(3)
controller.diagnosticar_medico()
time.sleep(3)

controller.view.titulo("ROBOT EXPLORADOR")

controller.explorar_robot()
